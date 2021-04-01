import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG") == "1"
AMQP_URI = os.getenv("AMQP_URI")
DATABASE_URI = os.getenv("DATABASE_URI")
CACHE_URI = os.getenv("CACHE_URI")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
