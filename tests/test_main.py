"""main 的测试：伪造命令行参数，验证入口契约（P0.20 P18.1）。"""

import sys

from application import main as main_module


def test_no_argument_returns_one(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py"])
    assert main_module.main() == 1
    assert "用法" in capsys.readouterr().err


def test_version_flag_prints_and_returns_zero(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "--version"])
    assert main_module.main() == 0
    assert "AI Chat Platform" in capsys.readouterr().out


def test_start_with_env_name_returns_zero(monkeypatch, caplog):
    monkeypatch.setattr(sys, "argv", ["main.py", "dev"])
    assert main_module.main() == 0
    assert "启动完成" in caplog.text
