# 冲突处理记录：README tagline（P0.12）

- 症状: git merge feature/readme-tagline 报 CONFLICT (content): README.md
- 原因: main 与 feature 相对共同祖先 c583035 都修改了 README 第 3 行（feature 版 b8947d5，main 版 32b4ed2），三方合并无法自动裁决
- 证据: git status 显示 both modified；文件中的 <<<<<<< HEAD / ======= / >>>>>>> feature/readme-tagline 冲突标记
- 处理: 手工融合两版 tagline（工程基础优先 + 逐步长成 AI Chat Platform），删除冲突标记，git add 标记已解决，git commit 完成合并
- 结果: 诞生 merge commit ba4f605（两个父亲：32b4ed2 与 b8947d5），README 为融合版
