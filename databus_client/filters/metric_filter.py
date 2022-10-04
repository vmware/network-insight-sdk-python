from databus_client.filters.filter_manager import FilterManager
from databus_client.utils.common.databus_constants import DatabusMessageGroup


class MetricFilter:

    @staticmethod
    def pass_metric_filter(source=None, entry=None, message_group=None):
        f_manager = FilterManager()
        pass_through = False
        check_key = source
        match_ent = entry
        match_points = []
        if message_group == DatabusMessageGroup.METRICS.value:
            filter_table = f_manager.metric_filter_table
        else:
            filter_table = f_manager.get_sub_metric_filter_table()

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

        if pass_through:
            return True, entry

        if check_key + ":databus:databus" in f_manager.get_metric_filter_table():
            pass_through = MetricFilter.check_match_unmatch(data_pass=True)
            return pass_through, entry
        else:
            pass_through = MetricFilter.check_match_unmatch(data_pass=False)
            return pass_through, entry

    @staticmethod
    def check_match_unmatch(data_pass):
        f_manager = FilterManager()
        match, unmatch = f_manager.get_match_unmatch_filter()
        if data_pass:
            if match == "reject": return False
            else: return True
        else:
            if unmatch == "reject": return False
            else: return True

    @staticmethod
    def unmatch():
        f_manager = FilterManager()
        match, unmatch = f_manager.get_match_unmatch_filter()
        if unmatch == "reject":
            return True
        else:
            return False

