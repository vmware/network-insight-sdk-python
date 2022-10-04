from databus_client.filters.filter_manager import FilterManager


class NonMetricFilter:

    @staticmethod
    def pass_non_metric_filter(source=None, entity_id=None, entity_name=None):
        f_manager = FilterManager()
        if source + ":" + entity_id + ":databus" in f_manager.get_non_metric_filter_table():
            ret_flag = NonMetricFilter.check_match_unmatch(data_pass=True)
        elif entity_name:
            if source + ":" + entity_name + ":databus" in f_manager.get_non_metric_filter_table():
                ret_flag = NonMetricFilter.check_match_unmatch(data_pass=True)
        else:
            ret_flag = NonMetricFilter.check_match_unmatch(data_pass=False)

        return ret_flag

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
