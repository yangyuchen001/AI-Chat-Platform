"""AI Chat Platform 最小启动脚本（P0.03）"""

import sys

def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python main.py <环境名>", file=sys.stderr)
        print("错误: 缺少环境名参数", file=sys.stderr)
        return 1

    env_name = sys.argv[1]
    print(f"AI Chat Platform 启动中... 环境: {env_name}")
    print("启动完成")
    return 0

if __name__ == "__main__":
    sys.exit(main())