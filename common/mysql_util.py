# MySQL 数据库连接与操作工具。
import pymysql

from config.config import MYSQL_CONFIG

def get_mysql_connection():
    return pymysql.connect(
        host=MYSQL_CONFIG["host"],
        port=MYSQL_CONFIG["port"],
        user=MYSQL_CONFIG["user"],
        password=MYSQL_CONFIG["password"],
        database=MYSQL_CONFIG["database"],
        charset=MYSQL_CONFIG["charset"],
        cursorclass=pymysql.cursors.DictCursor
    )

def query_mysql(sql, params=None):
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()
    finally:
        connection.close()

def execute_mysql(sql, params=None):
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            affected_rows = cursor.rowcount

        connection.commit()
        return affected_rows

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()