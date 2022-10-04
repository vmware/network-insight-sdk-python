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


class DatabusHostsQueue(DatabusQueue):

    def __init__(self, use_mongo=True, message_group=None, file_threshold=None):
        super(DatabusHostsQueue, self).__init__(message_group=DatabusMessageGroup.HOSTS.value, num_of_worker_threads=2,
                                                use_mongo=use_mongo)
        self.logger = LogQueue(num_of_worker_threads=2, message_group=DatabusMessageGroup.HOSTS.value, file_threshold=file_threshold)
        self.exception_logger = LogQueue(num_of_worker_threads=1, message_group="exception", file_threshold=file_threshold)
        self.license_plate = DatabusUtilities.get_license_plate()

    def start_processing_data(self):

        def update_message(message, data):

            self.count += 1  # 1 entity per entry
            token = message["token"] = self.get_dict_val("token", entry)
            entity_id = data["entity_id"]
            message["data"] = data

            db_entry = dict()
            db_entry.update({
                "source": message["source"],
                "entity_id": entity_id,
                "message": message,
                "token": token})

            """
            Getting filtered pass
            """
            self.logger.log(self.license_plate + "Passing through filter.")
            pass_through = NonMetricFilter.pass_non_metric_filter(source=message["source"], entity_id=entity_id,
                                                                  entity_name=message["data"]["name"] if "name" in message["data"] else None)

            if pass_through:
                if entity_id in source_map:
                    # find and update
                    if self.use_mongo:
                        push_db = DatabusClientDataService.update_nonmetric_entity_message_group_data(db_entry,
                                                                                                      message_group=self.message_group)
                        if push_db[0]:
                            self.logger.log(self.license_plate + "updated new host in mongo -> {} ".format(entity_id))
                        else:
                            self.logger.log(
                                self.license_plate + "Error while pushing data to downstream: " + push_db[1])
                    else:
                        source_map.update({entity_id: message})
                        self.logger.log(self.license_plate + "updated host -> {} ".format(entity_id))
                else:
                    # add new
                    if self.use_mongo:
                        push_db = DatabusClientDataService.put_new_nonmetric_entity_message_group_data(db_entry,
                                                                                                       message_group=self.message_group)
                        source_map[entity_id] = dict()  # for look up only, hence not saving the message
                        if push_db[0]:
                            self.logger.log(self.license_plate + "added new host in mongo -> {} ".format(entity_id))
                        else:
                            self.logger.log(
                                self.license_plate + "Error while pushing data to downstream: " + push_db[1])
                    else:
                        source_map[entity_id] = message
                        self.logger.log(self.license_plate + "added new host -> {} ".format(entity_id))
            else:
                self.logger.log(
                    self.license_plate + "Data was eliminated from the filter criteria. Was not pushed further downstream")

        while True:
            entry = None
            try:
                entry = self.queue.get(block=False)
                self.license_plate = "[License Plate: " + self.license_plate + "] "
                self.logger.log(self.license_plate + "Processing Request : " + str(entry))

                _source = self.get_dict_val("source", entry)

                if _source not in self.data_map:
                    self.data_map[_source] = dict()
                    self.logger.log(self.license_plate +"---new source {} added".format(_source))

                source_map = self.data_map[_source]

                message_type = self.get_dict_val("type", entry)

                header = dict()
                self.append_key_val_in_dict(header, ["id", "type", "specversion", "source", "message_group", "status", "token"], entry)

                # if heart beat message
                if message_type == "HEARTBEAT":
                    self.append_key_val_in_dict(header, ["timestamp"], entry)
                    self.logger.log(
                        self.license_plate + ". Message received is identified as heartbeat. Bypassing filters")
                    DatabusHeartBeatDbHandler.get_instance(logger=self.logger, ex_log=self.exception_logger).add_to_queue(header)
                else:

                    host_data = self.get_dict_val("data", entry)

                    if type(host_data) == list:
                        self.count += len(host_data)
                        for host in host_data:
                            update_message(header, host)
                    else:
                        self.count += 1  # 1 entity per entry
                        update_message(header, host_data)

                self.queue.task_done()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                message = "Error occured process message in DatabusHostsQueue. Trace : {}".format(traceback.format_exc())
                self.exception_logger.log(self.license_plate + "Exception: " + message)
