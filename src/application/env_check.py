"""哨兵：检查 P18.1 需要的环境变量，缺失则以非零码退出（补全 P0.03 的失败契约）

P0.17：启动时先加载项目根的 .env（真值不进 git，模板见 .env.example）。
优先级：真实环境变量 > .env —— 已存在的变量不会被覆盖。
P0.18：print 升级为 logging，级别闸门由 APP_ENV 决定（dev=DEBUG，其余=INFO）。
"""

import logging
import os
import sys

from dotenv import load_dotenv

from application.logging_setup import setup_logging

logger = logging.getLogger(__name__)

REQUIRED = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]


def main() -> int:
    load_dotenv()  # 载入 .env；已存在的真实环境变量优先，不覆盖
    setup_logging()  # 装配日志闸门：读 APP_ENV 决定级别

    missing = [name for name in REQUIRED if os.environ.get(name) is None]

    for name in REQUIRED:
        if name in missing:
            logger.error("缺少必需变量: %s", name)
        else:
            logger.info("变量就绪: %s（值不打印）", name)

    if missing:
        logger.error("共 %d 个必需变量缺失", len(missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
