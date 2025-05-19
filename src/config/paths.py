from pathlib import Path

PATH = Path(__file__).resolve().parent.parent.parent


LOGS_DIR = PATH / 'logs/'
LOGS_FILE = LOGS_DIR / 'jobNest.log'