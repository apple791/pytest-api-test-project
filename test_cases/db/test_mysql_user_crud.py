"""只在显式启用MySQL练习时写入独立记录，并清理自己的记录。"""
from uuid import uuid4
import pytest
from common.mysql_util import execute_mysql, query_mysql

pytestmark = pytest.mark.mysql


def test_insert_and_query_mysql_user():
    user_id = int(uuid4().hex[:7], 16) + 10000
    assert not query_mysql("SELECT id FROM users WHERE id=%s", (user_id,)), "随机ID冲突，请重新执行"
    affected = execute_mysql("INSERT INTO users(id,name,phone) VALUES(%s,%s,%s)",
                             (user_id, "Charlie", "13712345678"))
    try:
        assert affected == 1
        rows = query_mysql("SELECT id,name,phone FROM users WHERE id=%s", (user_id,))
        assert len(rows) == 1
        assert rows[0]["name"] == "Charlie"
        assert rows[0]["phone"] == "13712345678"
    finally:
        execute_mysql("DELETE FROM users WHERE id=%s", (user_id,))
