

from PySetWacom.button import Button, get_mappings
from PySetWacom.device import Device, detect_devices
from PySetWacom.gui import GUI, CaptureKeystrokeDialog, EditMappingDialog, app, NewProfileValidator
from PySetWacom.profile import Profile, get_profiles_list, profiles_dir
from PySetWacom.tray_icon import TrayIcon
from PySetWacom.xmodmap import apply_overrides
from PySetWacom.__main__ import main


__all__ = [
		"Button", "get_mappings",
		"Device", "detect_devices",
		"GUI", "CaptureKeystrokeDialog", "EditMappingDialog", "app", "NewProfileValidator",
		"Profile", "get_profiles_list", "profiles_dir",
		"TrayIcon",
		"apply_overrides",
		"main"
		]

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "GPLv3"
__version__ = "0.1.6"
__email__ = "dominic@davis-foster.co.uk"