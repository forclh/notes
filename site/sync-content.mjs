#!/usr/bin/env node
/**
 * 内容同步脚本：仓库根目录的笔记 → site/content/
 *
 * 1. 为每篇缺少 permalink 的笔记分配 6 位小写短码，写回源笔记 frontmatter（永久固定）；
 *    已有 permalink 统一转小写（Quartz 的 slug 解析会小写化 URL，避免大小写不一致）
 * 2. 由源笔记生成 site/content/<短名>/<短码>.md：
 *    - 内容副本的 title 加章节号前缀（explorer 按显示名排序，保证目录按章节顺序排列）
 *    - 移除内容中的 permalink（与 alias-redirects 自跳冲突）
 *    - 去掉正文开头与 title 重复的一级标题（与官网样式一致）
 *    - [[文件名]] 双链重写为 [[<短名>/<短码>]]，保证链接解析（解析不认 aliases）
 * 3. 用专题目录页生成首页 content/index.md
 *
 * 注意：本环境的 Node 在处理中文文件名的 rmSync/cpSync 时会静默崩溃，
 * 因此全程不删除、不递归拷贝中文命名文件（content 目录名是 ASCII，可安全重建）。
 *
 * 用法：node sync-content.mjs   （在 site/ 目录下运行；写笔记后需重新执行）
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const siteDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(siteDir, "..");
const contentDir = path.join(siteDir, "content");

/** 专题映射：仓库根目录的文件夹名 → URL 英文短名。新增专题在这里加一行即可。 */
const SUBJECTS = [{ dir: "Python语言核心精讲", short: "python" }];

const BASE36 = "abcdefghijklmnopqrstuvwxyz0123456789";
const randomCode = () =>
  crypto.randomBytes(6).reduce((s, b) => s + BASE36[b % 36], "");

const frontmatterOf = (text) => {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  return m ? { raw: m[0], body: text.slice(m[0].length), yaml: m[1] } : null;
};

const permalinkOf = (text) =>
  frontmatterOf(text).yaml.match(/^permalink:\s*(.+)$/m)[1].trim();

// ---------- 第 1 步：为源笔记分配 permalink 短码 ----------
const subjects = []; // { dir, short, notes: [{ file, name, code }] }
for (const { dir, short } of SUBJECTS) {
  const srcDir = path.join(repoRoot, dir);
  const notes = [];
  for (const f of fs.readdirSync(srcDir).filter((f) => f.endsWith(".md"))) {
    const file = path.join(srcDir, f);
    let text = fs.readFileSync(file, "utf8");
    let fm = frontmatterOf(text);
    if (!fm) {
      text = `---\npermalink: ${short}/${randomCode()}\n---\n\n${text}`;
      fm = frontmatterOf(text);
    } else if (/^permalink:/m.test(fm.yaml)) {
      // 统一小写；若与 frontmatter 前缀短名不一致则修正
      const old = fm.yaml.match(/^permalink:\s*(.+)$/m)[1].trim();
      const fixed = `${short}/${old.split("/").pop().toLowerCase()}`;
      if (old !== fixed) {
        text = text.replace(/^permalink:.*$/m, `permalink: ${fixed}`);
        fs.writeFileSync(file, text);
      }
    } else {
      text = text.replace(/---\r?\n/, `---\npermalink: ${short}/${randomCode()}\n`);
      fs.writeFileSync(file, text);
    }
    notes.push({ file, name: f.slice(0, -3), code: permalinkOf(text) });
  }
  subjects.push({ dir, short, notes });
}

// 全局短码查重（跨专题），重复者重新分配
{
  const seen = new Map();
  for (const s of subjects) {
    for (const n of s.notes) {
      const code = n.code.split("/").pop();
      if (seen.has(code)) {
        let text = fs.readFileSync(n.file, "utf8");
        text = text.replace(/^permalink:.*$/m, `permalink: ${s.short}/${randomCode()}`);
        fs.writeFileSync(n.file, text);
        n.code = permalinkOf(text);
      } else seen.set(code, n);
    }
  }
}

// 文件名 → 完整短码路径 的映射，供双链重写
const nameMap = new Map();
for (const s of subjects) for (const n of s.notes) nameMap.set(n.name, n.code);

// ---------- 第 2 步：清空并重建 content ----------
fs.rmSync(contentDir, { recursive: true, force: true });
fs.mkdirSync(contentDir, { recursive: true });

/** [[原名]] / [[原名|显示]] / [[原名#标题]] / [[原名#标题|显示]] → 短码路径
 *  无显式显示名时保留原文件名作为显示文本；表格行内竖线需转义为 \| */
const rewriteWikiLinks = (text) =>
  text
    .split("\n")
    .map((line) => {
      const sep = line.trimStart().startsWith("|") ? "\\|" : "|";
      return line.replace(/\[\[([^\[\]]+)\]\]/g, (whole, inner) => {
        const pipeAt = inner.search(/\||\\\|/);
        const target = pipeAt === -1 ? inner : inner.slice(0, pipeAt);
        const rest = pipeAt === -1 ? "" : inner.slice(pipeAt);
        const hashAt = target.indexOf("#");
        const page = hashAt === -1 ? target : target.slice(0, hashAt);
        const anchor = hashAt === -1 ? "" : target.slice(hashAt);
        const code = nameMap.get(page.trim());
        if (!code) return whole; // 非页面链接（页内锚点等）保持原样
        const display = rest || `${sep}${inner}`;
        return `[[${code}${anchor}${display}]]`;
      });
    })
    .join("\n");

// ---------- 第 3 步：生成内容（短码命名 + title 前缀 + 双链重写） ----------
for (const { short, notes } of subjects) {
  const destDir = path.join(contentDir, short);
  fs.mkdirSync(destDir, { recursive: true });

  for (const { file, code } of notes) {
    let text = fs.readFileSync(file, "utf8");
    // 内容副本的 title 加章节号前缀：explorer 按显示名排序，保证目录按章节顺序排列
    const chapter = frontmatterOf(text).yaml.match(/^chapter:\s*(.+)$/m)?.[1].trim();
    if (chapter) {
      text = text.replace(/^(title:\s*)/m, `$1${chapter} `);
    }
    // 内容文件名已是短码，permalink 会与 alias-redirects 冲突（自己跳自己），从内容中移除
    let body = text.replace(/^permalink:.*$\r?\n?/m, "");
    // 页面标题由 frontmatter 的 title 渲染，去掉正文开头重复的一级标题（与官网样式一致）
    body = body.replace(
      /^(---\r?\n[\s\S]*?\r?\n---\r?\n?)(?:[ \t]*\r?\n)*(#[ \t]+[^\n]*\r?\n+)/,
      "$1"
    );
    fs.writeFileSync(path.join(destDir, `${code.split("/").pop()}.md`), rewriteWikiLinks(body));
  }
}

// ---------- 第 4 步：生成首页（专题目录页的正文，同样重写双链） ----------
const moc = subjects[0].notes.find((n) => path.basename(n.file).startsWith("00-"));
if (moc) {
  let { body } = frontmatterOf(fs.readFileSync(moc.file, "utf8")) ?? { body: "" };
  // 首页标题为 AK's Notes，同样去掉正文开头重复的一级标题
  body = body.replace(/^(?:[ \t]*\r?\n)*(#[ \t]+[^\n]*\r?\n+)/, "");
  fs.writeFileSync(
    path.join(contentDir, "index.md"),
    `---\ntitle: AK's Notes\n---\n${rewriteWikiLinks(body)}`
  );
}

const noteCount = subjects.reduce((n, s) => n + s.notes.length, 0);
console.log(`✓ 同步完成：${noteCount} 篇笔记`);
