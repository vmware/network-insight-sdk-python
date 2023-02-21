import queue
import threading
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.log_handler.log_queue import LogQueue
from databus_client.utils.common.databus_queue_telemetry import DatabusQueueTelemetry
from databus_client.utils.databus_utilities import DatabusUtilities


class DatabusHeartBeatDbHandler:
    """
    Due to high inflow of heartbeat data, multiple threads are required to push the data in mongo at once.
    Using multi-threaded buffering approach we have achieved faster timings in number of data-objects pushed in
    mongo.

    POST CALL >> heartbeat Queue (processes and gives data to DbHandler queue) >> DbHandlerQueue (pushes data to mongo)

    This approach works as we do not need ordering anywhere as data when fetched is re-ordered in-memory as per test requirement.

    """
    _instance = None
    _queue = queue.Queue()
    num_of_worker_threads = 2

    def __init__(self, logger=None, ex_log=None):
        self.logger = logger
        self.license_plate = "[License Plate: " + DatabusUtilities.get_license_plate() + "]"
        self.exception_logger = ex_log
        for i in range(self.num_of_worker_threads):
            t = threading.Thread(target=self.start_processing_data)
            t.start()

    @classmethod
    def get_instance(cls, logger=None, ex_log=None):
        if cls._instance is None:
            cls._instance = DatabusHeartBeatDbHandler(logger=logger, ex_log=ex_log)

        return cls._instance

    def add_to_queue(self, data):
        return self._queue.put(data)

    def start_processing_data(self):
        while True:
            heartbeat_data = None
            try:
                heartbeat_data = self._queue.get(block=False)
                self.logger.log(self.license_plate + "Pushing HEARTBEAT to downstream")
                DatabusClientDataService.put_new_heartbeat_data_point(heartbeat_data)
                self.logger.log(self.license_plate + "HEARTBEAT pushed to downstream")
                self._queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occurred process message in DatabusheartbeatDbHandler. Trace : {}".format(
                    traceback.format_exc())
                self.exception_logger.log(self.license_plate + "Exception: " + message)
                DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)
