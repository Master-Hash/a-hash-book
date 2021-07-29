from sys import stdout
from typing import Any
import subprocess
from sphinx.application import Sphinx
import docutils.nodes as nodes


def update_metadata(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document,
) -> None:
    if "sourcename" not in context:
        return
    data = subprocess.run(["git", "-P", "log", "--follow",
                          "--format='%an¦%ce¦%ad¦%h¦%s'",
                           "--", f"docs/{context['sourcename']}*"
                           ],
                          capture_output=True,
                          )
    # 原谅我偷懒，用了一个实际上可行，但极不严谨的手法
    tmp = data.stdout.decode("utf-8").split("\n")[:-1]
    xs = [i.split("¦") for i in tmp]
    if doctree and xs:
        # subprocess.run(['clear'])
        # for i in context:
        #     print(i + str(" " if type(context[i]) != str else context[i]))
        # print(x)
        for x in xs:
            context["theme_extra_footer"] += \
                f'作者 {x[0]} 邮箱 {x[1]} 修改时间 {x[2]} commit hash {x[3]} commit message {x[4]} 没法集成 有空再改'


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("html-page-context", update_metadata)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
