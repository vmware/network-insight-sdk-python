
import threading

from databus_client.queues.entity_queues.databus_application_queue import DatabusApplicationQueue
from databus_client.queues.entity_queues.databus_flows_queue import DatabusFlowsQueue
from databus_client.queues.entity_queues.databus_hosts_queue import DatabusHostsQueue
from databus_client.queues.entity_queues.databus_problems_queue import DatabusProblemsQueue
from databus_client.queues.entity_queues.databus_vms_queue import DatabusVmsQueue
from databus_client.queues.entity_queues.databus_metric_queue import DatabusMetricsQueue
from databus_client.queues.entity_queues.databus_flows_metrics_queue import DatabusFlowsMetricsQueue
from databus_client.queues.entity_queues.databus_hosts_metrics_queue import DatabusHostsMetricsQueue
from databus_client.queues.entity_queues.databus_nics_metrics_queue import DatabusNicsMetricsQueue
from databus_client.queues.entity_queues.databus_switchports_metrics_queue import DatabusSwitchPortsMetricsQueue
from databus_client.queues.entity_queues.databus_vms_metric_queue import DatabusVmsMetricsQueue
from databus_client.log_handler.databus_logger import DatabusLoggerHandler


class DatabusQueueManager:

    ENDPOINT_CLASS_MAP = {
        "applications": DatabusApplicationQueue,
        "problems": DatabusProblemsQueue,
        "flows": DatabusFlowsQueue,
        "vms": DatabusVmsQueue,
        "hosts": DatabusHostsQueue,
        "metrics": DatabusMetricsQueue,
        "vms-metrics": DatabusVmsMetricsQueue,
        "hosts-metrics": DatabusHostsMetricsQueue,
        "flows-metrics": DatabusFlowsMetricsQueue,
        "nics-metrics": DatabusNicsMetricsQueue,
        "switchports-metrics": DatabusSwitchPortsMetricsQueue
    }

    def __init__(self,
                 host_ip=None,
                 host_port=None,
                 use_mongo=True):

        self.q_processors = dict()

        for message_group, cls in self.ENDPOINT_CLASS_MAP.items():
            klass = globals()[cls.__name__]
            instance = klass(use_mongo=use_mongo, message_group=message_group)
            att_name = message_group+"_qProcessor"
            self.__setattr__(att_name, instance)
            self.q_processors.update({message_group: self.__getattribute__(att_name)})

        self.use_mongo = use_mongo

    def get_file_handler(self, databus_queue_list=None, host_ip=None, host_port=None, use_mongo=None):

        return DatabusLoggerHandler(databus_queue_list=databus_queue_list,
                                    host_ip=host_ip,
                                    host_port=host_port,
                                    use_mongo=use_mongo)

    def get_qp(self, message_group):
        if message_group in self.q_processors:
            return self.q_processors[message_group]
        else:
            print("Exception: " + "message_group {} not found in DatabusQueueManager q_processors".format(message_group))