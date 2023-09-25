import calendar
import time
from time import sleep


class DatabusMessageEntityCountRecorder:
    """
    This class is designed to record number of entities that are processed by individual queues.
    Data (count) is pulled from queues processor classes as per the _duration that is set.
    This is just a bookkeeping class.
    """
    __shared_instance = None
    _message_count_log = dict()
    _queue_processor = dict()
    _duration = 300

    def __init__(self):
        DatabusMessageEntityCountRecorder.__shared_instance = self

    @staticmethod
    def get_instance():
        if DatabusMessageEntityCountRecorder.__shared_instance is None:
            __shared_instance = DatabusMessageEntityCountRecorder()
        return DatabusMessageEntityCountRecorder.__shared_instance

    def start_recording(self):
        while True:
            if len(self._queue_processor) == 0:
                sleep(1)
                continue

            current_epoch = calendar.timegm(time.gmtime())
            if current_epoch % self._duration == 0:
                for queue_name, queue in self._queue_processor.items():
                    self._add_entry(queue_name, current_epoch, queue.count)

            sleep(1)

    def register_queue(self, queue_processor):
        self._queue_processor[queue_processor.message_group] = queue_processor
        print("{} queue-processor registered to DatabusMessageEntityCountRecorder".format(queue_processor.message_group))

    def deregister_queue(self, queue_processor):
        try:
            del self._queue_processor[queue_processor.message_group]
        except KeyError as e:
            print("{} key does not exist".format(queue_processor.message_group))

    def get_data(self):
        return self._message_count_log

    def set_duration(self, duration):
        self._duration = int(duration)

    def get_duration(self):
        return self._duration

    def _add_entry(self, message_group, push_timestamp, count):
        # print("Message Count log added: {} - {} - {}".format(message_group, push_timestamp, count))
        if message_group in self._message_count_log:
            group_to_update = self._message_count_log[message_group]
            group_to_update.update({
                push_timestamp: count,
            })
        else:
            self._message_count_log[message_group] = {
                push_timestamp: count
            }
