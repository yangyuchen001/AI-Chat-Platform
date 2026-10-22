"""检查 P18.1 未来需要的三个环境变量（P0.05：只做概念与读取）"""

import os

REQUIRED = ["APP_ENV", "DATABASE_URL", "LLM_API_KEY"]

for name in REQUIRED:
    if os.environ.get(name) is None:
        print(f"[缺失] {name} —— 未设置")
    else:
        print(f"[就绪] {name} —— 已设置（值不打印）")