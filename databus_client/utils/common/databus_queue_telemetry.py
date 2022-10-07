import json
import threading
from enum import Enum

from databus_client.utils.common.databus_message_entity_count_recorder import DatabusMessageEntityCountRecorder


class EnumCall(Enum):
    POST = 0,
    GET = 1,
    DELETE = 2
    COPY = 3
    EXCEPTION = 4


def singleton(class_):
    lock = threading.Lock()
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            with lock:
                instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DatabusQueueTelemetry:
    """
    This utility gives us how many POST/GET/DELETE calls have happened.
    This utility gives us count of response-codes (200, 500) for POST/GET/DELETE calls have happened.
    This utility persists and gives Exceptions that have happened at various points.
    """

    def __init__(self, reduced_message=True):
        self.status_dict = dict()
        self.generic_failures = dict()
        self.summary_dict = dict()
        self.exception = dict()
        self.reduced_message = reduced_message
        self.recorder_duration = DatabusMessageEntityCountRecorder.get_instance().get_duration()

    def update_telemetry_config(self, url_param_dict=None):
        recorder_duration = url_param_dict["recorder_duration"] if "recorder_duration" in url_param_dict else \
            DatabusMessageEntityCountRecorder.get_instance().get_duration()

        self.recorder_duration = DatabusMessageEntityCountRecorder.get_instance().set_duration(recorder_duration)

    def update_post_telemetry(self, status=None, info_data_dict=None):
        # reset if required
        self._update_status(call_type="POST", message_group=info_data_dict["message_group"], status=status)
        self._update_summary(call_type="POST", message_group=info_data_dict["message_group"])

    def update_get_telemetry(self, status=None, info_data_dict=None):
        self._update_status(call_type="GET", message_group=info_data_dict["message_group"], status=status)
        self._update_summary(call_type="GET", message_group=info_data_dict["message_group"])

    def update_put_telemetry(self, status=None, info_data_dict=None):
        self._update_status(call_type="PUT", message_group=info_data_dict["message_group"], status=status)
        self._update_summary(call_type="PUT", message_group=info_data_dict["message_group"])

    def update_delete_telemetry(self, status=None, info_data_dict=None):
        self._update_status(call_type="DELETE", message_group=info_data_dict["message_group"], status=status)
        self._update_summary(call_type="DELETE", message_group=info_data_dict["message_group"])

    def update_copy_telemetry(self, status=None, info_data_dict=None):
        self._update_status(call_type="COPY", message_group=info_data_dict["message_group"], status=status)
        self._update_summary(call_type="COPY", message_group=info_data_dict["message_group"])

    def update_filter_telemetry(self, call_type=None, message_group=None):
        self._update_summary(call_type=call_type, message_group=message_group)

    def update_exception_telemetry(self, exe_type=None):
        if self.exception:
            if exe_type in self.exception:
                self.exception[exe_type] = self.exception[exe_type] + 1
            else:
                self.exception[exe_type] = 1
        else:
            self.exception[exe_type] = 1

    def _update_status(self, call_type=None, message_group=None, status=None):
        if call_type not in self.status_dict:
            self.status_dict[call_type] = dict()

        call_dict = self.status_dict[call_type]

        if message_group not in call_dict:
            call_dict[message_group] = dict()

        group_dict = call_dict[message_group]

        if status in group_dict:
            group_dict[status] += 1
        else:
            group_dict[status] = 1

    def _update_summary(self, call_type=None, message_group=None):
        if call_type not in self.summary_dict:
            self.summary_dict[call_type] = dict()

        call_dict = self.summary_dict[call_type]

        if message_group not in call_dict:
            call_dict[message_group] = 1
        else:
            call_dict[message_group] += 1

    def get_telemetry_dict(self, as_json=False):
        result_dict = {
            "SUMMARY": self.summary_dict,
            "REQUEST_STATUS": self.status_dict,
            "EXCEPTION": self.exception,
            # Below is to record the data received previous 5 minutes
            # "ENTITY_COUNT": DatabusMessageEntityCountRecorder.get_instance().get_data()
        }

        if as_json:
            return json.dumps(result_dict)
        else:
            return result_dict
