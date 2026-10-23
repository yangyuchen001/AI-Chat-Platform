"""项目测试的公共 fixture（P0.20）。

conftest.py 是 pytest 的约定文件：其中的 fixture 对整个 tests/ 目录可见，无需 import。
"""

import pytest

REQUIRED_ENV = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]


@pytest.fixture
def isolated_env(monkeypatch, tmp_path):
    """给 env_check 一个干净的运行环境：

    - cwd 切到空沙盒——项目根的 .env 不会被 load_dotenv 打扫进来
    - 三个必需变量清空——不受开发机真实环境影响
    """
    monkeypatch.chdir(tmp_path)
    for name in REQUIRED_ENV:
        monkeypatch.delenv(name, raising=False)
    return tmp_path
