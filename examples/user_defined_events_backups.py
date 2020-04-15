# Python SDK Examples
# Script will get all user defined eventss and dump to yaml file or create user defined events using data in given yaml file
# If event_backup_action = save : All the user defined events will be dump to yaml
# If event_backup_action = restore : User defined events are restored succesfully by reading yaml dump.


import init_api_client
import swagger_client
import utilities
import logging
import yaml
import json
import time
from swagger_client.rest import ApiException


logger = logging.getLogger("vrni_sdk")


def main(args):
    setting_api = swagger_client.SettingsApi()

    if args.event_backup_action == 'save':
        all_apps = []
        apps = setting_api.get_all_user_defined_events()
        for i in apps.results:
            event = setting_api.get_user_defined_event(i.entity_id)
            logger.info("Saving event {}".format(event))
            all_apps.append(event)
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors

        logger.info("Storing user defined events info to {}".format(args.event_backup_yaml))
        with open(args.event_backup_yaml, 'w') as outfile:
            yaml.dump(all_apps, outfile, default_flow_style=False)

    if args.event_backup_action == 'restore':
        with open(args.event_backup_yaml, 'r') as outfile:
            all_apps = yaml.load(outfile)
        snmp_list = []
        if args.update_snmp_destinations:
            logger.info("Getting SNMP trap destinations")
            snmp_details = setting_api.settings_snmp_profiles_get()
            snmp_list = [snmp.entity_id for snmp in snmp_details.results]
        time.sleep(0.025)  # make sure we don't hit the vRNI throttle and start getting 429 errors
        for app in all_apps:
            app._event_name =  app._event_name + '-restored'
            try:
                logger.info("Updating SNMP trap destinations")
                app.snmp_trap_entity_ids = snmp_list
                logger.info("Creating user defined event {}".format(app._event_name))
                created_application_defined_events= setting_api.settings_events_user_defined_events_post(app)
                logger.info("Created user defined events {}".format(created_application_defined_events))
                time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
            except ApiException as e:
                logger.error("{}".format(json.loads(e.body)))


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--event_backup_yaml", action="store",
                        default='events_backup.yml', help="User defined events are saved in this csv")
    parser.add_argument("--event_backup_action", action="store",
                        default='restore', help="Action can be 'save' or 'restore'")
    parser.add_argument("--update_snmp_destinations", action="store",
                        default=True, help="Update snmp in user defined events")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
