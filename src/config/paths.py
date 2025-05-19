from pathlib import Path

# Path to the project root
PATH = Path(__file__).resolve().parent.parent.parent

# Logs
LOGS_DIR = PATH / 'logs/'
LOGS_FILE = LOGS_DIR / 'jobNest.log'
