import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

print(f"SYS.PATH={sys.path}")

from octodns.__init__ import __version__

### sphinx config ###

project = "octodns"
copyright = "2017-present"  # noqa
author = "Ross McFarland"
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
]


### autodoc ###

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "special-members": "__init__, __repr__",
    # "inherited-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}
autodoc_typehints = "both"
autodoc_typehints_description_target = "all"
autodoc_member_order = "bysource"

### extlinks ###

extlinks = {
    "github": ("https://github.com/%s", "%s"),
    "pypi": ("https://pypi.org/project/%s/", "%s"),
}
extlinks_detect_hardcoded_links = True


### intersphinx ###

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "dnspython": ("https://dnspython.readthedocs.io/en/stable/", None),
    "six": ("https://six.readthedocs.io/", None),
    "python-dateutil": ("https://dateutil.readthedocs.io/en/stable/", None),
    "fqdn": ("https://fqdn.readthedocs.io/en/latest/", None),
}


### todo ###

todo_include_todos = True


### myst ###

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3


### content ###

master_doc = "index"

templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


### theme ###

# html_theme = "alabaster"
html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/octodns/octodns/",
    "source_branch": "main",
    "source_directory": "docs/",
}
