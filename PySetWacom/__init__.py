#  !/usr/bin/env python
#
#  __init__.py
#
#  This file is part of PySetWacom
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  PySetWacom is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  PySetWacom is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# this package
from PySetWacom.__main__ import main
from PySetWacom.button import Button, get_mappings
from PySetWacom.device import Device, detect_devices
from PySetWacom.gui import GUI, CaptureKeystrokeDialog, EditMappingDialog, NewProfileValidator, app
from PySetWacom.profile import Profile, get_profiles_list, profiles_dir
from PySetWacom.tray_icon import TrayIcon
from PySetWacom.xmodmap import apply_overrides

__all__ = [
		"app",
		"apply_overrides",
		"Button",
		"CaptureKeystrokeDialog",
		"detect_devices",
		"Device",
		"EditMappingDialog",
		"get_mappings",
		"get_profiles_list",
		"GUI",
		"main",
		"NewProfileValidator",
		"Profile",
		"profiles_dir",
		"TrayIcon",
		]

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "GPLv3"
__version__ = "0.1.8"
__email__ = "dominic@davis-foster.co.uk"
