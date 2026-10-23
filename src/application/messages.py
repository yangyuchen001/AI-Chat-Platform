"""消息校验（P18.1 领域逻辑）：规范化用户消息，拒绝无效输入。

接口契约：
- str 输入 → 返回去首尾空格后的文本
- 非 str 输入 → TypeError
- 空串 / 纯空白 → ValueError
"""


def normalize_message(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    normalized = message.strip()
    if not normalized:
        raise ValueError("message must not be empty")
    return normalized
