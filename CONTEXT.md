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
章节笔记"作业（可使用AI）"段中的学习任务。参考答案在"参考答案"段展示：可以是内联的代码块或文字要点，也可以是 `homework/` 文件夹下的单文件 `.py` 源码（如 `05-p1.py`），通过嵌入展示在笔记正文中。
_Avoid_: 练习、代码文件

**目录页**:
`type: MOC` 的笔记，作为专题的索引和学习路径，用双链指向各篇笔记。
_Avoid_: 索引、首页

**短码**:
每篇笔记在网站 URL 中的永久唯一标识，首次发布时随机分配后固定不变，与文件名和标题无关。
_Avoid_: slug、编码、ID

**官网样式**:
以 Quartz 官方文档站（quartz.jzhao.xyz）为基准的视觉风格：不加载任何第三方主题包（原生默认样式）、官方字体并补充中文字体、标题下方仅保留日期与阅读时长，不显示 Properties 折叠块和面包屑。
_Avoid_: minimal 主题、Obsidian 样式、quartz-themes 主题包
