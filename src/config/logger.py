import logging
from logging.handlers import RotatingFileHandler

from config.paths import LOGS_FILE


# Logger configuration
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

# File handler
file_handler = RotatingFileHandler(
	filename=LOGS_FILE,
	maxBytes=5000,
	backupCount=3
)

# Changes the format binded to file handler
file_handler.formatter = logging.Formatter(
	'[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')


def get_logger(name: str):
	"""
	Returns a new logger with the specified name. The logger is automatically
	set with a file handler, meaning the logs will be displayed both on the
	console and the log file.

	:param name: name of the logger that will be returned
	:type name: str
	:return: the logger object
	:rtype: Logger

	:Example:

	>>> get_logger(None)
	ValueError
	"""
	if name is None:
		raise ValueError("Name can't be none")
	logger = logging.getLogger(name)
	logger.addHandler(file_handler)
	return logger
