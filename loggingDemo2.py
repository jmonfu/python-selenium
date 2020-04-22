import logging

logging.basicConfig(filename="C://SeleniumTest//logging.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is an warning message")
logger.error("This is an error message")
logger.critical("This is an critical message")
