import queue
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.log_handler.log_queue import LogQueue
from databus_client.filters.non_metric_filter import NonMetricFilter
from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.queues.entity_queues.databus_queue import DatabusQueue
from databus_client.db_handler.mongoDB_handler.databus_hb_dbhandler import DatabusHeartBeatDbHandler
from databus_client.utils.common.databus_queue_telemetry import DatabusQueueTelemetry
from databus_client.utils.databus_utilities import DatabusUtilities


class DatabusFlowsQueue(DatabusQueue):

    def __init__(self, use_mongo=True, message_group=None, file_threshold=None):
        super(DatabusFlowsQueue, self).__init__(message_group=DatabusMessageGroup.FLOWS.value, num_of_worker_threads=2,
                                                use_mongo=use_mongo)
        self.logger = LogQueue(num_of_worker_threads=2, message_group=DatabusMessageGroup.FLOWS.value, file_threshold=file_threshold)
        self.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception", file_threshold=file_threshold)

    def start_processing_data(self):

        while True:
            license_plate = DatabusUtilities.get_license_plate()
            entry = None
            try:
                entry = self.queue.get(block=False)
                token = self.get_dict_val("token", entry)
                _source = self.get_dict_val("source", entry)
                license_plate = "[License Plate: " + license_plate + "] "
                self.logger.log(license_plate + "Processing Request : " + str(entry))

                if _source not in self.data_map:
                    self.data_map[_source] = dict()
                    self.logger.log(license_plate + "---new source {} added".format(_source))

                source_map = self.data_map[_source]

                message_type = self.get_dict_val("type", entry)

                # if heart beat message
                if message_type == "HEARTBEAT":
                    heart_beat = dict()
                    try:
                        self.append_key_val_in_dict(heart_beat,
                                                ["id", "type", "specversion", "source", "message_group", "status",
                                                 "timestamp", "token"], entry)
                    except KeyError as e:
                        print(f"Heartbeat Error: {e} not found in dictionary.")
                    except Exception as e:
                        print(f"An unexpected heartbeat error occurred: {e}")
                    else:
                        pass
                    self.logger.log(
                        license_plate + ". Message received is identified as heartbeat. Bypassing filters")
                    DatabusHeartBeatDbHandler.get_instance(logger=self.logger,
                                                           ex_log=self.exception_logger).add_to_queue(heart_beat)
                else:
                    is_filtered = self.get_dict_val("is_filtered", entry)
                    flow_data = self.get_dict_val("data", entry)

                    self.count += len(flow_data)

                    for flow in flow_data:
                        try:
                            message = dict()
                            self.append_key_val_in_dict(message,
                                                    ["id", "type", "specversion", "source", "message_group", "token", "is_filtered"],
                                                    entry)

                            entity_id = flow["entity_id"]
                            message["data"] = flow

                            db_entry = dict()
                            db_entry.update({
                                "source": _source,
                                "entity_id": entity_id,
                                "message": message,
                                "token": token,
                                "is_filtered": is_filtered})
                        except KeyError as e:
                            print(f"Error: {e} not found in dictionary.")
                        except Exception as e:
                            print(f"An unexpected error occurred: {e}")
                        else:
                            pass

                        """
                        Getting filtered pass
                        """
                        self.logger.log(license_plate + "Passing through filter.")
                        pass_through = NonMetricFilter.pass_non_metric_filter(source=_source,
                                                                              entity_id=entity_id,
                                                                              entity_name=message["data"][
                                                                                  "name"] if "name" in message[
                                                                                  "data"] else None)

                        if type(pass_through) == str:
                            self.logger.log(license_plate + pass_through)
                            pass_through = True

                        if pass_through:
                            DatabusQueueTelemetry().update_filter_telemetry(call_type="ALLOWED_BY_FILTER",
                                                                            message_group=self.message_group)
                            if entity_id in source_map:
                                if self.use_mongo:
                                    push_db = DatabusClientDataService.update_nonmetric_entity_message_group_data(
                                        db_entry,
                                        message_group=self.message_group)
                                    if push_db[0]:
                                        self.logger.log(
                                            license_plate + "updated new flow in mongo -> {} ".format(entity_id))
                                    else:
                                        self.logger.log(
                                            license_plate + "Error while pushing data to downstream: " + push_db[1])
                                else:
                                    source_map.update({entity_id: message})
                                    self.logger.log(license_plate + "updated flow -> {} ".format(entity_id))
                            else:
                                # add new
                                if self.use_mongo:
                                    push_db = DatabusClientDataService.put_new_nonmetric_entity_message_group_data(
                                        db_entry,
                                        self.message_group)
                                    source_map[entity_id] = dict()  # for look up only, hence not saving the message
                                    if push_db[0]:
                                        self.logger.log(
                                            license_plate + "added new flows in mongo -> {} ".format(entity_id))
                                    else:
                                        self.logger.log(
                                            license_plate + "Error while pushing data to downstream: " + push_db[1])
                                else:
                                    source_map[entity_id] = message
                                    self.logger.log(license_plate + "added new flow -> {} ".format(entity_id))
                        else:
                            self.logger.log(
                                license_plate + "Data was eliminated from the filter criteria. Was not pushed further downstream")
                            DatabusQueueTelemetry().update_filter_telemetry(call_type="REMOVED_BY_FILTER",
                                                                            message_group=self.message_group)

                self.queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occurred process message in DatabusFlowsQueue. Trace : {}".format(
                    traceback.format_exc())
                self.exception_logger.log(license_plate + "Exception: " + message)
                DatabusQueueTelemetry().update_exception_telemetry(exe_type=type(e).__name__)
