"""哨兵：检查 P18.1 需要的环境变量，缺失则以非零码退出（补全 P0.03 的失败契约）

P0.17：启动时先加载项目根的 .env（真值不进 git，模板见 .env.example）。
优先级：真实环境变量 > .env —— 已存在的变量不会被覆盖。
"""

import os
import sys

from dotenv import load_dotenv

REQUIRED = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]


def main() -> int:
    load_dotenv()  # 载入 .env；已存在的真实环境变量优先，不覆盖
    missing = [name for name in REQUIRED if os.environ.get(name) is None]

    for name in REQUIRED:
        if name in missing:
            print(f"[缺失] {name} —— 未设置")
        else:
            print(f"[就绪] {name} —— 已设置（值不打印）")

    if missing:
        print(f"错误: {len(missing)} 个必需变量缺失", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())