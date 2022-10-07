from databus_client.filters.filter_manager import FilterManager


class NonMetricFilter:

    @staticmethod
    def pass_non_metric_filter(source=None, entity_id=None, entity_name=None):
        filter_table = FilterManager().get_non_metric_filter_table()
        ret_flag = True
        if filter_table is None:
            return "NFC: No filters are configured as of now. Passing entry through filter"
        else:
            if source + ":" + entity_id + ":databus" in filter_table:
                ret_flag = NonMetricFilter.check_match_unmatch(data_pass=True)
            elif entity_name and source + ":" + entity_name + ":databus" in filter_table:
                ret_flag = NonMetricFilter.check_match_unmatch(data_pass=True)
            elif source + ":databus:databus" in filter_table:
                ret_flag = NonMetricFilter.check_match_unmatch(data_pass=True)
            else:
                ret_flag = NonMetricFilter.check_match_unmatch(data_pass=False)
        return ret_flag

    @staticmethod
    def check_match_unmatch(data_pass):
        match, unmatch = FilterManager().get_match_unmatch_filter()
        if data_pass:
            if match == "reject": return False
            else: return True
        else:
            if unmatch == "reject": return False
            else: return True
