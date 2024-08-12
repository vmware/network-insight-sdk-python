import argparse
import calendar
import distutils.util
import json
import os
import threading
import time
import traceback
from datetime import datetime
from json.decoder import JSONDecodeError
import ssl
import socket

import pytz
from flask import Flask, Response
from flask import jsonify
from flask import request

from databus_client.db_handler.mongoDB_handler.connection import MongoDBConnection
from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.db_handler.mongoDB_handler.databus_metric_db_handler import DatabusMetricDbHandler
from databus_client.log_handler.databus_logger import DatabusLoggerHandler
from databus_client.log_handler.log_queue import LogQueue
from databus_client.filters.filter_manager import FilterManager
from databus_client.filters.queue_manager import DatabusQueueManager
from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.utils.common.databus_message_entity_count_recorder import DatabusMessageEntityCountRecorder
from databus_client.utils.common.databus_queue_telemetry import DatabusQueueTelemetry

"""
Flask endpoint class to create a server which can accept POST/GET/DELETE/COPY etc calls to corresponding endpoints.
This is created as a databus subscriber, where VRNI setup sends data (POST calls) and test-side code pulls data (GET calls).
This support various other functionalities which help in debugging. 

Feature set is as below:
1) Databus client endpoint for VRNI to POST data and test to GET data for a databus message-group
2) Telemetry
3) Simulating data (bring up server and POST/GET data from json files) for debugging
4) Fetch configuration 
5) Update  file dump frequency (applicable for in-memory data persistance mode only, i.e. use_mongo=False)
"""

app = Flask(__name__)
dbclient_queue_handler = None

enable_telemetry = False

TIME = calendar.timegm(time.gmtime())

timeZ_Kl = pytz.timezone('Asia/Kolkata')
dt_Kl = datetime.now(timeZ_Kl)
IST = dt_Kl.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/' + DatabusMessageGroup.APPLICATIONS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_application():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.APPLICATIONS.value)


@app.route('/' + DatabusMessageGroup.PROBLEMS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_alerts():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.PROBLEMS.value)


@app.route('/' + DatabusMessageGroup.METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.METRICS.value)


@app.route('/' + DatabusMessageGroup.VMS_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_vms_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.VMS_METRICS.value)


@app.route('/' + DatabusMessageGroup.HOSTS_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_hosts_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.HOSTS_METRICS.value)

@app.route('/' + DatabusMessageGroup.NSXT_EDGE_NODE_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_nsxt_edge_node_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.NSXT_EDGE_NODE_METRICS.value)

@app.route('/' + DatabusMessageGroup.FLOWS_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_flows_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.FLOWS_METRICS.value)


@app.route('/' + DatabusMessageGroup.NICS_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_nics_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.NICS_METRICS.value)


@app.route('/' + DatabusMessageGroup.SWITCHPORTS_METRICS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_switchports_metrics():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.SWITCHPORTS_METRICS.value)


@app.route('/' + DatabusMessageGroup.FLOWS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_flows():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.FLOWS.value)

@app.route('/' + DatabusMessageGroup.FLOWS.value + "-filter", methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_filtered_flows():
   return databus_queue_processor(request=request, message_group=DatabusMessageGroup.FLOWS.value, is_filtered=True)

@app.route('/' + DatabusMessageGroup.VMS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_vms():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.VMS.value)


@app.route('/' + DatabusMessageGroup.HOSTS.value, methods=['GET', 'POST', 'DELETE', 'COPY'])
def databus_hosts():
    return databus_queue_processor(request=request, message_group=DatabusMessageGroup.HOSTS.value)


@app.route('/heartbeat', methods=['GET'])
def databus_heartbeat():
    if request.method == 'GET':
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value

        if "source" in request_filter_dict:
            source = request_filter_dict["source"]
            message_group = request_filter_dict["message_group"] if "message_group" in request_filter_dict else None

            #  based on customer_id + entity_id
            result_dict = DatabusClientDataService.get_heartbeat_data(source,
                                                                      message_group=message_group)
            return Response(json.dumps(result_dict), content_type="json")

        else:
            message = "source attribute is must. Not provided."
            exception_logger.log(license_plate + "Exception: " + message)
            raise Exception(message)
    else:
        result = dbclient_queue_handler.file_handler.get_info()
        return Response(json.dumps(result), content_type="json")


@app.route('/telemetry', methods=['GET', 'POST'])
def databus_telemetry():
    if request.method == 'POST':
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value
        result = telemetry.update_telemetry_config(request_filter_dict)
        return Response(result, content_type="json")

    elif request.method == 'GET':
        result = telemetry.get_telemetry_dict(as_json=True)
        return Response(result, content_type="json")


@app.route('/filedumpfrequency', methods=['GET', 'POST'])
def databus_filedumpfrequency():
    if request.method == 'POST':
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value
        result = dbclient_queue_handler.file_handler.update_dump_frequency(request_filter_dict)
        return Response(json.dumps(result), content_type="json")

    elif request.method == 'GET':
        result = dbclient_queue_handler.file_handler.get_info()
        return Response(json.dumps(result), content_type="json")


@app.route("/filters", methods=["POST", "GET", "PUT", "DELETE"])
def filters():
    request_status = None
    try:
        if request.method == 'POST':
            filter_dict = dict()
            record = request.get_json()
            for key, value in record.items():
                filter_dict[key] = value
            FilterManager().set_filters(filter_dict=filter_dict)
            request_status = 200
            return Response("Filters successfully configured", request_status)

        elif request.method == 'GET':
            request_filter_dict = dict()
            for key, value in request.args.items():
                request_filter_dict[key] = value
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]
                result = FilterManager().get_filters(source=source)
            else:
                result = FilterManager().get_filters(source=None)
            if result is None:
                request_status = 204
                return Response("No Filters configured found", request_status)
            else:
                request_status = 200
                return Response(json.dumps(result), content_type=json)

        elif request.method == 'PUT':
            filter_dict = dict()
            record = request.get_json()
            for key, value in record.items():
                if value == "" or value == "NA":
                    filter_dict[key] = None
                else:
                    filter_dict[key] = value
            if "source" not in filter_dict:
                request_status = 500
                return Response("Source is required.", request_status)
            request_status = 200
            message = FilterManager().update_filters(update_dict=filter_dict)
            return Response(json.dumps(message), content_type=json)

        elif request.method == 'DELETE':
            request_filter_dict = dict()
            for key, value in request.args.items():
                request_filter_dict[key] = value
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]
            else:
                request_status = 500
                return Response("Source is required.", request_status)
            done = FilterManager().delete_filters(source=source)
            if done:
                return Response("Deleted source {} from filter".format(source))
            else:
                request_status = 204
                return Response("Source does not exist in source", request_status)
    except Exception as e:
        exception_logger.log(
            license_plate + "Exception occurred while fetching/sending filters - " + traceback.format_exc())
        DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)
    finally:
        info_dict = {"message_group": "filters"}
        if request_status is None:
            request_status = 200
        if enable_telemetry:
            if request.method == 'POST':
                telemetry.update_post_telemetry(status=request_status, info_data_dict=info_dict)
            if request.method == 'GET':
                telemetry.update_get_telemetry(status=request_status, info_data_dict=info_dict)
            if request.method == 'PUT':
                telemetry.update_put_telemetry(status=request_status, info_data_dict=info_dict)
            if request.method == 'DELETE':
                telemetry.update_delete_telemetry(status=request_status, info_data_dict=info_dict)


@app.route("/entity_filters", methods=["GET"])
def get_entity_filter():
    try:
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value
        source = str
        if "source" in request_filter_dict:
            source = request_filter_dict["source"]
        else:
            return Response("Source is required.", 500)

        result = None
        if "entity" in request_filter_dict:
            if request_filter_dict["entity"] == 'applications':
                result = FilterManager().get_application_filter(source=source)
            elif request_filter_dict["entity"] == 'vms':
                result = FilterManager().get_vms_filter(source=source)
            elif request_filter_dict["entity"] == 'hosts':
                result = FilterManager().get_hosts_filter(source=source)
            elif request_filter_dict["entity"] == 'flows':
                result = FilterManager().get_flows_filter(source=source)
            elif request_filter_dict["entity"] == 'nics':
                result = FilterManager().get_nics_filter(source=source)
            elif request_filter_dict["entity"] == 'problems':
                result = FilterManager().get_problems_filter(source=source)
            elif request_filter_dict["entity"] == 'metrics':
                result = FilterManager().get_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'vms-metrics':
                result = FilterManager().get_vms_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'hosts-metrics':
                result = FilterManager().get_hosts_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'flows-metrics':
                result = FilterManager().get_flows_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'nics-metrics':
                result = FilterManager().get_nics_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'switchports-metrics':
                result = FilterManager().get_switchport_metrics_filter(source=source)
            elif request_filter_dict["entity"] == 'nsxt-edge-node-metrics':
                result = FilterManager().get_nsxt_edge_node_metrics_filter(source=source)
        else:
            return Response("Entity is required.", 500)

        return Response(json.dumps(result), content_type="json")
    except Exception as e:
        message = "Exception occurred in entity_filters -" + format(traceback.format_exc())
        exception_logger.log(license_plate + message)
        DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)


@app.route("/token", methods=["GET"])
def get_bearer_token():
    request_filter_dict = dict()
    for key, value in request.get_json().items():
        request_filter_dict[key] = value
    token_key = str
    if "token_key" in request_filter_dict:
        token_key = request_filter_dict["token_key"]
    else:
        return Response("token_key is required.", 500)

    token = DatabusClientDataService.get_bearer_token(token_key);
    if token:
        return Response(json.dumps(token), content_type="json", status=200)
    else:
        return Response("No token found present for token_key: {}".format(token_key), status=204)


def databus_queue_processor(request=None, message_group=None, is_filtered=False):
    try:
        queue_processor = dbclient_queue_handler.get_qp(message_group)
        if request.method == 'POST':
            return do_post(queue_processor=queue_processor, message_group=message_group, is_filtered=is_filtered)
        elif request.method == 'GET':
            return do_get(queue_processor=queue_processor, message_group=message_group)
        elif request.method == 'DELETE':
            return do_delete(queue_processor=queue_processor, message_group=message_group)
        elif request.method == 'COPY':
            return do_copy(queue_processor=queue_processor, message_group=message_group)
    except Exception as e:
        exception_logger.log(license_plate + e)
        DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)
        raise Exception("EXCEPTION IN {} REQUEST".format(request.method))


def do_post(queue_processor=None, message_group=None, is_filtered=False):
    request_status = 200
    info_dict = {"message_group": message_group}
    try:
        data = request.json
        if type(data) is dict:
            data['is_filtered'] = is_filtered
        elif type(data) is list:
            for entry in data:
                if type(entry) is dict:
                    entry['is_filtered'] = is_filtered
                else:
                    pass
        """Adding token to list"""
        token = None
        if request.headers['Authorization']:
            token = str(request.headers['Authorization']).split("Bearer ")[1]
        if not token:
            print("No token obtained in header")
        else:
            if type(data) is dict:
                data['token'] = token
            else:
                """If data is list type"""
                for entry in data:
                    entry['token'] = token

        app.logger.info(data)
        json_resp = jsonify(success=True)

        queue_processor.add_to_queue(data)

        return json_resp

    except Exception as e:
        message = "Unexpected Exception during POST call. Trace ... \n\n{}".format(traceback.format_exc())
        exception_logger.log(license_plate + "Exception: " + message)
        request_status = 500
        return Response(message, request_status)
    finally:
        if enable_telemetry: telemetry.update_post_telemetry(status=request_status, info_data_dict=info_dict)


def do_get(queue_processor=None, message_group=None):
    request_status = 200
    info_dict = {"message_group": message_group}
    try:
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value

        if "get_raw" in request_filter_dict and request_filter_dict["get_raw"] == "True":
            print("Into condition for getting raw data")
            result_json = json.dumps(queue_processor.get_non_filtered_data(request_filter_dict))
        else:
            result_json = json.dumps(queue_processor.get_filtered_data(request_filter_dict))
        return Response(result_json, content_type="json")
    except JSONDecodeError as e:
        request_status = 400
        return Response("Invalid JSON", request_status)
    except Exception as e:
        message = "Unexpected Exception during GET call. Trace ... \n\n{}".format(traceback.format_exc())
        exception_logger.log(license_plate + "Exception: " + message)
        request_status = 500
        return Response("Internal Server Error. Contact Developer. Message: {}".format(message), request_status)
    finally:
        if enable_telemetry: telemetry.update_get_telemetry(status=request_status, info_data_dict=info_dict)


def do_delete(queue_processor=None, message_group=None):
    request_status = 200
    info_dict = {"message_group": message_group}
    try:
        request_filter_dict = dict()
        for key, value in request.args.items():
            request_filter_dict[key] = value
        queue_processor.reset_data_map(request_filter_dict)
        return Response("reset successfull for payload : {}".format(request_filter_dict), content_type="json")
    except Exception as e:
        message = "Unexpected Exception during DELETE call. Trace ... \n\n{}".format(traceback.format_exc())
        exception_logger.log(license_plate + "Exception: " + message)
        request_status = 500
        return Response("Internal Server Error. Contact Developer. Message: {}".format(message), request_status)
    finally:
        if enable_telemetry: telemetry.update_delete_telemetry(status=request_status, info_data_dict=info_dict)


def do_copy(queue_processor=None, message_group=None):
    request_status = 200
    info_dict = {"message_group": message_group}
    try:
        name_dict = queue_processor.save_to_file(data_dict=queue_processor.get_data_map(),
                                                 host_ip=args.host, host_port=args.port,
                                                 message_group=message_group)
        response = {
            "result": "success",
            "data": name_dict
        }
        return Response(json.dumps(response), content_type="json")
    except Exception as e:
        message = "Unexpected Exception during COPY call. Trace ... \n\n{}".format(traceback.format_exc())
        exception_logger.log(license_plate + "Exception: " + message)
        DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)
        request_status = 500
        return Response("Internal Server Error. Contact Developer. Message: {}".format(message), request_status)
    finally:
        if enable_telemetry: telemetry.update_copy_telemetry(status=request_status, info_data_dict=info_dict)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # this is some random ip address
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def parse_arguments():
    parser = argparse.ArgumentParser(description="HTTP server end point configuration for databus")
    parser.add_argument("--host", default="0.0.0.0", action="store", dest="host")
    parser.add_argument("--port", default="5001", action="store", dest="port")
    parser.add_argument("--enable_telemetry", default="True", action="store")
    parser.add_argument("--use_mongo", default="True", action="store")
    parser.add_argument("--mongo_server_ip", default="10.196.167.141:27017", action="store")
    parser.add_argument("--https", default="False", action="store")
    parser.add_argument("--cert_file_path", default="", action="store")
    parser.add_argument("--key_file_path", default="", action="store")
    parser.add_argument("--file_threshold", default=100, action="store")
    args_cmd = parser.parse_args()
    return args_cmd


def load_staging_ssl(cert_file_path=None, key_file_path=None):
    staging_context = ssl.SSLContext()
    staging_cert_path = os.path.abspath(cert_file_path)
    staging_key_path = os.path.abspath(key_file_path)

    staging_context.load_cert_chain(staging_cert_path, staging_key_path)
    return staging_context


def get_file_threshold():
    return file_threshold


if __name__ == "__main__":
    print("###################INITIALIZING DATABUS CLIENT#########################")
    args = parse_arguments()
    use_mongo = bool(distutils.util.strtobool(args.use_mongo))
    enable_telemetry = bool(distutils.util.strtobool(args.enable_telemetry))
    bringup_https = bool(distutils.util.strtobool(args.https))
    file_threshold = args.file_threshold
    mongo_server_ip = args.mongo_server_ip

    if mongo_server_ip == "":
        mongo_server_ip = get_ip_address() + ":27017"

    if not use_mongo:
        FilterManager().set_use_local(flag=True)
        print("******************Starting in NO Mongo mode*******************")
    else:
        print("*******************Connecting to MONGO************************")
        MongoDBConnection(server_url=mongo_server_ip,
                          database_name="databus_client_data",
                          alias='databus_client_data')
        FilterManager()

    print("********************Setting up processes**********************")
    DatabusLoggerHandler.create_file_structure()

    license_plate = "[License Plate: Endpoint] "

    dbclient_queue_handler = DatabusQueueManager(use_mongo=use_mongo, file_threshold=file_threshold)
    DatabusClientDataService.set_ex_logger()
    mdb_hand = DatabusMetricDbHandler()
    mdb_hand.set_ex_logger()
    exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception", file_threshold=file_threshold)

    telemetry = DatabusQueueTelemetry()

    t = threading.Thread(target=DatabusMessageEntityCountRecorder.get_instance().start_recording)
    t.start()

    if bringup_https:
        context = load_staging_ssl(cert_file_path=args.cert_file_path, key_file_path=args.key_file_path)
        app.run(ssl_context=context, host=args.host, port=args.port, debug=True)
    else:
        app.run(host=args.host, port=args.port, debug=False)
