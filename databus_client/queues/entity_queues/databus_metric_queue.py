import queue
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.db_handler.mongoDB_handler.databus_metric_db_handler import DatabusMetricDbHandler
from databus_client.log_handler.log_queue import LogQueue
from databus_client.filters.metric_filter import MetricFilter
from databus_client.queues.entity_queues.databus_queue import DatabusQueue
from databus_client.db_handler.mongoDB_handler.databus_hb_dbhandler import DatabusHeartBeatDbHandler
from databus_client.utils.databus_utilities import DatabusUtilities


class DatabusMetricsQueue(DatabusQueue):

    def __init__(self, use_mongo=True, message_group=None, file_threshold=None):
        super(DatabusMetricsQueue, self).__init__(message_group=message_group,
                                                  num_of_worker_threads=2, use_mongo=use_mongo)
        self.logger = LogQueue(num_of_worker_threads=2, message_group=self.message_group, file_threshold=file_threshold)
        self.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception", file_threshold=file_threshold)
        self.license_plate = ""
        self.source_entity_id_lookup = dict()

    def start_processing_data(self):

        while True:
            self.license_plate = "[License Plate: " + DatabusUtilities.get_license_plate() + "] "
            entry = None
            try:
                entry = self.queue.get(block=False)
                message = dict()
                self.logger.log(self.license_plate + "Processing Request : " + str(entry))

                token = self.get_dict_val("token", entry)
                source = message["source"] = self.get_dict_val("source", entry)

                if source not in self.data_map:
                    self.data_map[source] = dict()
                    self.logger.log(self.license_plate + "\n---new source {} added".format(source))

                source_map = self.data_map[source]

                # as of now optiona to persist this
                self.append_key_val_in_dict(message, ["id", "type", "specversion", "message_group", "token"], entry)

                # if heart beat message
                if message["type"] == "HEARTBEAT":
                    self.append_key_val_in_dict(message, ["status", "timestamp"], entry)
                    self.logger.log(
                        self.license_plate + ". Message received is identified as heartbeat. Bypassing filters")
                    DatabusHeartBeatDbHandler.get_instance().add_to_queue(message)
                else:
                    """
                    Getting filtered pass
                    """
                    self.logger.log(self.license_plate + "Passing through filter.")
                    pass_through, entry = MetricFilter.pass_metric_filter(source=source, entry=entry, message_group=self.message_group)

                    if pass_through:
                        data = self.get_dict_val("data", entry)
                        self.logger.log(self.license_plate + "\n---data -- type {}---{}".format(type(data), data))

                        metric_unit = self.get_dict_val("unit", data)
                        metric_entity_type = self.get_dict_val("entity_type", data)
                        metric_interval = self.get_dict_val("interval", data)
                        metric_name = self.get_dict_val("metric", data)
                        metric_timestamp = self.get_dict_val("timestamp", data)
                        metric_points = self.get_dict_val("points", data)

                        self.logger.log(self.license_plate +
                                        "\n---metric_points -- type {}---{}".format(type(metric_points), metric_points))

                        self.count += len(metric_points)

                        for entity_point in metric_points:
                            entity_id = entity_point["entity_id"]
                            metric_value = entity_point["value"]

                            # prepare data for mongo
                            metric_data = dict()
                            if self.use_mongo:
                                metric_data.update({
                                    "source": source,
                                    "entity_id": entity_id,
                                    "metric_name": metric_name,
                                    "metric_unit": metric_unit,
                                    "metric_interval": metric_interval,
                                    "metric_entity_type": metric_entity_type,
                                    "metric_timestamp": metric_timestamp,
                                    "metric_value": metric_value,
                                    "token": token
                                })

                                DatabusMetricDbHandler.get_instance().add_to_queue(metric_data, self.message_group)
                                self.logger.log(self.license_plate +
                                                "added new entity_id and metric in mongo -> {} ".format(entity_id))
                            else:
                                if entity_id in source_map:
                                    if metric_name in source_map[entity_id]:
                                        source_map[entity_id][metric_name].update({
                                            metric_timestamp: metric_value,
                                        })
                                        self.logger.log(self.license_plate +
                                                        "added new timestamp on metric-> {} ".format(entity_id))
                                    else:
                                        source_map[entity_id].update({
                                            metric_name: {
                                                metric_timestamp: metric_value,
                                                "unit": metric_unit,
                                                "interval": metric_interval,
                                                "entity_type": metric_entity_type
                                            }
                                        })
                                        self.logger.log(
                                            self.license_plate + "added new metric -> {} ".format(entity_id))
                                else:
                                    source_map[entity_id] = {
                                        metric_name: {
                                            metric_timestamp: metric_value,
                                            "unit": metric_unit,
                                            "interval": metric_interval,
                                            "entity_type": metric_entity_type
                                        }
                                    }
                                    self.logger.log(
                                        self.license_plate + "added new entity_id and metric -> {} ".format(entity_id))
                    else:
                        self.logger.log(
                            self.license_plate + "Data was eliminated from the filter criteria. Was not pushed further downstream")
                self.queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occured process message in DatabusMetricsQueue. Trace : {}".format(
                    traceback.format_exc())
                self.exception_logger.log(self.license_plate + "Exception: " + message)

    def get_filtered_data(self, request_filter_dict=None):
        if self.use_mongo:
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]

                entity_id = request_filter_dict["entity_id"] if "entity_id" in request_filter_dict else None
                metric_name = request_filter_dict["metric_name"] if "metric_name" in request_filter_dict else None
                #  based on customer_id + entity_id
                result_dict = DatabusClientDataService.get_data_for_source_metric_message_group(source,
                                                                                                self.message_group,
                                                                                                entity_id=entity_id,
                                                                                                metric_name=metric_name)

                return result_dict

            else:
                message = "source attribute is must. Not provided for get call message_group {}.".format(
                    self.message_group)
                self.exception_logger.log(self.license_plate + "Exception: " + message)
                raise Exception(message)
        else:

            data_dict = dict()
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]
                source_map = self.data_map[source]
                if "entity_id" in request_filter_dict:
                    entity_id = request_filter_dict["entity_id"]
                    if entity_id in source_map:
                        data_dict = source_map[entity_id]
                        if "metric" in request_filter_dict:
                            metric = request_filter_dict["metric"]
                            if metric in data_dict:
                                data_dict = source_map[entity_id][metric]
                            else:
                                data_dict = dict()
                                print("NO DATA FOR ENTITY ID {} and METRIC {} ".format(entity_id, metric))
                        else:
                            data_dict = source_map[entity_id]
                    else:
                        data_dict = dict()
                        print("NO DATA FOR ENTITY ID {} ".format(entity_id))
                else:
                    data_dict = source_map
            else:
                data_dict = self.data_map

            return data_dict

    # Getting data as non-metric group to get raw data
    def get_non_filtered_data(self, request_filter_dict=None):
        print("Reached to get non filtered data")
        data_dict = dict()
        if self.use_mongo:

            if "source" in request_filter_dict:
                source = request_filter_dict["source"]

                entity_id = request_filter_dict["entity_id"] if "entity_id" in request_filter_dict else None

                #  based on customer_id + entity_id
                result_dict = DatabusClientDataService.get_raw_data_for_source_metric_message_group(source,
                                                                                                    self.message_group,
                                                                                                    entity_id=entity_id)
                return result_dict

            else:
                message = "source attribute is must. Not provided for get call message_group {}.".format(
                    self.message_group)
                self.exception_logger.log(self.license_plate + "Exception: " + message)
                raise Exception(message)

        else:
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]
                source_map = self.data_map[source]
                if "entity_id" in request_filter_dict:
                    entity_id = request_filter_dict["entity_id"]
                    if entity_id in source_map:
                        data_dict = source_map[entity_id]
                    else:
                        print("NO DATA FOR ENTITY ID {} ".format(entity_id))
                else:
                    data_dict = source_map
            else:
                data_dict = self.data_map

        return data_dict
