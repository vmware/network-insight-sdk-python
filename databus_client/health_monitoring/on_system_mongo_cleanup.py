import os
import argparse


class DatabusOnSystemMongoCleanup:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="vRNI Source value (customer ID / service tag)")
    parser.add_argument("-c", "--msg_group", help="Message group name")
    args = parser.parse_args()

    db_name = "databus_client_data"

    collection = dict()
    collection.update({
        'metrics': 'metrics_message_group',
        'vms-metrics': 'vms_metrics_message_group',
        'hosts-metrics': 'hosts_metrics_message_group',
        'nsxt-edge-node-metrics': 'nsxt_edge_node_message_group',
        'flows-metrics': 'flows_metrics_message_group',
        'nics-metrics': 'nics_metrics_message_group',
        'switchport-metrics': 'switchports_metrics_message_group',
        'heartbeat': 'hearbeats_all_message_groups',
        'applications': 'applications_message_group',
        'hosts': 'hosts_message_group',
        'vms': 'vms_message_group',
        'flows': 'flows_message_group'
    })

    os.system("mongo")
    os.system("use {}".format(db_name))

    if type(args.msg_group) == list:
        for msg in args.msg_group:
            col_name = collection[msg]
            if args.source:
                os.system("db.{}.remove".format(col_name) + "({\"source\":" + "\"{}\"".format(args.source) + "})")
            else:
                os.system("db.{}.drop()".format(col_name))
    else:
        col_name = collection[args.msg_group]
        if args.source:
            os.system(
                "db.{}.remove".format(col_name) + "({\"source\":" + "\"{}\"".format(args.source) + "})")
        else:
            os.system("db.{}.drop()".format(col_name))

    os.system("exit")
