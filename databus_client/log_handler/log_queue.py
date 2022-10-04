import queue
import threading

from databus_client.log_handler.file_handler import DatabusLogFileHandler
from databus_client.log_handler.log_file_scheduler import DatabusLogFileScheduler


class LogQueue:

    def __init__(self, num_of_worker_threads=2, message_group=None, file_threshold=None):
        self.queue = queue.Queue()
        self.data_map = dict()
        self.threads = list()
        self.num_of_worker_threads = num_of_worker_threads
        self.message_group = message_group
        self.file_handler = DatabusLogFileHandler(message_group=message_group, queue=self.queue)
        self.file_scheduler = DatabusLogFileScheduler(message_group=message_group, file_threshold=file_threshold,
                                                      file_log_handler=self.file_handler)

        for i in range(self.num_of_worker_threads):
            t = threading.Thread(target=self.start_processing_data)
            self.threads.append(t)
            t.start()

    def start_processing_data(self):
        pass

    def log(self, message):
        self.queue.put(message)
