import logging
import os

LOG_PATH = "logs/app.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message: str):
    logging.error(message)