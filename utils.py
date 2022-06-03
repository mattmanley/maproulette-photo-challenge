import sys
import logging

def init_logger(name):
	"""Initialize logging"""

	logger = logging.getLogger(name)
	logger.setLevel(logging.INFO)
	handler = logging.StreamHandler(sys.stdout)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	return logger
