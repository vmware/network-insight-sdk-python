import os
import threading
import traceback
from os import listdir
from os.path import isfile, join
from time import sleep

from databus_client.log_handler.databus_logger import DatabusLoggerHandler


class DatabusLogFileCleanup:

    """
    Old logs are always archived.
    Cleanup logic is implemented to keep last two records and cleanup the rest
    """

    def __init__(self, message_group=None):
        self.message_group = message_group
        self.folder_path = DatabusLoggerHandler.get_file_folder(message_group=message_group)
        t = threading.Thread(target=self.start_periodic_schedule)
        t.start()

    def start_periodic_schedule(self):
        while True:
            sleep(10 * 60)
            file_list = []
            f_list = [f for f in listdir(self.folder_path) if isfile(join(self.folder_path, f))]
            org_list = []
            for file in f_list:
                if ".gz" in file:
                    file_list.append(file)
                    org_list.append(file)
            try:
                file_list.sort(reverse=True)
                if len(file_list) > 2:
                    del file_list[2:]

                for f_d in org_list:
                    if f_d not in file_list:
                        print("Deleted file {}".format(str(f_d)))
                        os.remove(self.folder_path + '/' + f_d)
            except Exception as e:
                tb = traceback.format_exc()
                print("Error in file cleanup." + tb)


if __name__ == "__main__":
    ob = DatabusLogFileCleanup(message_group="vms")
