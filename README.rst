**********************
PySetWacom
**********************

.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs|
	* - Tests
	  - |travis| |requires| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Other
	  - |license| |language| |commits-since| |commits-latest| |maintained| 
	
.. |docs| image:: https://readthedocs.org/projects/pysetwacom/badge/?version=latest
	:target: https://pysetwacom.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/PySetWacom/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/PySetWacom
	:alt: Travis Build Status
	
.. |requires| image:: https://requires.io/github/domdfcoding/PySetWacom/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/PySetWacom/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/PySetWacom
	:target: https://www.codefactor.io/repository/github/domdfcoding/PySetWacom
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/PySetWacom.svg
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/PySetWacom.svg
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/PySetWacom
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/PySetWacom
	:target: https://pypi.org/project/PySetWacom/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/PySetWacom
	:alt: License
	:target: https://github.com/domdfcoding/PySetWacom/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/PySetWacom
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/PySetWacom/v0.1.6
	:target: https://github.com/domdfcoding/PySetWacom/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/PySetWacom
	:target: https://github.com/domdfcoding/PySetWacom/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields

A GUI utility for configuring buttons on graphics tablets and styli, using the xsetwacom utility.

Dependencies
=============

xsetwacom must be installed for this program to function. Python dependencies include:

.. code-block:: bash

	appdirs>=1.4.3
	domdf_python_tools>=0.1.17
	domdf_wxpython_tools>=0.2.0
	Pypubsub>=4.0.3
	pid>=2.2.5
	sh>=1.12.14

These can all be installed using ``pip``.

wxPython (4.0.7 or greater) must also be installed. See https://wxpython.org/pages/downloads/ for more information and installation instructions.

PyGObject must also be installed. See https://pygobject.readthedocs.io/en/latest/ for more information and installation instructions.


Depending on your tablet model you may need to install DIGImend_. See https://digimend.github.io/ for further information, a list of supported devices, and installation instructions.

.. _DIGImend: https://digimend.github.io/

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

