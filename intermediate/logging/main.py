import logging  

#Need the config to return the time and Debug mode, review python docs logging config, loffinf facility, time format
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

""" #Calling default logger - Not recommended- basic
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message') """


#Logging in different modules using helper: It return the message from helper with the name of the logger, create a hierarchy of loggers
#import helper


#Calling to logging.conf usinf a file 
# There is another option using dictionaries, check docs
""" import logging.config
logging.config.fileConfig('intermediate/logging/logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message') """


#Raises and exception: two ways
""" try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:                             
    logging.error(e, exc_info=True)                     # REturn info from stacktrace - the traceback info included
 """


# Import Traceback to return same info
""" import traceback                                        # Using the traceback library we can get traceback info too

try:
    a=[1,2,3]
    val=a[4]
except:
    logging.error("The error is %s", traceback.format_exc()) """



#Rotating fileHandler for large applications, a lot of log messages
""" from logging.handlers import RotatingFileHandler        # To Rotate files accord configuration - in this case after 2KB

logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB and keep backup logs: app.log , app.log.1 , app.log2, etc...
handler=RotatingFileHandler('intermediate/logging/app.log',maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello World') """



import time
from logging.handlers import TimedRotatingFileHandler   # To Rotate  every some time

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Time available: s,m,h,d,midnight,w0
handler = TimedRotatingFileHandler('intermediate/logging/timed_test.log',when='s', interval=5,backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, World!')
    time.sleep(5)
