import queue
import threading
import traceback
from threading import Lock
from time import sleep
from datetime import datetime

from databus_client.log_handler.databus_logger import DatabusLoggerHandler


class DatabusLogFileHandler:
    """
    This helps periodically save in-memory dict (if used) in pickle format.
    """
    lock = Lock()
    path_lib = {"applications": 0,
                "vms": 0,
                "hosts": 0,
                "flows": 0,
                "problems": 0,
                "metrics": 0,
                "vms-metrics": 0,
                "hosts-metrics": 0,
                "nics-metrics": 0,
                "flows-metrics": 0,
                "switchports-metrics": 0,
                "nsxt-edge-node-metrics": 0,
                "exception": 0}

    def __init__(self, message_group=None, queue=None):
        self.message_group = message_group
        self.queue = queue
        self.file_path = DatabusLoggerHandler.get_file_path(message_group=self.message_group)
        t = threading.Thread(target=self.write_in_file)
        t.start()

    def write_in_file(self):
        while True:
            try:
                entry = self.queue.get(block=False)
                time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                if self.path_lib[self.message_group] > 0:
                    self.file_path = DatabusLoggerHandler.get_file_path(message_group=self.message_group)
                    self.path_lib[self.message_group] = 0
                file = open(self.file_path, "a")  # append mode
                file.write(time + ": " + entry + "\n")
                file.close()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                print("Exception occurred: " + str(traceback.print_exc()))

    @classmethod
    def update_path_lib(cls, message_group=None):
        cls.path_lib[message_group] = 1
