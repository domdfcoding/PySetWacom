#  !/usr/bin/env python
#
#  profile.py
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

# stdlib
import json
import os
import pathlib
from typing import Iterator, List

# 3rd party
from platformdirs import user_data_dir

# this package
from PySetWacom.button import get_mappings
from PySetWacom.device import Device, detect_devices

__all__ = ["Profile", "get_profiles_list"]


class Profile:
	"""
	Models a Profile for mapping the buttons on one or more devices.

	:param name:
	:param devices:
	"""

	def __init__(self, name: str, devices: List[Device]):
		self.devices = self._devices = devices
		self._name = name

	@classmethod
	def new(cls, name: str) -> "Profile":
		"""
		Create a new Profile.

		:param name: The name of the profile
		"""

		devices = detect_devices()
		for device in devices:
			device.add_multiple_buttons(get_mappings(device.name))
		return cls(name, devices)

	def __dict__(self):
		return {
				"name": self._name,
				"devices": [dict(device) for device in self.devices],
				}

	def __iter__(self) -> Iterator:
		yield from self.__dict__().items()

	def save(self) -> None:
		"""
		Save the Profile.
		"""

		filename = profiles_dir / f"{self._name}.profile"

		with filename.open('w') as fp:
			json.dump(dict(self), fp, indent=4)

	@classmethod
	def load(cls, name: str) -> "Profile":
		"""
		Load a profile from file.

		:param name: The name of the profile to load
		"""

		filename = profiles_dir / f"{name}.profile"

		with filename.open('r') as fp:
			data_dict = json.load(fp)

		data_dict["devices"] = [Device.from_dict(device) for device in data_dict["devices"]]

		return cls(**data_dict)

	@property
	def name(self) -> str:
		"""
		Returns the name of the Profile.
		"""

		return self._name

	def apply(self) -> None:
		"""
		Apply the Profile with xsetwacom.
		"""

		for device in self.devices:
			for button in device.buttons:
				# print(xsetwacom(f'--set "{device.name}" Button {button.id} "{button.mapping}"'))
				# print(xsetwacom.set(device.name, button.id, button.mapping))
				# print(xsetwacom("--set", device.name, button.id, button.mapping))
				# print(f'--set "{device.name}" Button {button.id} "{button.mapping}"')
				os.system(f'xsetwacom --set "{device.name}" Button {button.id} "{button.mapping}"')


def get_profiles_list() -> List[str]:
	"""
	Returns a list of existing Profiles.
	"""

	return sorted(profile_file.stem for profile_file in profiles_dir.glob("**/*.profile"))


profiles_dir = pathlib.Path(user_data_dir("PySetWacom"))
if not profiles_dir.exists():
	profiles_dir.mkdir()
