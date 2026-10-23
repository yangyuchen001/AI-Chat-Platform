"""env_check 的测试：伪造环境变量，验证退出码契约（P0.20 P18.1）。"""

from application import env_check

REQUIRED = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]


def test_all_required_vars_present_returns_zero(isolated_env, monkeypatch):
    for name in REQUIRED:
        monkeypatch.setenv(name, "test-value")
    assert env_check.main() == 0


def test_all_missing_returns_one(isolated_env):
    assert env_check.main() == 1


def test_partial_missing_returns_one(isolated_env, monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    assert env_check.main() == 1
