from databus_client.filters.filter_manager import FilterManager
from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.utils.common.databus_queue_telemetry import DatabusQueueTelemetry


class MetricFilter:

    @staticmethod
    def pass_metric_filter(source=None, entry=None, message_group=None):
        pass_through = False
        check_key = source
        match_ent = entry
        match_points = []
        if message_group == DatabusMessageGroup.METRICS.value:
            filter_table = FilterManager().metric_filter_table
        else:
            filter_table = FilterManager().get_sub_metric_filter_table()

        if filter_table is None:
            return True, "NFC: No filters are configured as of now. Passing entry through filter"
        else:
            for m_id in match_ent["data"]["points"]:
                key = source + ":" + m_id["entity_id"]
                if key + ":" + match_ent["data"]["metric"] in filter_table:
                    pass_through = MetricFilter.check_match_unmatch(data_pass=True)
                else:
                    if key + ":databus" in filter_table:
                        pass_through = MetricFilter.check_match_unmatch(data_pass=True)
                    else:
                        match_points.append(m_id)

            if MetricFilter.unmatch():
                if len(match_points) > 0:
                    for mp_ent in match_points:
                        entry["data"]["points"].remove(mp_ent)
                DatabusQueueTelemetry().update_filter_telemetry(call_type="REMOVED_BY_FILTER", message_group=message_group)

            if pass_through:
                return True, entry

            if check_key + ":databus:databus" in FilterManager().get_metric_filter_table():
                pass_through = MetricFilter.check_match_unmatch(data_pass=True)
                return pass_through, entry
            else:
                pass_through = MetricFilter.check_match_unmatch(data_pass=False)
                return pass_through, entry

    @staticmethod
    def check_match_unmatch(data_pass):
        match, unmatch = FilterManager().get_match_unmatch_filter()
        if data_pass:
            if match == "reject": return False
            else: return True
        else:
            if unmatch == "reject": return False
            else: return True

    @staticmethod
    def unmatch():
        match, unmatch = FilterManager().get_match_unmatch_filter()
        if unmatch == "reject":
            return True
        else:
            return False

