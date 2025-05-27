#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import pathlib
import shutil
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from create_dotdesktop import create_dotdesktop

extras_require = {}

repo_root = pathlib.Path(__file__).parent
install_requires = (repo_root / "requirements.txt").read_text(encoding="UTF-8").split('\n')

create_dotdesktop("0.1.8")

setup(
		data_files=[("share/applications", ["PySetWacom.desktop"])],
		description="A GUI utility for configuring buttons on graphics tablets and styli",
		extras_require=extras_require,
		install_requires=install_requires,
		name="pysetwacom",
		py_modules=[],
		)

shutil.rmtree("PySetWacom.egg-info", ignore_errors=True)
