#!/usr/bin/env python
# This file is managed by `git_helper`. Don't edit it directly
"""Setup script"""

from __pkginfo__ import *

from setuptools import setup, find_packages

# Create .desktop file
with open("PySetWacom.desktop", "w") as desktop:
	desktop.write(f"""[Desktop Entry]
Version={__version__}
Name={modname}
Comment=A GUI utility for configuring buttons on graphics tablets and styli
Exec=PySetWacom
Icon=input-tablet
Terminal=false
Type=Application
Categories=Utility;Application;
""")


setup(
		author=author,
		author_email=author_email,
		classifiers=classifiers,
		description=short_desc,
		entry_points=entry_points,
		extras_require=extras_require,
		include_package_data=True,
		install_requires=install_requires,
		license=__license__,
		long_description=long_description,
		name=pypi_name,
		packages=find_packages(exclude=("tests", "doc-source")),
		project_urls=project_urls,
		py_modules=py_modules,
		python_requires=">=3.6",
		url=web,
		version=__version__,
		keywords=keywords,
		data_files=data_files,
		)
