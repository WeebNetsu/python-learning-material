import logging

# it is recommended to give every file its own logger name, otherwise the default name would be "root"
logger = logging.getLogger(__name__)

# If you dont want this file to log out it's messages when running it in the root file
# add the following code
# logger.propagate = False

# normal way to log out debug and stuff from a file
logger.debug("This is debug from a different file")



try:
	a = 10 / 0
except ZeroDivisionError as e:
	# exc_info will print more info about the error
	logging.error(e, exc_info=True)




# create handlers
# will log into that file (and create it if not created already)
file_handler = logging.FileHandler("log.txt")

file_handler.setLevel(logging.INFO)  # info and above levels will be logged

# the format in which it should be logged
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)  # add the handler

logger.info("This is being logged into a file")  # log it out

# output stream handler
stream_handler = logging.StreamHandler() # basic output stream (like saying: print())
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)  # add the handler
logger.error("AN ERROR OCCURED")




# the below module helps keep the log file(s) small in size
from logging.handlers import RotatingFileHandler
# maxBytes: max size of the file (in bytes)
# backupCount: How many old backup files are allowed
handler =  RotatingFileHandler("small_log.log", maxBytes=2000, backupCount=2)
n_logger = logging.getLogger(__name__)
n_logger.setLevel(logging.INFO)
n_logger.addHandler(handler)
# put the below in a massive for loop. The file size will only allow x amount of lines
# each time
# for _ in range(1000):
n_logger.info("This file will be kept a small size")



# the below module helps keep the log files updated over time
from logging.handlers import TimedRotatingFileHandler
"""
when:
s - seconds
m - minutes
h - hours
d - days
midnight
w0 - monday
w1 - tuesday 
etc.

The below will log out every 1 minute (intervals determained)
"""
s_handler =  TimedRotatingFileHandler("timed_log.log", when="m", interval=1, backupCount=0)
s_logger = logging.getLogger(__name__)
s_logger.setLevel(logging.INFO)
s_logger.addHandler(s_handler)
# put the below in a massive for loop. The file size will only allow x amount of lines
# each time
# for _ in range(1000):
s_logger.info("These files will be created as the program runs")



import logging.config # import logging configuration options

"""
HERE IS WHAT EVERYTHING IN THE FILE MEANS:
[loggers] -> this is all your loggers you have, you can have multiple types
keys=basicLogger,myOtherLogger,root -> 3 types of loggers (root must be included)

[handlers] -> types of handlers
[formatters] -> formatters

[logger_basicLogger] -> define the loggers you created by saying logger_loggerName
level=DEBUG -> what level to log out with
handlers=consoleHandler -> what handler to use
qualname=basicLogger -> (optional, don't have to add)
propogate=0 -> should it propogate (optional, don't have to add)

[handler_consoleHandler] -> define what the handler is you added
class=StreamHandler -> what class it should come from
args=(sys.stdout)

[formatter_simpleFormatter] -> define/create your format
"""

logging.config.fileConfig("logging.conf") # set the config file
logger = logging.getLogger("basicLogger") # set as logger inside config file
logger.debug("Debug message from custom logger")