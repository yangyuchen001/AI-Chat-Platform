"""哨兵：检查 P18.1 需要的环境变量，缺失则以非零码退出（补全 P0.03 的失败契约）"""

import os
import sys

REQUIRED = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]

def main() -> int:
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