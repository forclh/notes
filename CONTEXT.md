# 笔记站

个人学习笔记仓库及其发布网站。笔记用 Obsidian 语法编写，通过 Quartz 构建为静态网站发布到 Cloudflare。

## Language

**专题**:
一个顶层文件夹，代表一门课程或一个主题（如"Python语言核心精讲"），内含该专题的全部笔记。
_Avoid_: 课程、目录、分类

**笔记**:
专题下的一个 Markdown 文件，带 YAML frontmatter（chapter/title/type/tags）和编号文件名，是网站的基本发布单元。
_Avoid_: 文章、页面、post

**作业**:
`homework/` 文件夹下的 Python 源码文件（如 `05-p1.py`），不单独成页，通过嵌入展示在笔记正文中。
_Avoid_: 练习、代码文件

**目录页**:
`type: MOC` 的笔记，作为专题的索引和学习路径，用双链指向各篇笔记。
_Avoid_: 索引、首页

**短码**:
每篇笔记在网站 URL 中的永久唯一标识，首次发布时随机分配后固定不变，与文件名和标题无关。
_Avoid_: slug、编码、ID
