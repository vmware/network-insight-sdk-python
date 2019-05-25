# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import time
import datetime
import logging
import os

LOG_LEVEL = logging.DEBUG


def get_start_time(delta_days):
    delta = datetime.timedelta(days=delta_days)
    start_date = datetime.datetime.fromtimestamp(time.time())
    start_date = start_date - delta
    start = int(start_date.strftime("%s"))
    return start


def get_end_time():
    return int(time.time())


def configure_logging(path_to_log_directory):
    """
    Configure logger
    :param path_to_log_directory:  path to directory to write log file in
    :return:
    """
    log_filename = 'vrni_sdk_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
    vrni_sdk_logger = logging.getLogger('vrni_sdk')
    vrni_sdk_logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

    fh = logging.FileHandler(filename=os.path.join(path_to_log_directory, log_filename))
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)
    vrni_sdk_logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(LOG_LEVEL)
    sh.setFormatter(formatter)
    vrni_sdk_logger.addHandler(sh)
