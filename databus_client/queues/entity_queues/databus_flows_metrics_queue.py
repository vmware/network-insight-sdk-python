from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.queues.entity_queues.databus_metric_queue import DatabusMetricsQueue


class DatabusFlowsMetricsQueue(DatabusMetricsQueue):

    def __init__(self, debug_logs=False, use_mongo=True, message_group=None):
        super(DatabusFlowsMetricsQueue, self).__init__(debug_logs=debug_logs, use_mongo=use_mongo, message_group=message_group)
        self.source_entity_id_lookup = dict()
        self.message_group = DatabusMessageGroup.FLOWS_METRICS.value
        self.num_of_worker_threads = 2,

