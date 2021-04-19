import logging
import os

logging.basicConfig(level=os.environ.get("LOGGING_LEVEL", "DEBUG"))
