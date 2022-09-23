import enum


class DatabusConstants(object):
    def __init__(self, *args, **kwargs):
        raise AssertionError("Constant object can not be instantiated: %s" %
                             type(self))


class DatabusMongo(DatabusConstants):
    SOURCE = 'source'
    ENTITY_ID = 'entity_id'
    MESSAGE = 'message'
    METRIC_NAME = 'metric_name'
    METRIC_UNIT = 'metric_unit'
    METRIC_INTERVAL = 'metric_interval'
    METRIC_ENTITY_TYPE = 'metric_entity_type'
    METRIC_TIMESTAMP = 'metric_timestamp'
    METRIC_VALUE = 'metric_value'
    MESSAGE_GROUP = 'message_group'
    TIMESTAMP = 'timestamp'
    STATUS = 'status'
    TYPE = 'type'
    CLIENT_KEY = 'client_key'
    TOKEN = 'token'


class DatabusSSHConstants(DatabusConstants):
    DATABUS_ND_JUMPBOX_IP = '10.45.0.111'
    DATABUS_ND_JUMPBOX_USER = 'ubuntu'
    DATABUS_ND_JUMPBOX_PASSWORD = 'c0113ct0rs0ftwar3'
    DATABUS_SAAS_SSH_KEYFILE = 'vnera-infra-ec2.pem'


class DatabusMessageGroup(enum.Enum):
    APPLICATIONS = "applications"
    PROBLEMS = "problems"
    METRICS = "metrics"
    VMS_METRICS = "vms-metrics"
    HOSTS_METRICS = "hosts-metrics"
    FLOWS_METRICS = "flows-metrics"
    NICS_METRICS = "nics-metrics"
    SWITCHPORTS_METRICS = "switchports-metrics"
    FLOWS = "flows"
    VMS = "vms"
    HOSTS = "hosts"


DATABUS_MONGO_IP = "10.89.69.157:27017,10.89.69.154:27017,10.89.69.156:27017,10.89.69.153:27017,10.89.69.155:27017"