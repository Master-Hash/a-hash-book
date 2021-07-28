# a-hash-book

## 写作流程
1. 创建新 branch 作为草稿，每个 branch 只允许一篇草稿
2. 需要正式发表时，先将文章加入 `_toc.yml`，再 squeeze merge 到 main branch，提交信息为“首次发表”或其它有意义的备注。

注意：author，changelog 将从 commit message 中提取。

## 编译
因为 dirhtml builder 暂时有锅，使用默认编译模式：

```console
$ jb build -W --keep-going docs
```

或使用 vsocde 编译命令：`Tasks: Run Build Task`（`Ctrl` + `Shift` + `B`）

我目前对 pdflatex builder 效果很不满意。暂不提供。

<!-- 如果需要编译整本书 pdf，请参阅 jupyter book 文档。

```
$ jb build -W --keep-going --builder pdflatex docs
``` -->
