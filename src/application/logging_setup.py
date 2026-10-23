"""日志总装：全局唯一的 basicConfig 所在地（P0.18）。

级别闸门由 APP_ENV 决定：dev=DEBUG（诊断全开），其余环境=INFO（生产口径）。
"""

import logging
import os


def setup_logging() -> None:
    env = os.environ.get("APP_ENV", "dev")
    level = logging.DEBUG if env == "dev" else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger(__name__).debug(
        "日志闸门=%s（APP_ENV=%s）", logging.getLevelName(level), env
    )
