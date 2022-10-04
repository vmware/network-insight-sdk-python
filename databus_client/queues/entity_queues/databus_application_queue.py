import queue
import traceback
from time import sleep

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.log_handler.log_queue import LogQueue

from databus_client.filters.non_metric_filter import NonMetricFilter
from databus_client.utils.common.databus_constants import DatabusMessageGroup
from databus_client.queues.entity_queues.databus_queue import DatabusQueue
from databus_client.db_handler.mongoDB_handler.databus_hb_dbhandler import DatabusHeartBeatDbHandler
from databus_client.utils.databus_utilities import DatabusUtilities


class DatabusApplicationQueue(DatabusQueue):

    def __init__(self, use_mongo=True, message_group=None, file_threshold=None):
        super(DatabusApplicationQueue, self).__init__(message_group=DatabusMessageGroup.APPLICATIONS.value,
                                                      num_of_worker_threads=2, use_mongo=use_mongo,
                                                      file_threshold=file_threshold)
        self.logger = LogQueue(num_of_worker_threads=2, message_group=DatabusMessageGroup.APPLICATIONS.value,
                               file_threshold=file_threshold)
        self.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception",
                                         file_threshold=file_threshold)
        self.license_plate = ""

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
                    self.logger.log(self.license_plate + "---new source {} added".format(source))

                source_map = self.data_map[source]

                self.append_key_val_in_dict(message, ["id", "type", "specversion", "message_group", "status", "token"],
                                            entry)

                # if heart beat message
                if message["type"] == "HEARTBEAT":
                    self.append_key_val_in_dict(message, ["timestamp"], entry)
                    self.logger.log(
                        self.license_plate + ". Message received is identified as heartbeat. Bypassing filters")
                    DatabusHeartBeatDbHandler.get_instance(logger=self.logger,
                                                           ex_log=self.exception_logger).add_to_queue(message)
                else:
                    # if data message
                    self.append_key_val_in_dict(message, ["data"], entry)
                    entity_id = message["data"]["entity_id"]

                    self.count += 1  # 1 entity per entry

                    db_entry = dict()
                    db_entry.update({
                        "source": source,
                        "entity_id": entity_id,
                        "message": message,
                        "token": token})

                    """
                    Getting filtered pass
                    """
                    self.logger.log(self.license_plate + "Passing through filter.")

                    pass_through = NonMetricFilter.pass_non_metric_filter(source=source, entity_id=entity_id,
                                                                          entity_name=message["data"][
                                                                              "name"] if "name" in message[
                                                                              "data"] else None)

                    if pass_through:
                        self.logger.log(self.license_plate + "Got pass through from filter. Pushing data to downstream")
                        if entity_id in source_map:
                            # find and update
                            if self.use_mongo:
                                push_db = DatabusClientDataService.update_nonmetric_entity_message_group_data(db_entry,
                                                                                                              message_group=self.message_group)
                                if push_db[0]:
                                    self.logger.log(
                                        self.license_plate + "updated new application in mongo -> {} ".format(
                                            entity_id))
                                else:
                                    self.logger.log(
                                        self.license_plate + "Error while pushing data to downstream: " + push_db[1])
                            else:
                                source_map.update({entity_id: message})
                                self.logger.log(self.license_plate + "updated application -> {} ".format(entity_id))
                        else:
                            # add new
                            if self.use_mongo:
                                push_db = DatabusClientDataService.put_new_nonmetric_entity_message_group_data(db_entry,
                                                                                                               message_group=self.message_group)
                                source_map[entity_id] = dict()  # for look up only, hence not saving the message
                                if push_db[0]:
                                    self.logger.log(self.license_plate +
                                                    "added new application in mongo -> {} ".format(entity_id))
                                else:
                                    self.logger.log(
                                        self.license_plate + "Error while pushing data to downstream: " + push_db[1])
                            else:
                                source_map[entity_id] = message
                                self.logger.log(self.license_plate + "added new application-> {} ".format(entity_id))
                        self.queue.task_done()
                    else:
                        self.logger.log(
                            self.license_plate + "Data was eliminated from the filter criteria. Was not pushed "
                                                 "further downstream")
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occured process message in DatabusApplicationQueue. Trace : {}".format(
                    traceback.format_exc())
                self.exception_logger.log(self.license_plate + "Exception: " + message)
