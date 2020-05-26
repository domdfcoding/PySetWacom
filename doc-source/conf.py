#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is managed by `git_helper`. Don't edit it directly

import os
import re
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from sphinx.locale import _

from __pkginfo__ import __version__

import shutil

for image in os.listdir('../images'):
	s = os.path.join('../images', image)
	d = os.path.join('./images', image)
	if os.path.isdir(s):
		shutil.copytree(s, d)
	else:
		shutil.copy2(s, d)

github_url = f"https://github.com/domdfcoding/PySetWacom"

rst_prolog = f""".. |pkgname| replace:: PySetWacom
.. |pkgname2| replace:: ``PySetWacom``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
.. |ghurl| replace:: {github_url}
"""

author = "Dominic Davis-Foster"
project = "PySetWacom"
slug = re.sub(r'\W+', '-', project.lower())
release = version = __version__
copyright = "2020 Dominic Davis-Foster"
language = 'en'
package_root = "PySetWacom"

extensions = [
		'sphinx.ext.intersphinx',
		'sphinx.ext.autodoc',
		'sphinx.ext.mathjax',
		'sphinx.ext.viewcode',
		'sphinxcontrib.httpdomain',
		"sphinxcontrib.extras_require",
		"sphinx.ext.todo",
		"sphinxemoji.sphinxemoji",
		"sphinx_autodoc_typehints",
		]

sphinxemoji_style = 'twemoji'
todo_include_todos = bool(os.environ.get("SHOW_TODOS", False))

templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = {
		'rtd': ('https://docs.readthedocs.io/en/latest/', None),
		'sphinx': ('https://www.sphinx-doc.org/en/stable/', None),
		'python': ('https://docs.python.org/3/', None),
		"NumPy": ('https://numpy.org/doc/stable/', None),
		"SciPy": ('https://docs.scipy.org/doc/scipy/reference', None),
		"matplotlib": ('https://matplotlib.org', None),
		"h5py": ('https://docs.h5py.org/en/latest/', None),
		"Sphinx": ('https://www.sphinx-doc.org/en/stable/', None),
		"Django": ('https://docs.djangoproject.com/en/dev/', 'https://docs.djangoproject.com/en/dev/_objects/'),
		"sarge": ('https://sarge.readthedocs.io/en/latest/', None),
		"attrs": ('https://www.attrs.org/en/stable/', None),
		}

html_theme = 'alabaster'
html_theme_options = {
		'page_width': '1200px',
		'logo_name': 'true',
		'github_user': 'domdfcoding',
		'github_repo': 'PySetWacom',
		'description': 'Update multiple configuration files, build scripts etc. from a single location',
		'github_banner': 'true',
		'github_type': 'star',
		'badge_branch': 'master',
		'fixed_sidebar': 'false',
		}
html_theme_path = ["../.."]
# html_logo = "logo/pyms.png"
html_show_sourcelink = False  # True will show link to source

html_context = {
		}

htmlhelp_basename = slug

latex_documents = [
		('index', f'{slug}.tex', project, author, 'manual'),
		]

man_pages = [
		('index', slug, project, [author], 1)
		]

texinfo_documents = [
		('index', slug, project, author, slug, project, 'Miscellaneous'),
		]


# Extensions to theme docs
def setup(app):
	from sphinx.domains.python import PyField
	from sphinx.util.docfields import Field

	app.add_object_type(
			'confval',
			'confval',
			objname='configuration value',
			indextemplate='pair: %s; configuration value',
			doc_field_types=[
					PyField(
							'type',
							label=_('Type'),
							has_arg=False,
							names=('type',),
							bodyrolename='class'
							),
					Field(
							'default',
							label=_('Default'),
							has_arg=False,
							names=('default',),
							),
					]
			)
