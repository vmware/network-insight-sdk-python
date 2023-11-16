import queue
import threading
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.log_handler.log_queue import LogQueue
from databus_client.utils.common.databus_constants import DatabusMessageGroup


class DatabusMetricDbHandler:
    """
    Due to high inflow of metric data, multiple threads are required to push the data in mongo at once.
    Using multi-threaded buffering approach we have achieved faster timings in number of data-objects pushed in
    mongo.

    POST CALL >> Metric Queue (processes and gives data to DbHandler queue) >> DbHandlerQueue (pushes data to mongo)

    This approach works as we do not need ordering anywhere as data when fetched is re-ordered in-memory as per test requirement.

    """
    _instance = None
    _queue = queue.Queue()
    num_of_worker_threads = 10
    exception_logger = None

    def __init__(self):
        for i in range(self.num_of_worker_threads):
            t = threading.Thread(target=self.start_processing_data)
            t.start()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabusMetricDbHandler()

        return cls._instance

    def add_to_queue(self, data, message_group):
        return self._queue.put((data, message_group))

    def set_ex_logger(cls):
        if cls.exception_logger:
            pass
        else:
            cls.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception")

    def start_processing_data(cls):
        while True:
            metric_data = None
            license_plate = None
            try:
                metric_data, message_group = cls._queue.get(block=False)
                if message_group == DatabusMessageGroup.METRICS.value:
                    DatabusClientDataService.put_new_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.VMS_METRICS.value:
                    DatabusClientDataService.put_new_vms_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.HOSTS_METRICS.value:
                    DatabusClientDataService.put_new_hosts_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.FLOWS_METRICS.value:
                    DatabusClientDataService.put_new_flows_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.NICS_METRICS.value:
                    DatabusClientDataService.put_new_nics_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.SWITCHPORTS_METRICS.value:
                    DatabusClientDataService.put_new_switchports_metric_data_point(metric_data)
                elif message_group == DatabusMessageGroup.NSXT_EDGE_NODE_METRICS.value:
                    DatabusClientDataService.put_new_switchports_metric_data_point(metric_data)
                else:
                    message = "message_group {} NOT_SUPPORTED".format(message_group)
                    cls.exception_logger.log("Exception in Metrics DB handle: " + message)
                cls._queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occurred process message in DatabusMetricDbHandler. Trace : {}".format(
                    traceback.format_exc())
                cls.exception_logger.log("Exception in Metrics DB handler: " + message)
