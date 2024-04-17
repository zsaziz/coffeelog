# local lib
from utils.common_utils import get_current_local_datetime

# python lib
import logging
import os

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'

LOGS_PATH = os.path.abspath(f'logs/{get_current_local_datetime().strftime(DATETIME_FORMAT)}.log')


def get_logger(namespace=__name__, save_file=False):
    logging.basicConfig(filename=LOGS_PATH if save_file else None,
                        format='%(asctime)s:%(module)s:%(levelname)s: %(message)s', datefmt='%m/%d/%Y-%I:%M:%S:%p',
                        level=logging.INFO)
    logger = logging.getLogger(namespace)
    logger.setLevel(logging.INFO)

    # Stop duplicate log statements
    # https://stackoverflow.com/questions/72943164/python-logging-duplicate-output
    logger.propagate = False

    # create console handler and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s:%(module)s:%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger