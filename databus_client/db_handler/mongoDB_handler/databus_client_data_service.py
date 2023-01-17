import json
import traceback

from databus_client.db_handler.mongoDB_handler.connection import MongoDBConnection
from databus_client.db_handler.utils.mongodb_models import *
from databus_client.log_handler.log_queue import LogQueue
from databus_client.utils.common.databus_constants import DatabusMongo, DatabusMessageGroup
from databus_client.db_handler.utils.utilities import MandatoryParameterMissing
from databus_client.db_handler.utils import utilities

EPOCH_LAST_24_HRS = 24 * 60 * 60

MESSAGE_GRP_DB_SCHEMA = {
    DatabusMessageGroup.APPLICATIONS.value: DatabusClientApplicationsMessageGroupData,
    DatabusMessageGroup.PROBLEMS.value: DatabusClientProblemsMessageGroupData,
    DatabusMessageGroup.METRICS.value: DatabusClientMetricsMessageGroupData,
    DatabusMessageGroup.FLOWS.value: DatabusClientFlowsMessageGroupData,
    DatabusMessageGroup.VMS.value: DatabusClientVmsMessageGroupData,
    DatabusMessageGroup.HOSTS.value: DatabusClientHostsMessageGroupData,
    DatabusMessageGroup.VMS_METRICS.value: DatabusClientVmsMetricsMessageGroupData,
    DatabusMessageGroup.HOSTS_METRICS.value: DatabusClientHostsMetricsMessageGroupData,
    DatabusMessageGroup.FLOWS_METRICS.value: DatabusClientFlowsMetricsMessageGroupData,
    DatabusMessageGroup.NICS_METRICS.value: DatabusClientNicsMetricsMessageGroupData,
    DatabusMessageGroup.SWITCHPORTS_METRICS.value: DatabusClientSwitchPortsMetricsMessageGroupData
}

NON_METRIC_MSG_GRPS = [
    DatabusMessageGroup.APPLICATIONS.value,
    DatabusMessageGroup.PROBLEMS.value,
    DatabusMessageGroup.FLOWS.value,
    DatabusMessageGroup.VMS.value,
    DatabusMessageGroup.HOSTS.value
]

METRIC_MSG_GRPS = [
    DatabusMessageGroup.METRICS.value,
    DatabusMessageGroup.VMS_METRICS.value,
    DatabusMessageGroup.HOSTS_METRICS.value,
    DatabusMessageGroup.FLOWS_METRICS.value,
    DatabusMessageGroup.NICS_METRICS.value,
    DatabusMessageGroup.SWITCHPORTS_METRICS.value
]


class DatabusClientDataService(object):
    exception_logger = None
    license_plate = "[License Plate: DB service] "

    @classmethod
    def set_ex_logger(cls):
        if cls.exception_logger:
            pass
        else:
            cls.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception")
    """
    To support DB operations for MongoDB add/delete/get mongo db documents
    """

    @classmethod
    def get_data_for_source_nonmetric_message_group(cls, source, message_group,
                                                    entity_id=None):
        params = cls.get_query_params(source, message_group)

        ret_result = None
        if message_group in NON_METRIC_MSG_GRPS:
            data = MESSAGE_GRP_DB_SCHEMA[message_group].objects(**params)
        else:
            message = "INCORRECT MESSAGE GROUP {} PASSED FOR get_data_for_source_nonmetric_message_group()".format(
                message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        # Process data if not None
        if data is not None:
            ret_result = cls.process_nonmetric_data(data, source)

            # Filter based on entity_id in not None
            if entity_id is not None:
                ret_result = ret_result[source][entity_id]
            else:
                ret_result = ret_result[source]

        else:
            message = "None (data) QuerySet while getting result for {}".format(message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        return ret_result

    @classmethod
    def get_data_for_source_metric_message_group(cls, source, message_group,
                                                 entity_id=None, metric_name=None):

        params = cls.get_query_params(source, message_group)

        if message_group in METRIC_MSG_GRPS:
            data = MESSAGE_GRP_DB_SCHEMA[message_group].objects(**params)
        else:
            message = "INCORRECT MESSAGE GROUP {} PASSED FOR get_data_for_source_metric_message_group()".format(
                message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        # Process data if not None
        if data is not None:
            ret_result = cls.process_metric_data(data, source)

            if entity_id is not None:
                ret_result = ret_result[source][entity_id]
                if metric_name is not None:
                    ret_result = ret_result[metric_name]
            else:
                ret_result = ret_result[source]
        else:
            message = "None (data) QuerySet while getting result for {}".format(message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        return ret_result

    """Processing metric data as non metric to get the packets based on entity id"""

    @classmethod
    def get_raw_data_for_source_metric_message_group(cls, source, message_group,
                                                     entity_id=None):
        params = cls.get_query_params(source, message_group)

        ret_result = None
        if message_group in METRIC_MSG_GRPS:
            data = MESSAGE_GRP_DB_SCHEMA[message_group].objects(**params)
        else:
            message = "INCORRECT MESSAGE GROUP {} PASSED FOR get_raw_data_for_source_metric_message_group()".format(
                message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        # Process data if not None
        if data is not None:
            ret_result = cls.process_raw_metric_data(data, source)

            # Filter based on entity_id in not None
            if entity_id is not None:
                ret_result = ret_result[source][entity_id]
            else:
                ret_result = ret_result[source]

        else:
            message = "None (data) QuerySet while getting result for {}".format(message_group)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)
            return None

        return ret_result

    @classmethod
    def process_nonmetric_data(cls, data, source):
        ret_result = {
            source: dict()
        }
        for x in data:
            entry_data = json.loads(json.dumps(x, cls=utilities.MongoEncoder))
            ret_result[source].update({entry_data[DatabusMongo.ENTITY_ID]: entry_data["message"]})

        return ret_result

    @classmethod
    def process_raw_metric_data(cls, data, source):
        ret_result = {
            source: dict()
        }
        for x in data:
            entry_data = json.loads(json.dumps(x, cls=utilities.MongoEncoder))
            ret_result[source].update({entry_data[DatabusMongo.ENTITY_ID]: entry_data})

        return ret_result

    @classmethod
    def process_metric_data(cls, data, source):
        ret_result = {
            source: dict()
        }
        source_map = ret_result[source]
        for entry in data:
            entity_id = entry["entity_id"]
            metric_name = entry["metric_name"]
            metric_unit = entry["metric_unit"]
            metric_interval = entry["metric_interval"]
            metric_entity_type = entry["metric_entity_type"]
            metric_timestamp = entry["metric_timestamp"]
            metric_value = entry["metric_value"]

            if entity_id in source_map:
                if metric_name in source_map[entity_id]:
                    source_map[entity_id][metric_name].update({
                        metric_timestamp: metric_value,
                    })
                else:
                    source_map[entity_id].update({
                        metric_name: {
                            metric_timestamp: metric_value,
                            "unit": metric_unit,
                            "interval": metric_interval,
                            "entity_type": metric_entity_type
                        }
                    })
            else:
                source_map[entity_id] = {
                    metric_name: {
                        metric_timestamp: metric_value,
                        "unit": metric_unit,
                        "interval": metric_interval,
                        "entity_type": metric_entity_type
                    }
                }

        return ret_result

    @classmethod
    def delete_data_for_source_message_group(cls, source, message_group,
                                             entity_id=None):

        params = cls.get_query_params(source, message_group, entity_id=entity_id)

        result = MESSAGE_GRP_DB_SCHEMA[message_group].objects(**params).delete()

        return True

    @classmethod
    def delete_heartbeat_data(cls, source, message_group, entity_id=None):

        params = cls.get_query_params(source, message_group, entity_id=entity_id)

        result = DatabusClientHeartBeatData.objects(**params).delete()

        return True

    @classmethod
    def get_heartbeat_data(cls, source, message_group=None):
        if not source:
            raise MandatoryParameterMissing('source parameter missing', status_code=400)
        params = dict(source=source)

        data = DatabusClientHeartBeatData.objects(**params)

        ret_result = None
        if data is not None:
            ret_result = cls.process_hearbeat_data(data, source)
            ret_result = ret_result[source]

            if message_group is not None:
                m_grp_result = dict()
                for k, v in ret_result.items():
                    if v["message_group"] == message_group:
                        m_grp_result[k] = v
                return m_grp_result

        else:
            message = "None (data) QuerySet while getting result for Heartbeat for source {}".format(source)
            cls.exception_logger.log(cls.license_plate + "Exception: " + message)

        print(ret_result)

        return ret_result

    @classmethod
    def process_hearbeat_data(cls, data, source):
        ret_result = {
            source: dict()
        }
        count = 0
        for x in data:
            entry_data = json.loads(json.dumps(x, cls=utilities.MongoEncoder))
            ret_result[source].update({count: entry_data})
            count += 1

        return ret_result

    """
    MESSAGE GROUP METHODS
    """

    @classmethod
    def put_new_nonmetric_entity_message_group_data(cls, data, message_group):

        if message_group in NON_METRIC_MSG_GRPS:
            db_entry_new_non_metric = MESSAGE_GRP_DB_SCHEMA[message_group](source=data[DatabusMongo.SOURCE],
                                                                           entity_id=data[DatabusMongo.ENTITY_ID],
                                                                           message=data[DatabusMongo.MESSAGE],
                                                                           token=data[DatabusMongo.TOKEN])
            try:
                db_entry_new_non_metric.save()
            except Exception as e:
                cls.exception_logger.log(cls.license_plate + "Exception: Error pushing message to mongo")
                return False, "Exception: Error pushing message to mongo"

        else:
            message = "Incorrect message group passed put_new_nonmetric_entity_message_group_data :  {}".format(
                message_group)
            return False, message
        return True, None

    @classmethod
    def update_nonmetric_entity_message_group_data(cls, data, message_group):
        params = {
            "source": data[DatabusMongo.SOURCE],
            "entity_id": data[DatabusMongo.ENTITY_ID],
            "token": data[DatabusMongo.TOKEN]
        }

        if message_group in NON_METRIC_MSG_GRPS:
            db_entry_update_non_metric = MESSAGE_GRP_DB_SCHEMA[message_group].objects(**params)
            try:
                db_entry_update_non_metric.update_one(message=data["message"])
            except Exception as e:
                cls.exception_logger.log(cls.license_plate + "Exception: Error pushing message to mongo")
                return False, "Exception: Error pushing message to mongo"
        else:
            message = "Incorrect message group passed put_new_nonmetric_entity_message_group_data :  {}".format(
                message_group)
            return False, message

        return True, None

    """
    METRICS MESSAGE GROUP METHODS
    """

    @classmethod
    def put_new_metric_data_point(cls, data):
        db_entry = DatabusClientMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                        entity_id=data[DatabusMongo.ENTITY_ID],
                                                        metric_name=data[DatabusMongo.METRIC_NAME],
                                                        metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                        metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                        metric_entity_type=data[DatabusMongo.METRIC_ENTITY_TYPE],
                                                        metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                        metric_value=data[DatabusMongo.METRIC_VALUE],
                                                        token=data[DatabusMongo.TOKEN]
                                                        )
        db_entry.save()
        return

    @classmethod
    def put_new_vms_metric_data_point(cls, data):
        db_entry = DatabusClientVmsMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                           entity_id=data[DatabusMongo.ENTITY_ID],
                                                           metric_name=data[DatabusMongo.METRIC_NAME],
                                                           metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                           metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                           metric_entity_type=data[DatabusMongo.METRIC_ENTITY_TYPE],
                                                           metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                           metric_value=data[DatabusMongo.METRIC_VALUE],
                                                           token=data[DatabusMongo.TOKEN]
                                                           )
        db_entry.save()

        return

    @classmethod
    def put_new_hosts_metric_data_point(cls, data):
        db_entry = DatabusClientHostsMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                             entity_id=data[DatabusMongo.ENTITY_ID],
                                                             metric_name=data[DatabusMongo.METRIC_NAME],
                                                             metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                             metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                             metric_entity_type=data[DatabusMongo.METRIC_ENTITY_TYPE],
                                                             metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                             metric_value=data[DatabusMongo.METRIC_VALUE],
                                                             token=data[DatabusMongo.TOKEN]
                                                             )
        db_entry.save()
        return

    @classmethod
    def put_new_flows_metric_data_point(cls, data):
        db_entry = DatabusClientFlowsMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                             entity_id=data[DatabusMongo.ENTITY_ID],
                                                             metric_name=data[DatabusMongo.METRIC_NAME],
                                                             metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                             metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                             metric_entity_type=data[DatabusMongo.METRIC_ENTITY_TYPE],
                                                             metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                             metric_value=data[DatabusMongo.METRIC_VALUE],
                                                             token=data[DatabusMongo.TOKEN]
                                                             )
        db_entry.save()
        return

    @classmethod
    def put_new_nics_metric_data_point(cls, data):
        db_entry = DatabusClientNicsMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                            entity_id=data[DatabusMongo.ENTITY_ID],
                                                            metric_name=data[DatabusMongo.METRIC_NAME],
                                                            metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                            metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                            metric_entity_type=data[DatabusMongo.METRIC_ENTITY_TYPE],
                                                            metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                            metric_value=data[DatabusMongo.METRIC_VALUE],
                                                            token=data[DatabusMongo.TOKEN]
                                                            )
        db_entry.save()
        return

    @classmethod
    def put_new_switchports_metric_data_point(cls, data):
        db_entry = DatabusClientSwitchPortsMetricsMessageGroupData(source=data[DatabusMongo.SOURCE],
                                                                   entity_id=data[DatabusMongo.ENTITY_ID],
                                                                   metric_name=data[DatabusMongo.METRIC_NAME],
                                                                   metric_unit=data[DatabusMongo.METRIC_UNIT],
                                                                   metric_interval=data[DatabusMongo.METRIC_INTERVAL],
                                                                   metric_entity_type=data[
                                                                       DatabusMongo.METRIC_ENTITY_TYPE],
                                                                   metric_timestamp=data[DatabusMongo.METRIC_TIMESTAMP],
                                                                   metric_value=data[DatabusMongo.METRIC_VALUE],
                                                                   token=data[DatabusMongo.TOKEN]
                                                                   )

        db_entry.save()
        return

    @classmethod
    def put_new_heartbeat_data_point(cls, data):
        db_entry = DatabusClientHeartBeatData(source=data[DatabusMongo.SOURCE],
                                              message_group=data[DatabusMongo.MESSAGE_GROUP],
                                              timestamp=data[DatabusMongo.TIMESTAMP],
                                              status=data[DatabusMongo.STATUS],
                                              type=data[DatabusMongo.TYPE],
                                              token=data[DatabusMongo.TOKEN]
                                              )

        db_entry.save()
        return

    @classmethod
    def put_filters(cls, data):
        if data:
            db_entry = DatabusClientFilterData(matched_filter=data[DatabusMongo.MATCHED_FILTER],
                                               unmatched_filter=data[DatabusMongo.UNMATCHED_FILTER],
                                               non_metric_filter=data[DatabusMongo.NON_METRIC_FILTER] if DatabusMongo.NON_METRIC_FILTER in data else [],
                                               metric_filter=data[DatabusMongo.METRIC_FILTER] if DatabusMongo.METRIC_FILTER in data else [],
                                               sub_metric_filter=data[DatabusMongo.SUB_METRIC_FILTER] if DatabusMongo.SUB_METRIC_FILTER in data else []
                                               )
            try:
                exist_fil = DatabusClientFilterData.objects(None)
                processed_data = cls.process_filter_data(exist_fil)
                if processed_data:
                    exist_fil.delete()
                db_entry.save()
            except Exception as e:
                cls.exception_logger.log(cls.license_plate + "Exception: Error pushing filter to mongo. {}".format(traceback.format_exc()))
        else:
            DatabusClientFilterData.drop_collection()
        return

    @classmethod
    def get_filters(cls):
        data = DatabusClientFilterData.objects(None)
        f_dict = cls.process_filter_data(data=data)
        return f_dict

    @classmethod
    def process_filter_data(cls, data=None):
        f = dict()
        if data:
            for x in data:
                if type(x) == DatabusClientFilterData:
                    f['matched_filter'] = x.matched_filter
                    f['unmatched_filter'] = x.unmatched_filter
                    f['non_metric_filter'] = x.non_metric_filter
                    f['metric_filter'] = x.metric_filter
                    f['sub_metric_filter'] = x.sub_metric_filter
            return f
        else:
            return None

    @classmethod
    def get_query_params(cls, source, message_group, entity_id=None):
        if not source:
            raise MandatoryParameterMissing('source parameter missing', status_code=400)
        if not message_group:
            raise MandatoryParameterMissing('source parameter missing', status_code=400)
        params = dict(source=source)

        # update optionals params
        if entity_id is not None:
            params.update({"entity_id": entity_id})

        return params


if __name__ == '__main__':
    dbc = MongoDBConnection(alias='databus_client_data')
    print("")
