======================
PySetWacom
======================

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/pysetwacom/latest?logo=read-the-docs
	:target: https://pysetwacom.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/PySetWacom/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/PySetWacom/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://github.com/domdfcoding/PySetWacom/workflows/Linux%20Tests/badge.svg
	:target: https://github.com/domdfcoding/PySetWacom/actions?query=workflow%3A%22Linux+Tests%22
	:alt: Linux Test Status

.. |requires| image:: https://requires.io/github/domdfcoding/PySetWacom/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/PySetWacom/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/PySetWacom?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/PySetWacom
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/PySetWacom
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/PySetWacom?logo=python&logoColor=white
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/PySetWacom
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/PySetWacom
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/PySetWacom
	:target: https://github.com/domdfcoding/PySetWacom/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/PySetWacom
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/PySetWacom/v0.1.8
	:target: https://github.com/domdfcoding/PySetWacom/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/PySetWacom
	:target: https://github.com/domdfcoding/PySetWacom/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/PySetWacom/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/PySetWacom/master
	:alt: pre-commit.ci status

.. end shields

A GUI utility for configuring buttons on graphics tablets and styli, using the xsetwacom utility.

Installation
----------------

Before installing ``PySetWacom`` ensure you have installed the following:

* ``xsetwacom``. This may be installed by default.
* ``PyGObject``. See https://pygobject.readthedocs.io/en/latest/ for more information and installation instructions.

	On Ubuntu you may need to install ``libgirepository1.0-dev``, ``libcairo2-dev`` and ``python3-gi``.

* ``wxPython`` (version 4.0.7 or greater). See https://wxpython.org/pages/downloads/ for more information and installation instructions.

	On Ubuntu you may also need to install ``libsdl2-2.0.0``.

Depending on your tablet model you may need to install DIGImend_. See https://digimend.github.io/ for further information, a list of supported devices, and installation instructions.

.. _DIGImend: https://digimend.github.io/


.. start installation

``PySetWacom`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install PySetWacom

.. end installation


Brief Tutorial
================

`PySetWacom` can be run from the terminal with the command

.. code-block:: bash

	$ PySetWacom

or by selecting its icon from your application menu.

AppIndicator
---------------

Once started, you should see an AppIndicator icon appear that looks like this:

.. image:: images/AppIndicator.png

You can click this icon to show the `Editor` window, switch profiles, or quit `PySetWacom`.

.. image:: images/AppIndicatorMenu.png

Editor
-------

In the `Editor` window, you can change profiles and edit the mappings for the different buttons on your tablet.

.. image:: images/Editor.png
	:width: 400

Double clicking on a button opens the `Edit Mapping` dialog, where you can type in the mapping or capture it from your keyboard.


.. image:: images/Edit_Mapping.png
	:width: 400

If there are devices in the list that you don't want to configure, or if there is a new device you want to add, you can click the `Manage Devices` button in the `Editor` window.

.. image:: images/Manage_Devices.png
	:width: 400


Further Reading
================

https://github.com/linuxwacom/xf86-input-wacom/wiki/Tablet-Configuration-1:-xsetwacom-and-xorg.conf
https://github.com/linuxwacom/xf86-input-wacom/wiki/xsetwacom
https://www.x.org/releases/current/doc/man/man4/mousedrv.4.xhtml
https://wiki.archlinux.org/index.php/Wacom_tablet
