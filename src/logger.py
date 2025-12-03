import logging


def setup_logging():
    logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()
logger = setup_logging()

def log_message(message, level="info"):
    if level == "error":
        logging.error(message)
    else:
        logging.info(message)
    print(message)