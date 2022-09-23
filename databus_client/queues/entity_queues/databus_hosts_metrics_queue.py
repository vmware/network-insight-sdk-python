from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.queues.entity_queues.databus_metric_queue import DatabusMetricsQueue


class DatabusHostsMetricsQueue(DatabusMetricsQueue):

    def __init__(self, use_mongo=True, message_group=None):
        super(DatabusHostsMetricsQueue, self).__init__(use_mongo=use_mongo, message_group=message_group)
        self.source_entity_id_lookup = dict()
        self.message_group = DatabusMessageGroup.HOSTS_METRICS.value
        self.num_of_worker_threads = 2,

