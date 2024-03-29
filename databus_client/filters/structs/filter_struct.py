from databus_client.filters.structs.metric_struct import MetricStruct
from databus_client.filters.structs.non_metric_struct import NonMetricStruct
from databus_client.filters.structs.sub_metric_struct import SubMetricStruct


class FilterStruct:

    def __init__(self):
        self.matched_filter = str
        self.unmatched_filter = str
        self.non_metric_filter = list(NonMetricStruct())
        self.metric_filter = list(MetricStruct())
        self.sub_metric_filter = list(SubMetricStruct())

    def set_matched_filter(self, option):
        self.matched_filter = option

    def set_unmatched_filter(self, option):
        self.unmatched_filter = option