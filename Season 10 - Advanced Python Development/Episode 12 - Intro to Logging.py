# introduction to logging in python

"""
logging module is used to print things out similar to print(), we've used before but more powerful than that, and used
mainly to print logs.

levels of logging,
with lowest to highest

DEBUG - ONLY when you are developing and not when the application is running.
INFO

WARNING
ERROR
CRITICAL
"""
import logging

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s' ,level=logging.DEBUG)
# A bit nicer formatted string
logging.basicConfig(format='%(asctime)s : %(levelname)-8s [%(filename)s:%(lineno)d] : %(message)s' ,level=logging.DEBUG)
logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will show up')
logger.debug('This is a Debug message.')
logger.critical('This is a Critical message.')
