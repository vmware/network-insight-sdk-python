# Python SDK for vRNI - Examples
## examples/a_application_creation.py
### Bulk import applications from CSV
Imports applications that are defined in a file called cmdb_ci_hardware.csv.
## examples/add_generic_switch_router.py
### Upload configs of generic router/switch
This script uses an input ZIP file to add generic router/switch. To add generic router/switch data source for currently unsupported switch/router. Run this script with the param --zip_file_path (path for ZIP file created using network-insight-sdk-generic-datasources) proxy_ip and ip or fqdn of physical device.
## examples/application_backups.py
### Application Backup and Restore
Script will get all applications and dump to yaml file or create application using data in given yaml file If application_backup_action = save : All the applications will be dump to yaml If application_backup_action = restore : Applications and Tiers which are created only using Public API restored succesfully. e.g Tier with filter criteria for Virtual machine is given as security_groups.name='security_group_scale_100' will be restore correctly since it is done through public APIs while manually created Tier with filter criteria for virtual machine as security groups='security_group_scale_100' cannot be configured through public APIs.
## examples/application_creation.py
### Create single application
Script will create one application and three tiers in it Delete application snippet also included
## examples/billing_use_case.py
### Billing Use Case
Script will get total bytes transferred for a specific IP or group of IPs or the scope can be any l2 network, security group, etc.
## examples/bulk_fetch_exporter.py
### Export Flows
Script will fetch Flows matching certain search criteria It will take this fetch flows result and bulk fetch to get all flows information Along with the flow information it will fetch appropriate VM, Security group information and dump it to CSV file
## examples/datasource_addition.py
### Adding datasources in bulk
This script uses an input CSV (example: data_sources.csv) To add multiple vRealize Network Insight Data Sources. Modify data_sources.csv to contain your own data sources (vCenters, NSX, switches, firewalls) and run this script with the param --data_sources_csv to your CSV.
## examples/delete_datasource.py
### Delete datasources in bulk
This script uses an input CSV (example: data_sources.csv.csv) To Delete multiple vRealize Network Insight Data Sources. Modify data_sources.csv.csv to contain your own data sources (vCenters, NSX, switches, firewalls) and run this script with the param --data_sources_csv to your CSV.
## examples/flows_exporter_g.py
### Export Flows into CSV
Script will fetch Flows matching certain search criteria It will take this fetch flows result and bulk fetch to get all flows information Along with the flow information it will fetch appropriate VM, Security group information and dump it to CSV file
## examples/flows_to_vrli.py
### Export Flows into vRealize Log Insight
Script will fetch Flows matching certain search criteria Along with the flow information it will fetch the correlated VMs and send it to vRealize Log Insight via its API # Usage: python flows_to_vrli.py --platform_ip your-vrni-platform --username admin@local --password 'test' --vrli_server your-vrli-server
## examples/get_all_datasources.py
### Getting added datasources in bulk
This script write the added datasource in an input CSV (example: list_data_sources.csv) To list added vRealize Network Insight Data Sources, run this script with the param --data_sources_csv with new csv file name.
## examples/ip_tagging.py
### Add IP addresses/subnets to EAST_WEST or INTERNET settings
This script uses an input CSV (example: ip_tags.csv) To add or remove IP addresses to EAST-WEST or INTERNET Tags vRealize Network Insight Data Sources. Modify ip_tags ip_tags.csv to contain your own data sources The script also retrieves EAST-WEST and INTERNET IPs configured in vRNI and export as CSV
## examples/search_vms.py
### Search for VMs
Script will fetch VMs through a call to search API. Search API returns uuids for all VMs. Script will then fetch every single VM's complete information.
## examples/update_datasource.py
### Update datasources in bulk
This script uses an input CSV (example: update_data_sources.csv) To update multiple vRealize Network Insight Data Sources. Modify update_data_sources.csv to contain your own data sources (vCenters, NSX, switches, firewalls) and run this script with the param --data_sources_csv to your CSV.
## examples/update_datasource_retry.py
### Update datasources in bulk (with retries)
This script uses an input CSV (example: update_data_sources.csv) To update multiple vRealize Network Insight Data Sources. Modify update_data_sources.csv to contain your own data sources (vCenters, NSX, switches, firewalls) and run this script with the param --data_sources_csv to your CSV.
## examples/user_defined_events.py
### Create User-defined Events from YAML
Script will create user defined events using data in given yaml file
## examples/user_defined_events_backups.py
### User-defined Events Backup and Restore
Script will get all user defined events and dump to yaml file or create user defined events using data in given yaml file If event_backup_action = save : All the user defined events will be dump to yaml If event_backup_action = restore : User defined events are restored succesfully by reading given yaml file.
