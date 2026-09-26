# AGENTS.md

面向 AI 代理的仓库工作说明。仓库结构与术语详见 `CONTEXT.md`，专题写作约定与发布流程详见 `README.md`。

## 部署（重要）

- 本仓库**没有 CI/CD 工作流**，`site/.github/` 下的 workflows 是上游 Quartz 的遗留文件，均带 `if: github.repository == 'jackyzha0/quartz'` 守卫，在本仓库永远空转，不要尝试修改或依赖它们。
- **push 到 `main` 后，Cloudflare 会自动拉取仓库、构建（Quartz build）并发布**，无需本地构建或手动部署。
- 部署目标为 Cloudflare Workers 静态资产，配置在根目录 `wrangler.jsonc`（资产目录 `site/public`），站点地址 `notes.forclh.workers.dev`（对应 `site/quartz.config.yaml` 的 `baseUrl`）。
- 因此：**任何影响站点内容的改动（笔记、`site/content/`、`site/quartz.config.yaml`），提交并 push 后即自动上线**。构建产物 `site/public/` 不会也不会需要入库（已加入 `.gitignore`）。

## 代理工作注意事项

- 修改笔记源文件后，需在 `site/` 目录运行 `node sync-content.mjs` 重新生成 `site/content/`（该脚本只依赖 Node 内置模块），生成结果一并提交。
- 不要手改笔记 frontmatter 中的 `permalink`（短码由同步脚本分配并固定）。
- 本环境的 Node 在处理中文文件名的 `rmSync`/`cpSync` 时会静默崩溃；`sync-content.mjs` 已按此约束编写，修改时保持"不删除、不递归拷贝中文命名文件"的原则。
