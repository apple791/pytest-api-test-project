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