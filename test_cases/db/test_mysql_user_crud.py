# MySQL 用户数据增删改查测试
# 验证 execute_mysql() 的写入能力和 query_mysql() 的查询能力
from common.mysql_util import execute_mysql, query_mysql

def test_insert_and_query_mysql_user():
    insert_sql = """
        insert into users(id, name, phone)
        values(%s, %s, %s) as new
        on duplicate key update
            name = new.name,
            phone = new.phone
    """

    affected_rows = execute_mysql(
        insert_sql,
        (3, "Charlie", "13712345678")
    )
    assert affected_rows >= 1

    query_sql = "select * from users where id = %s"
    rows = query_mysql(query_sql, (3,))

    assert len(rows) == 1
    assert rows[0]["name"] == "Charlie"
    assert rows[0]["phone"] == "13712345678"