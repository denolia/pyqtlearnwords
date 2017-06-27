import logging
import sys
import logging.handlers

from colorlog import ColoredFormatter


def configure_logging():
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    LOG_LEVEL = logging.DEBUG
    LOGFORMAT = " %(log_color)s%(asctime)-6s:%(name)-6s.%(funcName)s():%(lineno)d%(reset)s | " \
                "[PID:%(process)d TID:%(thread)d] | %(log_color)s%(message)s%(reset)s"
    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(fmt=LOGFORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    handlers = [
        logging.handlers.RotatingFileHandler('rotated.log', encoding='utf8',
    maxBytes=100000, backupCount=1),
        logging.StreamHandler(stream=sys.stdout)
    ]
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    for h in handlers:
        h.setFormatter(formatter)
        h.setLevel(LOG_LEVEL)
        root_logger.addHandler(h)
