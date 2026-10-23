"""项目测试的公共 fixture（P0.20）。

conftest.py 是 pytest 的约定文件：其中的 fixture 对整个 tests/ 目录可见，无需 import。
"""

import pytest

REQUIRED_ENV = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]


@pytest.fixture
def isolated_env(monkeypatch, tmp_path):
    """给 env_check 一个干净的运行环境：

    - load_dotenv 替换为空操作——它默认按调用者文件位置向上搜索，
      会爬到项目根找到真 .env（测试必须切断这条供给线）
    - 三个必需变量清空——不受开发机真实环境影响
    """
    monkeypatch.setattr("application.env_check.load_dotenv", lambda: None)
    for name in REQUIRED_ENV:
        monkeypatch.delenv(name, raising=False)
    return tmp_path
