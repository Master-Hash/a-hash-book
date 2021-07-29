from typing import Any
from sphinx.application import Sphinx
import docutils.nodes as nodes


def update_metadata(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document,
) -> None:
    if doctree:
        context["metatags"] += f'<link rel="mask-icon" href="{app.config["pinned_tab_icon"]}" color="{app.config["pinned_tab_color"]}">'


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value("pinned_tab_icon", None, "html")
    app.add_config_value("pinned_tab_color", None, "html")
    app.connect("html-page-context", update_metadata)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
