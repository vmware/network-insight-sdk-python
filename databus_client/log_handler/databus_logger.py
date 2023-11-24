import os
from threading import Lock
from datetime import datetime

path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../logs/"))


class DatabusLoggerHandler:
    """
    This creates log files structure per message group
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
                         "nsxt-edge-node-metrics": "nsxt-edge-node-metrics",
                         "exception": "exception"}
    paths_dict = dict()
    lock = Lock()

    @staticmethod
    def create_file_structure():
        print("Creating folder and file structure")
        if os.path.exists(path + '/' + DatabusLoggerHandler.main_folder):
            pass
        else:
            os.makedirs(path + '/' + DatabusLoggerHandler.main_folder)
        sub_path = os.path.abspath(os.path.join(path + '/' + DatabusLoggerHandler.main_folder))
        x = datetime.now()
        for key, value in DatabusLoggerHandler.sub_folders_files.items():
            if os.path.exists(sub_path + '/' + key):
                pass
            else:
                os.makedirs(sub_path + '/' + key)
            file_path = os.path.abspath(os.path.join((sub_path + '/' + key)))
            file_name = x.strftime(value + '_' + '%d-%m-%Y' + '.log')
            open(file_path + '/' + file_name, 'a')
            DatabusLoggerHandler.paths_dict[key] = file_path + "/" + file_name
        return "Done"

    @staticmethod
    def get_file_path(message_group=None):
        return DatabusLoggerHandler.paths_dict[message_group]

    @staticmethod
    def get_file_name(message_group=None):
        for key, value in DatabusLoggerHandler.paths_dict:
            if key == message_group:
                return value

    @staticmethod
    def set_file_path(message_group=None, file_path=None):
        DatabusLoggerHandler.paths_dict[message_group] = file_path

    @staticmethod
    def get_file_folder(message_group=None):
        if os.path.exists(path + '/' + DatabusLoggerHandler.main_folder):
            sub_path = os.path.abspath(os.path.join(path + '/' + DatabusLoggerHandler.main_folder))
            pre_name = sub_path + '/' + message_group
            if os.path.exists(pre_name):
                return pre_name
