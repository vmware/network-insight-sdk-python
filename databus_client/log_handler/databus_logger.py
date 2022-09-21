import os
from threading import Lock
from datetime import datetime

path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../utils/common/files/"))


class DatabusLoggerHandler:
    """
    This helps periodically save in-memory dict (if used) in pickle format.
    """
    main_folder = "databus_logs"
    sub_folders_files = {"applications": "applications",
                         "vms": "vms",
                         "hosts": "hosts",
                         "flows": "flows",
                         "problems": "problems",
                         "metrics": "metrics",
                         "vms-metrics": "vms-metrics",
                         "hosts-metrics": "hosts-metrics",
                         "nics-metrics": "nics-metrics",
                         "flows-metrics": "flows-metrics",
                         "switchports-metrics": "switchports-metrics",
                         "exception": "exception"}
    paths_dict = dict()
    lock = Lock()

    def create_file_structure(self):
        print("Creating folder and file structure")
        if os.path.exists(path + '/' + self.main_folder):
            pass
        else:
            os.makedirs(path + '/' + self.main_folder)
        sub_path = os.path.abspath(os.path.join(path + '/' + self.main_folder))
        x = datetime.now()
        for key, value in self.sub_folders_files.items():
            # print("Creating folder and file for {}".format(key))
            if os.path.exists(sub_path + '/' + key):
                pass
            else:
                os.makedirs(sub_path + '/' + key)
            file_path = os.path.abspath(os.path.join((sub_path + '/' + key)))
            file_name = x.strftime(value + '_' + '%d-%m-%Y' + '.log')
            open(file_path + '/' + file_name, 'a')
            self.paths_dict[key] = file_path + "/" + file_name
        return "Done"

    def get_file_path(self, message_group=None):
        return self.paths_dict[message_group]

    def get_file_name(self, message_group=None):
        for key, value in self.paths_dict:
            if key == message_group:
                return value