#!/usr/bin/env bash
# AI Chat Platform 启动脚本（Linux/WSL 侧）
export UV_PROJECT_ENVIRONMENT="$HOME/.venvs/ai-chat-platform"
uv run python -m application.main dev
