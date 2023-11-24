import gzip
import os.path
import threading
import traceback
from time import sleep
from datetime import datetime

from databus_client.log_handler.databus_logger import DatabusLoggerHandler
from databus_client.log_handler.file_cleanup import DatabusLogFileCleanup
from databus_client.log_handler.file_handler import DatabusLogFileHandler


class DatabusLogFileScheduler:
    """
    This periodically checks the log file size and if found above threshold,
    then zip that files replacing with new one
    """
    file_count = {"applications": 0,
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

    def __init__(self, message_group=None, file_threshold=None, file_log_handler=None):
        self.message_group = message_group
        self.file_threshold = file_threshold
        self.file_log_handler = file_log_handler
        self.file_path = DatabusLoggerHandler.get_file_path(message_group=message_group)
        self.file_cleanup = DatabusLogFileCleanup(message_group=message_group)
        t = threading.Thread(target=self.start_periodic_schedule)
        t.start()

    def start_periodic_schedule(self):
        while True:
            try:
                sleep(1 * 60)
                if os.path.exists(self.file_path):
                    file_size = self.get_file_size(file_path=self.file_path)
                    if self.file_threshold is None:
                        self.file_threshold = 100
                    else:
                        if file_size > float(self.file_threshold):
                            self.perform_rollover(file_path=self.file_path)
            except Exception as e:
                tb = traceback.format_exc()
                print("Error in scheduler." + tb)

    def get_file_size(self, file_path=None):
        return os.path.getsize(file_path) / (1024 * 1024)

    def perform_rollover(self, file_path=None):
        dirt = os.path.dirname(file_path)
        new_file = dirt + "/" + "temp.log"
        open(new_file, "a")
        DatabusLoggerHandler.set_file_path(message_group=self.message_group, file_path=new_file)
        DatabusLogFileHandler.update_path_lib(message_group=self.message_group)
        self.rollover_file(file=file_path, dirt=dirt, temp_file=new_file)
        print("Log file rollover performed successfully for {}".format(self.message_group))

    def rollover_file(self, file=None, dirt=None, temp_file=None):
        x = datetime.now()
        # checking and updating count
        file_count = self.file_count[self.message_group]
        file_name = x.strftime(self.message_group + '_' + '%d-%m-%Y' + "_" + str(file_count) + '.log')

        # compressing file
        new_file_path = dirt + '/' + file_name
        new_file = open(new_file_path, 'a')
        new_file.close()
        self.file_path = new_file_path

        with open(file) as log:
            with gzip.open(file + '.gz', 'wt') as comp_log:
                comp_log.writelines(log)

        # updating the new file path
        DatabusLoggerHandler.set_file_path(message_group=self.message_group, file_path=new_file_path)

        # writing content of temp into new file
        with open(temp_file, "r") as input:
            with open(new_file_path, "w") as output:
                for line in input:
                    output.write(line)

        # updating scheduler fileCount dict
        self.file_count[self.message_group] = file_count + 1

        # Removing old log file and temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)
        if os.path.exists(file):
            os.remove(file)
