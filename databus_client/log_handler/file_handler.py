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

    def __init__(self, message_group=None, queue=None):
        self.message_group = message_group
        self.queue = queue

        handler = DatabusLoggerHandler()
        self.file_path = handler.get_file_path(message_group=self.message_group)
        t = threading.Thread(target=self.write_in_file)
        t.start()

    def write_in_file(self):
        while True:
            try:
                entry = self.queue.get(block=False)
                time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file = open(self.file_path, "a")  # append mode
                file.write(time + ": " + entry + "\n")
                file.close()
            except queue.Empty as e:
                sleep(1)
            except Exception as e:
                print("Exception occurred: " + str(traceback.print_exc()))

    def refresh_file_path(self, file_path=None):
        self.file_path = file_path
