import queue
import threading

from databus_client.db_handler.mongoDB_handler.databus_client_data_service import DatabusClientDataService
from databus_client.utils.common.databus_message_entity_count_recorder import DatabusMessageEntityCountRecorder


class DatabusQueue:

    def __init__(self, message_group=None,
                 num_of_worker_threads=2,
                 use_mongo=False, file_threshold=None):
        self.queue = queue.Queue()
        self.data_map = dict()
        self.threads = list()
        self.num_of_worker_threads = num_of_worker_threads
        self.message_group = message_group
        self.file_threshold = file_threshold
        self.count = 0  # depicts count of an entity process in queue (eq to count of unique entity ids)
        self.use_mongo = use_mongo

        DatabusMessageEntityCountRecorder.get_instance().register_queue(self)

        for i in range(self.num_of_worker_threads):
            t = threading.Thread(target=self.start_processing_data)
            self.threads.append(t)
            t.start()

    def start_processing_data(self):
        """
        parent method. Nothing to see here ;)
        :return:
        :rtype:
        """
        pass

    def add_to_queue(self, data=None):
        if type(data) == dict:
            self.queue.put(data)
        elif type(data) == list:
            for entry in data:
                self.queue.put(entry)
        else:
            raise Exception(
                "Invalid Data found to be added in queue for message group {}. Data --> {}".format(self.message_group,
                                                                                                   data))

    def update_from_dump(self, data=None):
        self.data_map = data

    def get_data_map(self):
        return self.data_map

    def reset_data_map(self, request_filter_dict):
        if self.use_mongo:
            if "source" in request_filter_dict:
                source = request_filter_dict["source"]
                entity_id = None
                if "entity_id" in request_filter_dict:
                    entity_id = request_filter_dict["entity_id"]

                result_dict = DatabusClientDataService.delete_data_for_source_message_group(source,
                                                                                            self.message_group,
                                                                                            entity_id=entity_id)
                if source in self.data_map:
                    self.data_map.pop(source)
                return result_dict
            else:
                message = "source attribute is must. Not provided for get call message_group {}.".format(
                    self.message_group, )
                print("Exception: " + message)
                raise Exception(message)

        else:
            self.data_map.clear()

    def get_dict_val(self, key, entry):
        # TODO: Enable when debug mode added in logs
        # self.logger.log(self.license_plate + "fetch key {} in entry type {}".format(key, type(entry)))
        if key in entry:
            return entry[key]
        else:
            message = "$$$$$$$$ Key: {} not found in {} $$$$$$$$$$".format(key, entry)
            print(message)
            print("Exception: " + message)
            return None

    def append_key_val_in_dict(self, target_dict, keys, source_dict):

        for key in keys:
            if key in source_dict:
                target_dict.update({key: self.get_dict_val(key, source_dict)})
            else:
                message = "Required Key: {} not found in source_dict {} ".format(key, source_dict)
                print(message)
                print("Exception: " + message)

        return target_dict

    def get_filtered_data(self, request_filter_dict=None):
        data_dict = dict()
        if self.use_mongo:

            if "source" in request_filter_dict:
                source = request_filter_dict["source"]

                entity_id = request_filter_dict["entity_id"] if "entity_id" in request_filter_dict else None

                #  based on customer_id + entity_id
                result_dict = DatabusClientDataService.get_data_for_source_nonmetric_message_group(source,
                                                                                                   self.message_group,
                                                                                                   entity_id=entity_id)
                return result_dict

            else:
                message = "source attribute is must. Not provided for get call message_group {}.".format(
                    self.message_group, )
                print("Exception: " + message)
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
