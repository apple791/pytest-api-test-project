from common.db_util import query_db

def test_query_users():
    sql = "select * from users WHERE id = ?"

    data = query_db(sql, (1,))

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["name"] == "张三"

def test_query_active_users():
    sql = "select * from users where status = ?"

    data = query_db(sql, ("active",))

    assert len(data) > 0

    for item in data:
        assert item["status"] == "active"