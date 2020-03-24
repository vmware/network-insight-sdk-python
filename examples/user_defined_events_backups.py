# Python SDK Examples
# Script will get all applications and dump to yaml file or create application using data in given yaml file
# If application_backup_action = save : All the applications will be dump to yaml
# If application_backup_action = restore : Applications and Tiers which are created only using Public API restored succesfully.
# e.g Tier with filter criteria for Virtual machine is given as security_groups.name='security_group_scale_100' will be restore correctly since it is done through public APIs
# while manually created Tier with filter criteria for virtual machine as security groups='security_group_scale_100' cannot be configured through public APIs.

import init_api_client
import argparse
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
        apps = setting_api.settings_events_user_defined_events_get()
        for i in apps.results:
            event = setting_api.settings_events_user_defined_events_id_get(i.entity_id)
            logger.info("Saving event {}".format(event))
            all_apps.append(event)
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors

        logger.info("Storing user defined events info to {}".format(args.event_backup_yaml))
        with open(args.event_backup_yaml, 'w') as outfile:
            yaml.dump(all_apps, outfile, default_flow_style=False)

    if args.event_backup_action == 'restore':
        with open(args.event_backup_yaml, 'r') as outfile:
            all_apps = yaml.load(outfile)
        for app in all_apps:
            app._event_name =  app._event_name + '-restored'
            try:
                logger.info("Creating user defined event {}".format(app._event_name))
                created_application_defined_events= setting_api.settings_events_user_defined_events_post(app)
                time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
            except ApiException as e:
                logger.error("{}".format(json.loads(e.body)))


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--event_backup_yaml", action="store",
                        default='events_backup.yml', help="User defined events are saved in this csv")
    parser.add_argument("--event_backup_action", action="store",
                        default='restore', help="Action can be 'save' or 'restore'")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
