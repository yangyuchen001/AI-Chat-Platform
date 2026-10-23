"""AI Chat Platform 启动入口（P0.03）。"""

import sys

from application import __version__

def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python -m application.main [--version | <环境名>]", file=sys.stderr)
        print("错误: 缺少参数", file=sys.stderr)
        return 1

    if sys.argv[1] == "--version":
        print(f"AI Chat Platform {__version__}")
        return 0

    env_name = sys.argv[1]
    print(f"AI Chat Platform 启动中... 环境: {env_name}")
    print("启动完成")
    return 0

if __name__ == "__main__":
    sys.exit(main())