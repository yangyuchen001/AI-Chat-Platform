"""AI Chat Platform 启动入口（P0.03）。P0.18：启动事件改走 logging。"""

import logging
import sys

from application import __version__
from application.logging_setup import setup_logging


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "用法: python -m application.main [--version | <环境名>]", file=sys.stderr
        )
        print("错误: 缺少参数", file=sys.stderr)
        return 1

    if sys.argv[1] == "--version":
        # 版本号是程序的「产物」，走 stdout——print 是对的
        print(f"AI Chat Platform {__version__}")
        return 0

    setup_logging()
    logger = logging.getLogger(__name__)
    env_name = sys.argv[1]
    # 启动过程是「运行事件」，走日志
    logger.info("AI Chat Platform 启动中... 环境: %s", env_name)
    logger.info("启动完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
