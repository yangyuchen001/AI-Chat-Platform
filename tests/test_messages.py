"""normalize_message 的测试：正常、边界、异常三视角（P0.19）。"""

import pytest

from application.messages import normalize_message


# 视角 1：正常行为
def test_normal_text_is_returned():
    assert normalize_message("Hello World") == "Hello World"


def test_surrounding_spaces_are_stripped():
    assert normalize_message("  Hello  ") == "Hello"


# 视角 2：边界条件
def test_empty_string_is_rejected():
    with pytest.raises(ValueError, match="must not be empty"):
        normalize_message("")


# 视角 3：异常行为
def test_whitespace_only_is_rejected():
    with pytest.raises(ValueError, match="must not be empty"):
        normalize_message("   ")


def test_non_string_is_rejected():
    with pytest.raises(TypeError, match="must be a string"):
        normalize_message(123)
