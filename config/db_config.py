import os

from dotenv import load_dotenv

load_dotenv()  # read variables from .env in project root (if present)

db_config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "retail_db"),
}
