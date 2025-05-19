import logging
from logging.handlers import RotatingFileHandler

from config.paths import LOGS_FILE

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

file_handler = RotatingFileHandler(
	filename=LOGS_FILE,
	maxBytes=5000,
	backupCount=3
)

def get_logger(name: str):
	logger = logging.getLogger(name)
	logger.addHandler(file_handler)
	return logger