import collections
import copy

import databus_client

non_metric_message_group = ["applications", "vms", "flows", "hosts", "problems"]
sub_metrics_message_group = ["vms-metrics", "hosts-metrics", "flows-metrics", "hosts-metrics", "nics-metrics",
                             "switchports-metrics"]


class UpdateFilter:
    """
    Update the filter and return the updated copy
    """
    @staticmethod
    def update_filers(update_dict=None):
        new_filters = dict()
        morigi_filters = databus_client.filters.filter_manager.FilterManager().get_filters()
        m_filters = copy.deepcopy(morigi_filters)
        entity_not_found = []
        if "matched_filter" in update_dict and update_dict["matched_filter"] not in [None, "", "na", "NA"]:
            new_filters["matched_filter"] = update_dict["matched_filter"]
        else: new_filters["matched_filter"] = m_filters["matched_filter"]
        if "unmatched_filter" in update_dict and update_dict["unmatched_filter"] not in [None, "", "na", "NA"]:
            new_filters["unmatched_filter"] = update_dict["unmatched_filter"]
        else: new_filters["unmatched_filter"] = m_filters["unmatched_filter"]

        new_filters["non_metric_filter"] = []
        new_filters["sub_metric_filter"] = []
        new_filters["metric_filter"] = []

        if "message_group" in update_dict and update_dict["message_group"] in non_metric_message_group:
            # Check if source exists in existing config
            if update_dict["source"] in UpdateFilter.get_non_metric_source_list(com_filter=m_filters):
                for entry in m_filters["non_metric_filter"]:
                    nm_struct = collections.namedtuple("NonMetricStruct", entry.keys())(*entry.values())
                    if update_dict["source"] == entry["source"] and update_dict["message_group"] == entry["entity_type"]:
                        if "entityId" in update_dict and update_dict["entityId"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["entityId"]) == list:
                                    nm_struct.entityIds.extend(update_dict["entityId"])
                                elif type(update_dict["entityId"]) == str:
                                    nm_struct.entityIds.append(update_dict["entityId"])
                            else:
                                for eid in update_dict["entityId"]:
                                    if eid in nm_struct.entityIds:
                                        nm_struct.entityIds.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                        if "entityName" in update_dict and update_dict["entityName"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["entityName"]) == list:
                                    nm_struct.entityNames.extend(update_dict["entityName"])
                                elif type(update_dict["entityName"]) == list:
                                    nm_struct.entityNames.append(update_dict["entityName"])
                            else:
                                for eid in update_dict["entityName"]:
                                    if eid in nm_struct.entityNames:
                                        nm_struct.entityNames.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                    new_filters["non_metric_filter"].append(UpdateFilter.get_non_metric_struct_dict(nm_struct))
            else:
                new_filters["non_metric_filter"] = m_filters["non_metric_filter"]
                if update_dict["action"] == "add":
                    nm_dict = UpdateFilter.set_non_metric(fil_dict=update_dict)
                    new_filters["non_metric_filter"].append(nm_dict)
                else:
                    entity_not_found.append(update_dict["source"])
        else:
            new_filters["non_metric_filter"] = m_filters["non_metric_filter"]

        if "message_group" in update_dict and update_dict["message_group"] in sub_metrics_message_group:
            # Check if source exists in existing config
            if update_dict["source"] in UpdateFilter.get_sub_metric_source_list(com_filter=m_filters):
                for entry in m_filters["sub_metric_filter"]:
                    m_struct = collections.namedtuple("SubMetricStruct", entry.keys())(*entry.values())
                    if update_dict["source"] == entry["source"] and update_dict["message_group"] == entry["entity_type"]:
                        if "entityId" in update_dict and update_dict["entityId"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["entityId"]) == list:
                                    m_struct.entityIds.extend(update_dict["entityId"])
                                elif type(update_dict["entityId"]) == str:
                                    m_struct.entityIds.append(update_dict["entityId"])
                            else:
                                for eid in update_dict["entityId"]:
                                    if eid in m_struct.entityIds:
                                        m_struct.entityIds.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                        if "metric" in update_dict and update_dict["metric"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["metric"]) == list:
                                    m_struct.metrics.extend(update_dict["metric"])
                                elif type(update_dict["metric"]) == str:
                                    m_struct.metrics.append(update_dict["metric"])
                            else:
                                for eid in update_dict["metric"]:
                                    if eid in m_struct.metrics:
                                        m_struct.metrics.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                    new_filters["sub_metric_filter"].append(UpdateFilter.get_metric_struct_dict(m_struct))
            else:
                new_filters["sub_metric_filter"] = m_filters["sub_metric_filter"]
                if update_dict["action"] == "add":
                    nm_dict = UpdateFilter.set_sub_metric(fil_dict=update_dict)
                    new_filters["sub_metric_filter"].append(nm_dict)
                else:
                    entity_not_found.append(update_dict["source"])
        else:
            new_filters["sub_metric_filter"] = m_filters["sub_metric_filter"]

        if "message_group" in update_dict and update_dict["message_group"] == "metrics":
            # Check if source exists in existing config
            if update_dict["source"] in UpdateFilter.get_metric_source_list(com_filter=m_filters):
                for entry in m_filters["metric_filter"]:
                    sub_struct = collections.namedtuple("MetricStruct", entry.keys())(*entry.values())
                    if update_dict["source"] == entry["source"] and update_dict["metric_entity"] == entry["entity_type"]:
                        if "entityId" in update_dict and update_dict["entityId"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["entityId"]) == list:
                                    sub_struct.entityIds.extend(update_dict["entityId"])
                                elif type(update_dict["entityId"]) == str:
                                    sub_struct.entityIds.append(update_dict["entityId"])
                            else:
                                for eid in update_dict["entityId"]:
                                    if eid in sub_struct.entityIds:
                                        sub_struct.entityIds.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                        if "metric" in update_dict and update_dict["metric"] not in [None, "", "na", "NA"]:
                            if update_dict["action"] == "add":
                                if type(update_dict["metric"]) == list:
                                    sub_struct.metrics.extend(update_dict["metric"])
                                elif type(update_dict["metric"]) == str:
                                    sub_struct.metrics.append(update_dict["metric"])
                            else:
                                for eid in update_dict["metric"]:
                                    if eid in sub_struct.metrics:
                                        sub_struct.metrics.remove(eid)
                                    else:
                                        entity_not_found.append(eid)
                    new_filters["metric_filter"].append(UpdateFilter.get_metric_struct_dict(sub_struct))
            else:
                new_filters["metric_filter"] = m_filters["metric_filter"]
                if update_dict["action"] == "add":
                    nm_dict = UpdateFilter.set_metric(fil_dict=update_dict)
                    new_filters["metric_filter"].append(nm_dict)
                else:
                    entity_not_found.append(update_dict["source"])
        else:
            new_filters["metric_filter"] = m_filters["metric_filter"]

        return new_filters, entity_not_found

    @staticmethod
    def get_non_metric_source_list(com_filter=None):
        source_list = []
        for i in com_filter["non_metric_filter"]:
            i = collections.namedtuple("NonMetricStruct", i.keys())(*i.values())
            source_list.append(i.source)
        return source_list

    @staticmethod
    def get_sub_metric_source_list(com_filter=None):
        source_list = []
        for i in com_filter["sub_metric_filter"]:
            i = collections.namedtuple("SubMetricStruct", i.keys())(*i.values())
            source_list.append(i.source)
        return source_list

    @staticmethod
    def get_metric_source_list(com_filter=None):
        source_list = []
        for i in com_filter["metric_filter"]:
            i = collections.namedtuple("MetricStruct", i.keys())(*i.values())
            source_list.append(i.source)
        return source_list

    @staticmethod
    def get_non_metric_struct_dict(obj):
        m_dict = dict()
        m_dict.update({
            "source": obj.source,
            "entity_type": obj.entity_type if hasattr(obj, "entity_type") else "",
            "entityIds": obj.entityIds if hasattr(obj, "entityIds") else [],
            "entityNames": obj.entityNames if hasattr(obj, "entityNames") else [],
        })
        return m_dict

    @staticmethod
    def get_metric_struct_dict(obj):
        m_dict = dict()
        m_dict.update({
            "source": obj.source,
            "entity_type": obj.entity_type if hasattr(obj, "entity_type") else "",
            "entityIds": obj.entityIds if hasattr(obj, "entityIds") else [],
            "metrics": obj.metrics if hasattr(obj, "metrics") else [],
        })
        return m_dict

    @staticmethod
    def set_non_metric(fil_dict=None):
        m_dict = dict()
        m_dict.update({
            "source": fil_dict["source"],
            "entity_type": fil_dict["message_group"],
            "entityIds": fil_dict["entityId"] if "entityId" in fil_dict and fil_dict["entityId"] not in [None, "", "na", "NA"] else [],
            "entityNames": fil_dict["entityName"] if "entityName" in fil_dict and fil_dict["entityName"] not in [None, "", "na", "NA"]  else [],
        })
        return m_dict

    @staticmethod
    def set_sub_metric(fil_dict=None):
        m_dict = dict()
        m_dict.update({
            "source": fil_dict["source"],
            "entity_type": fil_dict["message_group"],
            "entityIds": fil_dict["entityId"] if "entityId" in fil_dict and fil_dict["entityId"] not in [None, "", "na", "NA"] else [],
            "metrics": fil_dict["metric"] if "metric" in fil_dict and fil_dict["metric"] not in [None, "", "na", "NA"]  else [],
        })
        return m_dict

    @staticmethod
    def set_metric(fil_dict=None):
        m_dict = dict()
        m_dict.update({
            "source": fil_dict["source"],
            "entity_type": fil_dict["metric_entity"] if "metric_entity" in fil_dict and fil_dict["metric_entity"] not in [None, "", "na", "NA"] else [],
            "entityIds": fil_dict["entityId"] if "entityId" in fil_dict and fil_dict["entityId"] not in [None, "", "na", "NA"] else [],
            "metrics": fil_dict["metric"] if "metric" in fil_dict and fil_dict["metric"] not in [None, "", "na", "NA"]  else [],
        })
        return m_dict


if __name__ == "__main__":
    update_dict = {
        "matched_filter": "",
        "unmatched_filter": "reject",
        "action": "add",
        "source": "CKRtEgdEUjNITU1P23",
        "message_group": "applications",
        "entityId": ["13988:561:2096623162362547540"],
        "entityName": "",
        "metric_entity": "",
        "metric": []
    }
    # update_dict = {
    #     "matched_filter": "",
    #     "unmatched_filter": "",
    #     "action": "delete",
    #     "source": "SOURCE_TWO",
    #     "message_group": "metrics",
    #     "entityId": ["v1"],
    #     "entityName": "",
    #     "metric_entity": "Hosts",
    #     "metric": ["three"]
    # }
    print(UpdateFilter().update_filers(update_dict=update_dict))
