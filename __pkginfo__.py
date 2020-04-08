# Copyright (C) 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py

import pathlib

VERSION = "0.1.5"

modname = "PySetWacom"
py_modules = None
entry_points = {
		'console_scripts': [
				'PySetWacom=PySetWacom:main',
				'pysetwacom=PySetWacom:main',
				]
		}
# Credit: https://stackoverflow.com/a/12514470/3092681

license = 'GPLv3'

short_desc = 'A GUI utility for configuring buttons on graphics tablets and styli'

classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		"Topic :: Utilities",
		"Topic :: Artistic Software",
		"Topic :: Multimedia :: Graphics",
		]

author = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
github_username = "domdfcoding"
web = github_url = f"https://github.com/{github_username}/{modname}"

# Get info from files; set: long_description
if pathlib.Path.cwd().name == "doc-source":
	print(pathlib.Path.cwd().parent / "README.rst")
	install_requires = (pathlib.Path.cwd().parent / "requirements.txt").read_text().split("\n")
	long_description = (pathlib.Path.cwd().parent / "README.rst").read_text() + '\n'
else:
	print(pathlib.Path("README.rst"))
	install_requires = pathlib.Path("requirements.txt").read_text().split("\n")
	long_description = pathlib.Path("README.rst").read_text() + '\n'

data_files = [
		('share/applications', ['PySetWacom.desktop']),
		]
