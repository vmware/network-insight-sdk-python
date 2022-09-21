import os.path
import shutil
import threading
from time import sleep
from datetime import datetime


from databus_client.log_handler.databus_logger import DatabusLoggerHandler
from databus_client.log_handler.file_handler import DatabusLogFileHandler


class DatabusLogFileScheduler:
    """
    This helps periodically save in-memory dict (if used) in pickle format.
    """

    def __init__(self, message_group=None, file_threshold=None, file_log_handler=None):
        log_handler = DatabusLoggerHandler()
        self.message_group = message_group
        self.file_threshold = file_threshold
        self.file_log_handler = file_log_handler
        self.file_path = log_handler.get_file_path(message_group=message_group)
        t = threading.Thread(target=self.start_periodic_schedule)
        t.start()

    def start_periodic_schedule(self):
        while True:
            sleep(5*60)
            if os.path.exists(self.file_path):
                file_size = self.get_file_size(file_path=self.file_path)
                if file_size > self.file_threshold:
                    self.perform_rollover(file_path=self.file_path)
        print("Done")

    def get_file_size(self, file_path=None):
        return os.path.getsize(file_path) / (1024 * 1024)

    def perform_rollover(self, file_path=None):
        dir = os.path.dirname(file_path)
        new_file = dir + "/" + "temp.log"
        open(new_file, "a")
        DatabusLogFileHandler.refresh_file_path(new_file)
        self.rollover_file(file=file_path, dir=dir, temp_file=new_file)
        print("Done")

    def rollover_file(self, file=None, dir=None, temp_file=None):
        x = datetime.now()
        name = DatabusLoggerHandler.get_file_name(message_group=self.message_group)

        shutil.make_archive(file, 'zip', dir)
        file_name = x.strftime('%d-%m-%Y' + self.message_group + '.txt')
        new_file = open(dir + '/' + file_name, 'a')
        with open(temp_file, "r") as input:
            with open(new_file, "w") as output:
                for line in input:
                    output.write(line)
        self.file_path = new_file
        DatabusLogFileHandler.refresh_file_path(new_file)