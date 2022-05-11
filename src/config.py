import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SHIFTS_FILENAME = os.getenv("SHIFTS_FILENAME") or "shifts.db"
SHIFTS_FILE_PATH = os.path.join(dirname, "..", SHIFTS_FILENAME)

USERS_FILENAME = os.getenv("USERS_FILENAME") or "users.db"
USERS_FILE_PATH = os.path.join(dirname, "..", USERS_FILENAME)
