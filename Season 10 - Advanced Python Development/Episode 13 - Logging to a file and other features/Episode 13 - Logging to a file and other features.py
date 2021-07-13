# Logging to a file and other features

import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)-8s [%(filename)s:%(lineno)d] : %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',    # Added date format
    level=logging.DEBUG,
    filename='logs.txt'     # just add a filename here or known as logging in file
)

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will show up')
logger.debug('This is a Debug message.')
logger.critical('This is a Critical message.')

