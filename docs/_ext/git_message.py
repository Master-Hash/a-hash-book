from typing import Any
from hashlib import md5
from jinja2 import Template
import subprocess
from sphinx.application import Sphinx
import docutils.nodes as nodes

footer_template = Template("""<ul>
{% for i in xs %}
{% if i.ae == "56669192+Master-Hash@users.noreply.github.com" %}
{% set avatar = md5("a137294381b@163.com".encode()).hexdigest() %}
{% else %}
{% set avatar = md5(i.ae.lower().encode()).hexdigest() %}
{% endif %}

  <li>
    <a href="https://hash.toys/"><img src="https://gravatar.loli.top/avatar/{{ avatar }}" alt="@{{ i.an }}"></a>
    {{ i.an }}
    {{ i.s }}
    <a href="https://github.com/Master-Hash/a-hash-book/commit/{{ i.H }}">{{ i.h }}</a>
    {{ i.ad }}
  </li>
{% endfor %}
</ul>""")


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
                          "--format=%an¦%ae¦%ad¦%h¦%H¦%s",
                           "--", f"docs/{context['sourcename']}"
                           ],
                          capture_output=True,
                          )
    # 原谅我偷懒，用了一个实际上可行，但极不严谨的手法
    # i: j for (i, j) in zip(("an", "ae", "ad", "h", "H", "s"),
    tmp = data.stdout.decode("utf-8").split("\n")[:-1]
    tmp2 = (zip(("an", "ae", "ad", "h", "H", "s"), i.split("¦")) for i in tmp)
    xs = [{j: k for j, k in i} for i in tmp2]
    print(xs)
    if doctree and xs:
        context["theme_extra_footer"] += footer_template.render(xs=xs, md5=md5)


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("html-page-context", update_metadata)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
