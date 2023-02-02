# NOTE TO FUTURE SELF: DON'T let VSCode format the code if you want it to work

import logging

# this is an optional line of code, but it sets the logging level to debug and sets the format
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")

# There are multiple logging levels:
logging.debug("This is debug")
logging.info("This is info")
# only warning and above gets printed by default (inless logging level changed in basicConfig)
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")

import other_file
