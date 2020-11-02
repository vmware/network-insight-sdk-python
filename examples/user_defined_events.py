# Python SDK Examples
# Script will create user defined events using data in given yaml file


import init_api_client
import swagger_client
import utilities
import logging
import yaml
import json
import time
import swagger_client.rest as exception
import swagger_client.models.subscription_response as subscription_response

logger = logging.getLogger("vrni_sdk")


def get_snmp_entity_id(setting_api, snmp_trap_destinations):
    logger.info("Getting SNMP trap snmp_trap_destinations")
    snmp_details = setting_api.settings_snmp_profiles_get()
    snmp_list = [snmp.entity_id for snmp in snmp_details.results if snmp.target_ip in snmp_trap_destinations]
    return snmp_list


def get_event_object(event, snmp_list):
    event_object = subscription_response.SubscriptionResponse(active=event['active'],
                                                              event_name=event['event_name'],
                                                              is_problem=event['is_problem'],
                                                              severity=event['severity'],
                                                              search_criteria=event['search_criteria'],
                                                              generate_event_criteria=event['generate_event_criteria'],
                                                              email_frequency=event['email_frequency'],
                                                              daily_at_utc="10:15",
                                                              email_ids=event['email_ids'],
                                                              snmp_trap_entity_ids=snmp_list)
    return event_object


def add_events(setting_api, all_events):
    for event in all_events:
        try:
            logger.info("Updating SNMP trap destinations")
            snmp_list = get_snmp_entity_id(setting_api, event['snmp_trap_destinations'])
            event_object = get_event_object(event, snmp_list)
            logger.info("Creating user defined event {}".format(event_object.event_name))
            created_user_defined_events = setting_api.create_user_defined_event(event_object)
            logger.info("Created user defined events {}".format(created_user_defined_events))
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
        except exception.ApiException as e:
            logger.error("{}".format(json.loads(e.body)))


def main(args):
    setting_api = swagger_client.SettingsApi()

    with open(args.events_yaml, 'r') as outfile:
        all_events = yaml.load(outfile)
        add_events(setting_api, all_events)


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--events_yaml", action="store",
                        default='events_backup.yml', help="Provide YAML with User defined events are saved in this csv")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
