import sqlite3

def query_db(sql, params=None, db_path="demo.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    if params is None:
        params = ()

    cursor.execute(sql, params)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(dict(row))

    cursor.close()
    conn.close()

    return result


def init_demo_db(db_path="demo.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    INSERT OR REPLACE INTO users (id, name, phone, status)
    VALUES (1, '张三', '13812345678', 'active')
    """)

    cursor.execute("""
    INSERT OR REPLACE INTO users (id, name, phone, status)
    VALUES (2, '李四', 'abc', 'inactive')
    """)

    cursor.execute("""
    INSERT OR REPLACE INTO users (id, name, phone, status)
    VALUES (3, '王五', '13900001111', 'active')
    """)

    conn.commit()
    cursor.close()
    conn.close()