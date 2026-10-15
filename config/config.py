"""公共接口配置不依赖MySQL；仅运行数据库测试时检查密码。"""
import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env", override=False)
TEST_ENV = os.getenv("TEST_ENV", "test")
ENV_CONFIG = {
    "test": {
        "base_url": "https://jsonplaceholder.typicode.com",
        "headers_url": "https://httpbin.org/headers",
        "bearer_url": "https://httpbin.org/bearer",
        "cookies_url": "https://httpbin.org/cookies",
        "mysql_database": "test_db",
        "request_timeout": 5,
        "retry_times": 3,
    }
}


def validate_test_environment():
    # 必须先检查环境，再索引字典，避免KeyError掩盖真实配置问题。
    if TEST_ENV == "prod":
        raise RuntimeError("禁止连接生产环境")
    if TEST_ENV not in ENV_CONFIG:
        raise ValueError(f"不支持的环境：{TEST_ENV}；当前仅配置test")
    database = os.getenv("MYSQL_DATABASE", ENV_CONFIG[TEST_ENV]["mysql_database"])
    if database.lower().startswith("prod"):
        raise RuntimeError("禁止连接生产数据库")


validate_test_environment()
CURRENT_CONFIG = ENV_CONFIG[TEST_ENV]
BASE_URL = CURRENT_CONFIG["base_url"]
HEADERS_URL = CURRENT_CONFIG["headers_url"]
BEARER_URL = CURRENT_CONFIG["bearer_url"]
COOKIES_URL = CURRENT_CONFIG["cookies_url"]
REQUEST_TIMEOUT = CURRENT_CONFIG["request_timeout"]
RETRY_TIMES = CURRENT_CONFIG["retry_times"]
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": MYSQL_PASSWORD,
    "database": os.getenv("MYSQL_DATABASE", CURRENT_CONFIG["mysql_database"]),
    "charset": "utf8mb4",
}


def validate_mysql_environment():
    validate_test_environment()
    if not MYSQL_CONFIG["password"]:
        raise ValueError("未配置MYSQL_PASSWORD；仅运行MySQL测试时需要在.env或环境变量中设置")
