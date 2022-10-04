import os
import argparse


class DatabusOnSystemMongoCleanup:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="vRNI Source value (customer ID / service tag)")
    parser.add_argument("-d", "--dbName", help="Database name")
    parser.add_argument("-c", "--colName", help="Collection name")
    args = parser.parse_args()

    if args.dbName:
        db_name = args.dbName
    else:
        db_name = "databus_client_data"

    if args.colName:
        col_name = args.colName
    else:
        col_name = dict()

    collection_list = ['metrics_message_group', 'vms_metrics_message_group', 'hosts_metrics_message_group',
                       'flows_metrics_message_group', 'nics_metrics_message_group', 'switchports_metrics_message_group',
                       'hearbeats_all_message_groups', 'applications_message_group', 'hosts_message_group',
                       'vms_message_group', 'flows_message_group']

    os.system("mongo")
    os.system("use {}".format(db_name))

    if type(col_name) == dict:
        for message_group in collection_list:
            if args.source:
                os.system("db.{}.remove".format(message_group) + "({\"source\":" + "\"{}\"".format(args.source) + "})")
            else:
                os.system("db.{}.drop()".format(message_group))
    else:
        if args.source:
            os.system(
                "db.{}.remove".format(col_name) + "({\"source\":" + "\"{}\"".format(args.source) + "})")
        else:
            os.system("db.{}.drop()".format(col_name))

    os.system("exit")
