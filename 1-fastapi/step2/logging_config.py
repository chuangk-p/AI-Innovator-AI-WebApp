import os
import logging.config
import pytz
from datetime import datetime

# Define the log format
log_format = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

# Define log_dir as None initially
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True) 

# Custom formatter to apply timezone
class TimezoneFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        tz = pytz.timezone("Asia/Bangkok")
        dt = datetime.fromtimestamp(record.created, tz)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

# Configure the logging
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': TimezoneFormatter,
            'format': log_format,
        },
        'simple': {
            '()': TimezoneFormatter,
            'format': log_format,
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(log_dir, 'app.log') if log_dir else 'logs/app.log',
            'formatter': 'verbose',
            'when': 'midnight',
            'backupCount': 0,
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
})

def get_logger(name):
    return logging.getLogger(name)

logger = logging.getLogger(__name__)