from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.queues.entity_queues.databus_metric_queue import DatabusMetricsQueue


class DatabusNsxtEdgeNodeMetricsQueue(DatabusMetricsQueue):

    def __init__(self, use_mongo=True, message_group=None, file_threshold=None):
        super(DatabusNsxtEdgeNodeMetricsQueue, self).__init__(use_mongo=use_mongo, message_group=message_group, file_threshold=file_threshold)
        self.source_entity_id_lookup = dict()
        self.message_group = DatabusMessageGroup.NSXT_EDGE_NODE_METRICS.value
        self.num_of_worker_threads = 2,

