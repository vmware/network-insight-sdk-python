import mongoengine

"""
Mondo DB schema/models
"""

"""
Here:
1. source is service_tag - complete operation of data feed and retrival is based in source
2. entity_id ID - model key of entity
3. message is the message received from vRNI
4. token - this is the authentication bearer token received from vRNI which can be used to determine the sender is vRNI
"""


class DatabusClientApplicationsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    message = mongoengine.DictField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'applications_message_group',
        'indexes': [
            'source',
            'entity_id',
            'token'
        ]
    }


class DatabusClientProblemsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    message = mongoengine.DictField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'problems_message_group',
        'indexes': [
            'source',
            'entity_id',
            'token'
        ]
    }


class DatabusClientHostsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    message = mongoengine.DictField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'hosts_message_group',
        'indexes': [
            'source',
            'entity_id',
            'token'
        ]
    }


class DatabusClientVmsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    message = mongoengine.DictField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'vms_message_group',
        'indexes': [
            'source',
            'entity_id',
            'token'
        ]
    }


class DatabusClientFlowsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    message = mongoengine.DictField()
    token = mongoengine.StringField()
    is_filtered = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'flows_message_group',
        'indexes': [
            'source',
            'entity_id',
            'token',
            'is_filtered'
        ]
    }


class DatabusClientMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientVmsMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField()  # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'vms_metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientHostsMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField()  # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'hosts_metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientFlowsMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField()  # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'flows_metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientNicsMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField()  # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'nics_metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientSwitchPortsMetricsMessageGroupData(mongoengine.Document):
    source = mongoengine.StringField()  # setup platform customer_id
    entity_id = mongoengine.StringField()
    metric_name = mongoengine.StringField()
    metric_unit = mongoengine.StringField()
    metric_interval = mongoengine.IntField()
    metric_entity_type = mongoengine.StringField()
    metric_timestamp = mongoengine.IntField()
    metric_value = mongoengine.FloatField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'switchports_metrics_message_group',
        'indexes': [
            'source',
            'entity_id',
            'metric_name',
            'token'
        ]
    }


class DatabusClientHeartBeatData(mongoengine.Document):
    source = mongoengine.StringField() # setup platform customer_id
    message_group = mongoengine.StringField()
    status = mongoengine.StringField()
    type = mongoengine.StringField()
    timestamp = mongoengine.IntField()
    token = mongoengine.StringField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'hearbeats_all_message_groups',
        'indexes': [
            'source',
            'message_group',
            'token'
        ]
    }


class DatabusClientFilterData(mongoengine.Document):
    matched_filter = mongoengine.StringField()
    unmatched_filter = mongoengine.StringField()
    non_metric_filter = mongoengine.ListField()
    metric_filter = mongoengine.ListField()
    sub_metric_filter = mongoengine.ListField()
    meta = {
        'db_alias': 'databus_client_data',
        'collection': 'filter_configuration',
    }
