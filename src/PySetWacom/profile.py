#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
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

# 3rd party
from appdirs import user_data_dir

# this package
from PySetWacom.button import get_mappings
from PySetWacom.device import detect_devices, Device


class Profile:
	"""
	Models a Profile for mapping the buttons on one or more devices
	"""
	
	def __init__(self, name, devices):
		"""
		:param name:
		:type name: str
		:param devices:
		:type devices: list of Device objects
		"""
		
		self._devices = devices
		self._name = name
	
	@classmethod
	def new(cls, name):
		"""
		Create a new Profile
		
		:param name: The name of the profile
		:type name: str
		
		:rtype: Profile
		"""
		
		devices = detect_devices()
		for device in devices:
			device.add_multiple_buttons(get_mappings(device.name))
		return cls(name, devices)
	
	def __dict__(self):
		return {
				"name": self._name,
				"devices": [dict(device) for device in self._devices],
				}
	
	def __iter__(self):
		for key, value in self.__dict__().items():
			yield key, value
	
	def save(self):
		"""
		Save the Profile
		"""
		
		filename = profiles_dir / f"{self._name}.profile"
		
		with filename.open("w") as fp:
			json.dump(dict(self), fp, indent=4)
	
	@classmethod
	def load(cls, name):
		"""
		Load a profile from file
		
		:param name: The name of the profile to load
		:type name: str
		
		:rtype: Profile
		"""
		
		filename = profiles_dir / f"{name}.profile"
		
		with filename.open("r") as fp:
			data_dict = json.load(fp)
		
		data_dict["devices"] = [Device.from_dict(device) for device in data_dict["devices"]]
		
		return cls(**data_dict)
	
	@property
	def name(self):
		"""
		Returns the name of the Profile
		
		:rtype: str
		"""
		
		return self._name
	
	@property
	def devices(self):
		"""
		Returns a list of Devices in the Profile

		:rtype: list of Device
		"""

		return self._devices

	def apply(self):
		"""
		Apply the Profile with xsetwacom
		
		:return:
		:rtype:
		"""
		
		for device in self.devices:
			for button in device.buttons:
				# print(xsetwacom(f'--set "{device.name}" Button {button.id} "{button.mapping}"'))
				# print(xsetwacom.set(device.name, button.id, button.mapping))
				# print(xsetwacom("--set", device.name, button.id, button.mapping))
				# print(f'--set "{device.name}" Button {button.id} "{button.mapping}"')
				os.system(f'xsetwacom --set "{device.name}" Button {button.id} "{button.mapping}"')

				
def get_profiles_list():
	"""
	Returns a list of existing Profiles

	:rtype:
	"""
	
	profile_files = list(profile_file.stem for profile_file in profiles_dir.glob("**/*.profile"))
	profile_files.sort()
	return profile_files


profiles_dir = pathlib.Path(user_data_dir("PySetWacom"))
if not profiles_dir.exists():
	profiles_dir.mkdir()
