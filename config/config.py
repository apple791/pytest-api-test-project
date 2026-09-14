import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://jsonplaceholder.typicode.com"

HEADERS_URL = "https://httpbin.org/headers"

BEARER_URL = "https://httpbin.org/bearer"

COOKIES_URL = "https://httpbin.org/cookies"

mysql_password = os.getenv("MYSQL_PASSWORD")

if not mysql_password:
    raise ValueError(
        "未配置 MYSQL_PASSWORD，请检查项目根目录下的 .env 文件"
    )

MYSQL_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": mysql_password,
    "database": "test_db",
    "charset": "utf8mb4"
}