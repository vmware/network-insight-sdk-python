import swagger_client
from swagger_client.rest import ApiException

entity_map_to_fn = dict()
entity_map_to_fn[swagger_client.AllEntityType.CLUSTER] = "get_cluster"
entity_map_to_fn[swagger_client.AllEntityType.VCDATACENTER] = "get_datacenter"
entity_map_to_fn[swagger_client.AllEntityType.DATASTORE] = "get_datastore"
entity_map_to_fn[swagger_client.AllEntityType.DISTRIBUTEDVIRTUALPORTGROUP] = "get_distributed_virtual_portgroup"
entity_map_to_fn[swagger_client.AllEntityType.DISTRIBUTEDVIRTUALSWITCH] = "get_distributed_virtual_switch"
entity_map_to_fn[swagger_client.AllEntityType.NSXTFIREWALL] = "get_firewall"
entity_map_to_fn[swagger_client.AllEntityType.EC2FIREWALL] = "get_firewall"
entity_map_to_fn[swagger_client.AllEntityType.NSXDISTRIBUTEDFIREWALL] = "get_firewall"
entity_map_to_fn[swagger_client.AllEntityType.NSXFIREWALLRULE] = "get_firewall_rule"
entity_map_to_fn[swagger_client.AllEntityType.NSXTFIREWALLRULE] = "get_firewall_rule"
entity_map_to_fn[swagger_client.AllEntityType.EC2SGFIREWALLRULE] = "get_firewall_rule"
entity_map_to_fn[swagger_client.AllEntityType.FLOW] = "get_flow"
entity_map_to_fn[swagger_client.AllEntityType.FOLDER] = "get_folder"
entity_map_to_fn[swagger_client.AllEntityType.HOST] = "get_host"
entity_map_to_fn[swagger_client.AllEntityType.EC2IPSET] = "get_ip_set"
entity_map_to_fn[swagger_client.AllEntityType.NSXIPSET] = "get_ip_set"
entity_map_to_fn[swagger_client.AllEntityType.NSXTIPSET] = "get_ip_set"
entity_map_to_fn[swagger_client.AllEntityType.VXLANLAYER2NETWORK] = "get_layer2_network"
entity_map_to_fn[swagger_client.AllEntityType.NSXSECURITYGROUP] = "get_security_group"
entity_map_to_fn[swagger_client.AllEntityType.EC2SECURITYGROUP] = "get_security_group"
entity_map_to_fn[swagger_client.AllEntityType.SECURITYTAG] = "get_security_tag"
entity_map_to_fn[swagger_client.AllEntityType.NSSERVICE] = "get_service"
entity_map_to_fn[swagger_client.AllEntityType.NSXSERVICE] = "get_service"
entity_map_to_fn[swagger_client.AllEntityType.NSSERVICEGROUP] = "get_service_group"
entity_map_to_fn[swagger_client.AllEntityType.NSXSERVICEGROUP] = "get_service_group"
entity_map_to_fn[swagger_client.AllEntityType.VIRTUALMACHINE] = "get_vm"
entity_map_to_fn[swagger_client.AllEntityType.VMKNIC] = "get_vmknic"
entity_map_to_fn[swagger_client.AllEntityType.VNIC] = "get_vnic"

id_to_name_map = dict()


def get_fn_for_entity_type(entity_type, entities_api=None):
    if not entities_api:
        entities_api = swagger_client.EntitiesApi()
    if entity_type not in entity_map_to_fn:
        raise ValueError("Entity Type {} not found in entity map for get fn".format(entity_type))
    return getattr(entities_api, entity_map_to_fn[entity_type])


def get_entity(reference_entity):
    entity_fn = get_fn_for_entity_type(reference_entity.entity_type)
    try:
        e = entity_fn(id=reference_entity.entity_id)
    except ApiException:
        return None
    return e


def get_referenced_entity_name(referenced_entity):
    print("Fetching id = {} of type = {}".format(referenced_entity.entity_id, referenced_entity.entity_type))
    if referenced_entity.entity_id in id_to_name_map:
        return id_to_name_map[referenced_entity.entity_id]
    entity_name = None
    try:
        entity_name = get_entity(referenced_entity).name
    except AttributeError as e:
        # This means referenced entity might be deleted
        print(e)
    id_to_name_map[referenced_entity.entity_id] = entity_name
    return entity_name
