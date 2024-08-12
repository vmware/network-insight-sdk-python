import queue
import threading
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.queues.databus_queue import DatabusQueue
from databus_client.utils.databus_utilities import DatabusUtilities


class DatabusBearerTokens(DatabusQueue):
    _instance = None
    _queue = queue.Queue()
    num_of_worker_threads = 4

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
            cls._instance = DatabusBearerTokens(logger=logger, ex_log=ex_log)

        return cls._instance

    def add_to_queue(self, data):
        return self._queue.put(data)

    def start_processing_data(self):
        while True:
            token_data = None
            try:
                token_data = self._queue.get(block=False)
                self.logger.log(self.license_plate + "Processing bearer token")
                DatabusClientDataService.update_bearer_token(token_data)
                self._queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occurred process message in Databus bearer token processing. Trace : {}".format(
                    traceback.format_exc())
                self.exception_logger.log(self.license_plate + "Exception: " + message)
