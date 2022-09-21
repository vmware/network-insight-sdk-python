from databus_client.queues.filters.structs.metric_struct import MetricStruct
from databus_client.queues.filters.structs.non_metric_struct import NonMetricStruct
from databus_client.queues.filters.structs.sub_metric_struct import SubMetricStruct


class FilterStruct:

    def __init__(self):
        self.matched_filter = str
        self.unmatched_filter = str
        self.non_metric_filter = list(NonMetricStruct())
        self.new_metric_filter = list(MetricStruct())
        self.sub_metric_filter = list(SubMetricStruct())
