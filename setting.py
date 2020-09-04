import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")
PROXY = os.getenv("PROXY")