import collections
import json
import os
import threading
from pprint import pprint

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "filter.json"))
f = open(path)

non_metric_message_group = ["applications", "vms", "flows", "hosts", "problems"]
sub_metrics_message_group = ["vms-metrics", "hosts-metrics", "flows-metrics", "hosts-metrics", "nics-metrics",
                             "switchports-metrics"]


def singleton(class_):
    lock = threading.Lock()
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            with lock:
                instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class FilterManager:
    non_metric_filter_table = dict()
    metric_filter_table = dict()
    sub_metric_filter_table = dict()
    use_local = False

    def __init__(self):
        self.non_metric_filter_table = self.get_non_metric_filter_table()
        self.metric_filter_table = self.get_metric_filter_table()
        self.sub_metric_filter_table = self.get_sub_metric_filter_table()

    def set_use_local(self, flag):
        self.use_local = flag

    def set_filters(self, filter_dict=None):
        # To access from local file use below

        if self.use_local:
            file = open(path, "w")  # append mode
            file.write(str(json.dumps(filter_dict)) + "\n")
            file.close()
        else:
            # Accessing from database
            DatabusClientDataService.put_filters(filter_dict)

    def update_filters(self, filter_dict=None):
        update_message = dict()
        try:
            m_filters = self.get_filters()
            if m_filters is None:
                return "Filters not configured. Set filters first"
            # m_filters = collections.namedtuple("FilterStruct", m_filters.keys())(*m_filters.values())

            if "matched_filter" in filter_dict and filter_dict["matched_filter"] is not None:
                m_filters["matched_filter"] = filter_dict["matched_filter"]

            if "unmatched_filter" in filter_dict and filter_dict["unmatched_filter"] is not None:
                m_filters["unmatched_filter"] = filter_dict["unmatched_filter"]
            source_found = True
            """Updating the non_metrics"""
            if "message_group" in filter_dict and filter_dict["message_group"] in non_metric_message_group:
                for i in m_filters["non_metric_filter"]:
                    i = collections.namedtuple("NonMetricStruct", i.keys())(*i.values())
                    if i.source == filter_dict["source"] and i.entity_type == filter_dict["message_group"]:
                        if i.entityIds and "entityId" in filter_dict and filter_dict["entityId"] is not None:
                            not_found_entities = []
                            for entry in filter_dict["entityId"]:
                                if filter_dict["action"] == "add":
                                    i.entityIds.append(entry)
                                else:
                                    if entry in i.entityIds:
                                        i.entityIds.remove(entry)
                                    else:
                                        not_found_entities.append(entry)
                            if len(not_found_entities) > 0:
                                message = "EntityID {} is not present in current configuration to delete".format(
                                    str(not_found_entities))
                                update_message["Issue in Non Metric Entity ID Update: "] = message
                            else:
                                # m_dict = self.my_dict(m_filters)
                                self.set_filters(m_filters)
                                message = "EntityID {} added to source {}".format(str(filter_dict["entityId"]),
                                                                                  filter_dict["source"])
                                update_message["Non Metric Entity ID Update: "] = message
                        if "entityName" in filter_dict and filter_dict["entityName"] is not None:
                            not_found_entities = []
                            for entry in filter_dict["entityName"]:
                                if filter_dict["action"] == "add":
                                    i.entityNames.append(entry)
                                else:
                                    if entry in i.entityNames:
                                        i.entityNames.remove(entry)
                                    else:
                                        not_found_entities.append(entry)
                            if len(not_found_entities) > 0:
                                message = "EntityName {} is not present in current configuration to delete".format(
                                    str(not_found_entities))
                                update_message["Issue in Non Metric Entity Name Update: "] = message
                            else:
                                # m_dict = self.my_dict(m_filters)
                                self.set_filters(m_filters)
                                message = "EntityName {} added to source {}".format(str(filter_dict["entityName"]),
                                                                                    filter_dict["source"])
                                update_message["Non Metric Entity Name Update: "] = message
                    else:
                        source_found = False

                if not source_found:
                    upd_dict = dict()
                    upd_dict["source"] = filter_dict["source"]
                    if filter_dict["message_group"] is not "" or filter_dict["message_group"] is not None:
                        upd_dict["message_group"] = filter_dict["message_group"]
                    if filter_dict["entityId"] is not "" or filter_dict["entityId"] is not None:
                        upd_dict["entityIds"] = filter_dict["entityId"]
                    if filter_dict["entityName"] is not "" or filter_dict["entityName"] is not None:
                        upd_dict["entityNames"] = filter_dict["entityName"]
                    upd_list = [upd_dict]
                    m_filters["non_metric_filter"].extend(upd_list)
                    # m_dict = self.my_dict(m_filters)
                    self.set_filters(m_filters)
                    source_found = True

            elif "message_group" in filter_dict and filter_dict["message_group"] in sub_metrics_message_group:
                """Updating the sub_metrics"""
                for i in m_filters["sub_metric_filter"]:
                    i = collections.namedtuple("SubMetricStruct", i.keys())(*i.values())
                    if i.source == filter_dict["source"]:
                        if i.entity_type == filter_dict["message_group"]:
                            if "entityId" in filter_dict and filter_dict["entityId"] is not None:
                                not_found_entities = []
                                for entry in filter_dict["entityId"]:
                                    if filter_dict["action"] == "add":
                                        i.entityIds.append(entry)
                                    else:
                                        if entry in i.entityIds:
                                            i.entityIds.remove(entry)
                                        else:
                                            not_found_entities.append(entry)
                                if len(not_found_entities) > 0:
                                    message = "EntityID {} is not present in current configuration to delete".format(
                                        str(not_found_entities))
                                    update_message["Issue in Sub metric EntityId update: "] = message
                                else:
                                    # m_dict = self.my_dict(m_filters)
                                    self.set_filters(m_filters)
                                    message = "EntityID {} added to source {}".format(str(filter_dict["entityId"]),
                                                                                      filter_dict["source"])
                                    update_message["Sub metric EntityId update: "] = message
                            if "metric" in filter_dict and filter_dict["metric"] is not None:
                                not_found_entities = []
                                for entry in filter_dict["metric"]:
                                    if filter_dict["action"] == "add":
                                        i.metrics.append(entry)
                                    else:
                                        if entry in i.metrics:
                                            i.metrics.remove(entry)
                                        else:
                                            not_found_entities.append(entry)
                                if len(not_found_entities) > 0:
                                    message = "Metric {} is not present in current configuration to delete".format(
                                        str(not_found_entities))
                                    update_message["Issue in Sub metric update: "] = message
                                else:
                                    # m_dict = self.my_dict(m_filters)
                                    self.set_filters(m_filters)
                                    message = "Metric {} added to source {}".format(str(filter_dict["metric"]),
                                                                                    filter_dict["source"])
                                    update_message["Sub metric update: "] = message
                    else:
                        source_found = False

                if not source_found:
                    upd_dict = dict()
                    upd_dict["source"] = filter_dict["source"]
                    if filter_dict["message_group"] is not "" or filter_dict["message_group"] is not None:
                        upd_dict["message_group"] = filter_dict["message_group"]
                    if filter_dict["entityId"] is not "" or filter_dict["entityId"] is not None:
                        upd_dict["entityIds"] = filter_dict["entityId"]
                    if filter_dict["entityName"] is not "" or filter_dict["entityName"] is not None:
                        upd_dict["entityNames"] = filter_dict["entityName"]
                    upd_list = [upd_dict]
                    m_filters["non_metric_filter"].extend(upd_list)
                    # m_dict = self.my_dict(m_filters)
                    self.set_filters(m_filters)
                    source_found = True

            elif "message_group" in filter_dict:
                for i in m_filters["sub_metric_filter"]:
                    i = collections.namedtuple("MetricStruct", i.keys())(*i.values())
                    if i.source == filter_dict["source"]:
                        if i.entity_type == filter_dict["metric_entity"]:
                            if "entityId" in filter_dict and filter_dict["entityId"] is not None:
                                not_found_entities = []
                                for entry in filter_dict["entityId"]:
                                    if filter_dict["action"] == "add":
                                        i.entityIds.append(entry)
                                    else:
                                        if entry in i.entityIds:
                                            i.entityIds.remove(entry)
                                        else:
                                            not_found_entities.append(entry)
                                if len(not_found_entities) > 0:
                                    message = "EntityID {} is not present in current configuration to delete".format(
                                        str(not_found_entities))
                                    update_message["Issue in Metric EntityId update: "] = message
                                else:
                                    # m_dict = self.my_dict(m_filters)
                                    self.set_filters(m_filters)
                                    message = "EntityID {} added to source {}".format(str(filter_dict["entityId"]),
                                                                                      filter_dict["source"])
                                    update_message["Metric EntityId update: "] = message
                            elif "metric" in filter_dict and filter_dict["metric"] is not None:
                                not_found_metrics = []
                                for entry in filter_dict["metric"]:
                                    if filter_dict["action"] == "add":
                                        i.metrics.append(entry)
                                    else:
                                        if entry in i.entityIds:
                                            i.metrics.remove(entry)
                                        else:
                                            not_found_metrics.append(entry)
                                if len(not_found_metrics) > 0:
                                    message = "Metrics {} is not present in current configuration to delete".format(
                                        str(not_found_metrics))
                                    update_message["Issue in Metric update: "] = message
                                else:
                                    # m_dict = self.my_dict(m_filters)
                                    self.set_filters(m_filters)
                                    message = "Metrics {} added to source {}".format(str(filter_dict["metric"]),
                                                                                     filter_dict["source"])
                                    update_message["Metric update: "] = message
                    else:
                        source_found = False

                if not source_found:
                    upd_dict = dict()
                    upd_dict["source"] = filter_dict["source"]
                    if filter_dict["message_group"] is not "" or filter_dict["message_group"] is not None:
                        upd_dict["message_group"] = filter_dict["message_group"]
                    if filter_dict["entityId"] is not "" or filter_dict["entityId"] is not None:
                        upd_dict["entityIds"] = filter_dict["entityId"]
                    if filter_dict["entityName"] is not "" or filter_dict["entityName"] is not None:
                        upd_dict["entityNames"] = filter_dict["entityName"]
                    upd_list = [upd_dict]
                    m_filters["non_metric_filter"].extend(upd_list)
                    # m_dict = self.my_dict(m_filters)
                    self.set_filters(m_filters)
                    source_found = True

            self.set_filters(m_filters)
            if update_message:
                return update_message
            else:
                return {"Update process": "Done"}
        except Exception as e:
            raise Exception

    def delete_filters(self, source=None):
        full_filters = self.get_filters()
        if full_filters is None:
            return False
        full_filters = collections.namedtuple("FilterStruct", full_filters.keys())(*full_filters.values())
        if source == "all":
            self.set_filters(None)
            return True
        else:
            m_filter = self.get_filters(source=source)
            if m_filter:
                m_filter = collections.namedtuple("FilterStruct", m_filter.keys())(*m_filter.values())
                if len(m_filter.non_metric_filter) > 0:
                    for i in m_filter.non_metric_filter:
                        if i in full_filters.non_metric_filter:
                            full_filters.non_metric_filter.remove(i)
                if len(m_filter.metric_filter) > 0:
                    for i in m_filter.metric_filter:
                        if i in full_filters.metric_filter:
                            full_filters.metric_filter.remove(i)
                if len(m_filter.sub_metric_filter) > 0:
                    for i in m_filter.sub_metric_filter:
                        if i in full_filters.sub_metric_filter:
                            full_filters.sub_metric_filter.remove(i)
            m_dict = self.my_dict(full_filters)
            self.set_filters(m_dict)
            return True

    def get_filters(self, source=None):
        # use_local fetches data from local file, else from db
        if self.use_local:
            file = open(path, "r")
            m_filters = json.loads(file.read())
            file.close
        else:
            m_filters = DatabusClientDataService.get_filters()

        if m_filters:
            if source:
                full_filters = collections.namedtuple("FilterStruct", m_filters.keys())(*m_filters.values())
                source_list = [source]
                source_filters = {"matched_filter": full_filters.matched_filter,
                                  "unmatched_filter": full_filters.unmatched_filter,
                                  "source": source_list}
                non_metric_list = []
                metric_list = []
                sub_metric_list = []
                for i in full_filters.non_metric_filter:
                    i = collections.namedtuple("NonMetricStruct", i.keys())(*i.values())
                    if i.source == source:
                        non_metric_list.append(i)
                for i in full_filters.metric_filter:
                    i = collections.namedtuple("MetricStruct", i.keys())(*i.values())
                    if i.source == source:
                        metric_list.append(i)
                for i in full_filters.sub_metric_filter:
                    i = collections.namedtuple("SubMetricStruct", i.keys())(*i.values())
                    if i.source == source:
                        sub_metric_list.append(i)
                source_filters["non_metric_filter"] = non_metric_list
                source_filters["metric_filter"] = metric_list
                source_filters["sub_metric_filter"] = sub_metric_list

                return source_filters

            return m_filters
        else:
            return None

    def get_application_filter(self, source=None):
        application_filter = self.extract_non_metric_filter(entity="applications", source=source)
        if not application_filter["entityIds"] and not application_filter["entityNames"]:
            return None
        print("Filters fetched for applications: " + json.dumps(application_filter))
        return application_filter

    def get_vms_filter(self, source=None):
        vms_filter = self.extract_non_metric_filter(entity="vms", source=source)
        if not vms_filter["entityIds"] and not vms_filter["entityNames"]:
            return None
        print("Filters fetched for vms: " + json.dumps(vms_filter))
        return vms_filter

    def get_hosts_filter(self, source=None):
        hosts_filter = self.extract_non_metric_filter(entity="hosts", source=source)
        if not hosts_filter["entityIds"] and not hosts_filter["entityNames"]:
            return None
        print("Filters fetched for hosts: " + json.dumps(hosts_filter))
        return hosts_filter

    def get_flows_filter(self, source=None):
        flows_filter = self.extract_non_metric_filter(entity="flows", source=source)
        if not flows_filter["entityIds"] and not flows_filter["entityNames"]:
            return None
        print("Filters fetched for flows: " + json.dumps(flows_filter))
        return flows_filter

    def get_problems_filter(self, source=None):
        problems_filter = self.extract_non_metric_filter(entity="problems", source=source)
        if not problems_filter["entityIds"] and not problems_filter["entityNames"]:
            return None
        print("Filters fetched for problems: " + json.dumps(problems_filter))
        return problems_filter

    def get_metrics_filter(self, source=None, entity=None):
        metrics_filter = self.extract_metric_filter(entity=entity, source=source)
        print("Metric filters fetched: " + json.dumps(metrics_filter))
        return metrics_filter

    def get_vms_metrics_filter(self, source=None):
        vms_metrics_filter = self.extract_sub_metric_filter(entity="vms-metrics", source=source)
        print("vms-metric filters fetched: " + json.dumps(vms_metrics_filter))
        return vms_metrics_filter

    def get_hosts_metrics_filter(self, source=None):
        hosts_metrics_filter = self.extract_sub_metric_filter(entity="hosts-metrics", source=source)
        print("hosts-metric filters fetched: " + json.dumps(hosts_metrics_filter))
        return hosts_metrics_filter

    def get_flows_metrics_filter(self, source=None):
        flows_metrics_filter = self.extract_sub_metric_filter(entity="flows-metrics", source=source)
        print("Metric filters fetched: " + json.dumps(flows_metrics_filter))
        return flows_metrics_filter

    def get_nics_metrics_filter(self, source=None):
        nics_metrics_filter = self.extract_sub_metric_filter(entity="nics-metrics", source=source)
        print("Metric filters fetched: " + json.dumps(nics_metrics_filter))
        return nics_metrics_filter

    def get_switchport_metrics_filter(self, source=None):
        switchports_metrics_filter = self.extract_sub_metric_filter(entity="switchports-metrics", source=source)
        print("Metric filters fetched: " + json.dumps(switchports_metrics_filter))
        return switchports_metrics_filter

    def get_non_metric_filter_table(self):
        non_metric_filter_dict = dict()
        f_filter = self.get_filters()
        if f_filter:
            f_filter = collections.namedtuple("FilterStruct", f_filter.keys())(*f_filter.values())
            for i in f_filter.non_metric_filter:
                i = collections.namedtuple("NonMetricStruct", i.keys())(*i.values())
                if i.source:
                    if hasattr(i, "entityIds"):
                        if len(i.entityIds) > 0:
                            for e_id in i.entityIds:
                                non_metric_filter_dict[self.getKey(source=i.source, entityId=e_id)] = ""
                    if hasattr(i, "entityNames"):
                        if len(i.entityNames) > 0:
                            for e_id in i.entityNames:
                                non_metric_filter_dict[self.getKey(source=i.source, entityId=e_id)] = ""
                    else:
                        non_metric_filter_dict[self.getKey(source=i.source)] = ""
            return non_metric_filter_dict
        else:
            return None

    def get_metric_filter_table(self):
        metric_filter_dict = dict()
        f_filter = self.get_filters()
        if f_filter:
            f_filter = collections.namedtuple("FilterStruct", f_filter.keys())(*f_filter.values())
            for i in f_filter.metric_filter:
                i = collections.namedtuple("MetricStruct", i.keys())(*i.values())
                if i.source:
                    if hasattr(i, "entityIds"):
                        if len(i.entityIds) > 0:
                            for e_id in i.entityIds:
                                if hasattr(i, "metrics"):
                                    if len(i.metrics) > 0:
                                        for m_name in i.metrics:
                                            metric_filter_dict[
                                                self.getKey(source=i.source, entityId=e_id, metricName=m_name)] = ""
                                else:
                                    metric_filter_dict[self.getKey(source=i.source, entityId=e_id)] = ""
                    else:
                        metric_filter_dict[self.getKey(source=i.source)] = ""
            return metric_filter_dict
        else:
            return None

    def get_sub_metric_filter_table(self):
        metric_filter_dict = dict()
        f_filter = self.get_filters()
        if f_filter:
            f_filter = collections.namedtuple("FilterStruct", f_filter.keys())(*f_filter.values())
            for i in f_filter.sub_metric_filter:
                i = collections.namedtuple("SubMetricStruct", i.keys())(*i.values())
                if i.source:
                    if hasattr(i, "entityIds"):
                        if len(i.entityIds) > 0:
                            for e_id in i.entityIds:
                                if hasattr(i, "metrics"):
                                    if len(i.metrics) > 0:
                                        for m_name in i.metrics:
                                            metric_filter_dict[
                                                self.getKey(source=i.source, entityId=e_id, metricName=m_name)] = ""
                                else:
                                    metric_filter_dict[self.getKey(source=i.source, entityId=e_id)] = ""
                    else:
                        metric_filter_dict[self.getKey(source=i.source)] = ""
            return metric_filter_dict
        else:
            return None

    def get_match_unmatch_filter(self):
        f_filter = self.get_filters()
        if f_filter:
            f_filter = collections.namedtuple("FilterStruct", f_filter.keys())(*f_filter.values())
            return f_filter.matched_filter, f_filter.unmatched_filter

    def getKey(self, source=None, entityId=None, metricName=None):
        key = ""
        if source:
            key = source
        if entityId:
            key = key + ":" + entityId
        else:
            key = key + ":" + "databus"
        if metricName:
            key = key + ":" + metricName
        else:
            key = key + ":" + "databus"
        return key

    def extract_non_metric_filter(self, source=None, entity=None):
        filter = self.get_filters(source=source)
        filter = collections.namedtuple("FilterStruct", filter.keys())(*filter.values())
        allowed_sources = []
        allowed_entityIds = []
        allowed_entityNames = []

        if source:
            for i in filter.non_metric_filter:
                if i.entity_type == entity and i.source == source:
                    allowed_entityIds.extend(i.entityIds)
                    allowed_entityNames.extend(i.entityNames)
            allowed_sources.append(source)

        else:
            for i in filter.non_metric_filter:
                i = collections.namedtuple("NonMetricStruct", i.keys())(*i.values())
                if i.entity_type == entity:
                    allowed_sources.append(i.source)
                    allowed_entityIds.extend(i.entityIds)
                    allowed_entityNames.extend(i.entityNames)

        return {"matched_filter": filter.matched_filter,
                "unmatched_filter": filter.unmatched_filter,
                "source": allowed_sources,
                "entityIds": allowed_entityIds,
                "entityNames": allowed_entityNames}

    def extract_metric_filter(self, source=None, entity=None):
        filter = self.get_filters(source=source)
        if filter:
            filter = collections.namedtuple("FilterStruct", filter.keys())(*filter.values())
            allowed_sources = []
            allowed_entityIds = []
            allowed_metrics = []

            if source:
                for i in filter.metric_filter:
                    if i.entity_type == entity and i.source == source:
                        allowed_entityIds.extend(i.entityIds)
                        allowed_metrics.extend(i.metrics)
                allowed_sources.append(source)
            else:
                for i in filter.metric_filter:
                    i = collections.namedtuple("MetricStruct", i.keys())(*i.values())
                    if i.entity_type == entity:
                        allowed_sources.append(i.source)
                        allowed_entityIds.extend(i.entityIds)
                        allowed_metrics.extend(i.metrics)

            return {"matched_filter": filter.matched_filter,
                    "unmatched_filter": filter.unmatched_filter,
                    "entity": entity,
                    "source": allowed_sources,
                    "entityIds": allowed_entityIds,
                    "metric": allowed_metrics}
        else:
            return None

    def extract_sub_metric_filter(self, source=None, entity=None):
        filter = self.get_filters(source=source)
        if filter:
            filter = collections.namedtuple("FilterStruct", filter.keys())(*filter.values())
            allowed_sources = []
            allowed_entityIds = []
            allowed_metrics = []

            if source:
                for i in filter.sub_metric_filter:
                    if i.entity_type == entity and i.source == source:
                        allowed_entityIds.extend(i.entityIds)
                        allowed_metrics.extend(i.metrics)
                allowed_sources.append(source)
            else:
                for i in filter.sub_metric_filter:
                    i = collections.namedtuple("SubMetricStruct", i.keys())(*i.values())
                    if i.entity_type == entity:
                        allowed_sources.append(i.source)
                        allowed_entityIds.extend(i.entityIds)
                        allowed_metrics.extend(i.metrics)

            return {"matched_filter": filter.matched_filter,
                    "unmatched_filter": filter.unmatched_filter,
                    "source": allowed_sources,
                    "entityIds": allowed_entityIds,
                    "metric": allowed_metrics}
        else:
            None

    def my_dict(self, obj=None):
        m_dict = dict()
        m_dict.update({
            "matched_filter": obj.matched_filter,
            "unmatched_filter": obj.unmatched_filter,
            "non_metric_filter": obj.non_metric_filter,
            "metric_filter": obj.metric_filter,
            "sub_metric_filter": obj.sub_metric_filter
        })
        return m_dict


if __name__ == "__main__":
    f_manager = FilterManager()
    pprint(f_manager.get_non_metric_filter_table())
    pprint(f_manager.get_metric_filter_table())
