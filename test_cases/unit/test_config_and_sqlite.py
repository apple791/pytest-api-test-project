"""配置修复的离线回归：无需公网、MySQL或浏览器。"""
import os
from pathlib import Path
import subprocess
import sys

import pytest

pytestmark = pytest.mark.unit

ROOT = Path(__file__).resolve().parents[2]


def import_config_without_env_file(tmp_path, test_env):
    folder = tmp_path / 'config'
    folder.mkdir()
    target = folder / 'config.py'
    target.write_text((ROOT / 'config/config.py').read_text(encoding='utf-8-sig'), encoding='utf-8')
    env = {k: v for k, v in os.environ.items() if k not in {'MYSQL_PASSWORD', 'TEST_ENV'}}
    env['TEST_ENV'] = test_env
    env['PYTHON_DOTENV_DISABLED'] = '1'
    return subprocess.run([sys.executable, '-c',
        'import runpy,sys; data=runpy.run_path(sys.argv[1]); print(data["TEST_ENV"])', str(target)],
        env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')


def test_api_config_does_not_require_mysql_password(tmp_path):
    result = import_config_without_env_file(tmp_path, 'test')
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == 'test'


def test_unknown_environment_has_clear_error(tmp_path):
    result = import_config_without_env_file(tmp_path, 'unknown')
    assert result.returncode != 0
    assert 'ValueError' in result.stderr and '不支持' in result.stderr
    assert 'KeyError' not in result.stderr


def test_production_environment_is_rejected_before_lookup(tmp_path):
    result = import_config_without_env_file(tmp_path, 'prod')
    assert result.returncode != 0
    assert 'RuntimeError' in result.stderr and '禁止' in result.stderr


def test_mysql_password_checked_only_when_connecting(monkeypatch):
    from common import mysql_util
    monkeypatch.setitem(mysql_util.MYSQL_CONFIG, 'password', None)
    def unexpected_connection(**kwargs):
        raise AssertionError('缺少密码时不应尝试网络连接')
    monkeypatch.setattr(mysql_util.pymysql, 'connect', unexpected_connection)
    with pytest.raises(ValueError, match='MYSQL_PASSWORD'):
        mysql_util.get_mysql_connection()


def test_sqlite_fixture_uses_independent_database(init_db):
    from common.db_util import query_db
    assert isinstance(init_db, Path)
    assert init_db.name == 'demo.db'
    assert init_db != ROOT / 'demo.db'
    rows = query_db('SELECT id FROM users ORDER BY id', db_path=init_db)
    assert [row['id'] for row in rows] == [1, 2, 3]