import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger('threat_intel')
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler('logs/threat_intel.log', maxBytes=10000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger