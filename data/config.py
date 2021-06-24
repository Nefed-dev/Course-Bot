import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMIN_LIST = list(os.getenv('ADMIN_LIST'))
ADMIN_ID = [1782255380, ]

DB_USER = str(os.getenv('DB_USER'))
DB_PASS = str(os.getenv('DB_PASSWORD'))
DB_NAME = str(os.getenv('DB_NAME'))
DB_HOST = str(os.getenv('DB_HOST'))
