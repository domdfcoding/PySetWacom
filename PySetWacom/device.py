#  !/usr/bin/env python
#
#  device.py
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
from typing import Dict, List, Optional

# 3rd party
from sh import xsetwacom  # type: ignore

# this package
from PySetWacom.button import Button

__all__ = ["Device", "detect_devices"]


class Device:
	"""
	Models a Device such as a tablet or stylus
	"""

	def __init__(self, name: str, id: str, type):
		"""
		:param name: The name of the device
		:param id: The id of the device
		:param type:
		"""

		self.name = name
		self.id = id
		self.type = type
		self._buttons: List[Button] = []

	def add_button(self, button: Button):
		"""
		Add the button to the device

		:param button:
		"""

		self._buttons.append(button)

	def add_multiple_buttons(self, button_list: List[Button]):
		"""
		Add multiple buttons to the device

		:param button_list:
		"""

		self._buttons += button_list

	@property
	def buttons(self) -> List[Button]:
		"""
		Returns the buttons of the device
		"""

		return self._buttons

	@classmethod
	def from_string(cls, raw_string: str) -> Optional["Device"]:
		"""
		Create a Device object from a string

		:param raw_string:
		"""

		if raw_string.strip() == '':
			return None

		elements = raw_string.split('\t')

		name = elements[0].strip()
		id = elements[1].strip().replace("id: ", '')
		type = elements[2].strip().replace("type: ", '')

		return cls(name, id, type)

	@classmethod
	def from_dict(cls, data_dict: Dict) -> "Device":
		"""
		Create a Device object from a string

		:param data_dict:
		"""

		device = cls(data_dict["name"], data_dict["id"], data_dict["type"])
		device.add_multiple_buttons([Button.from_dict(button) for button in data_dict["buttons"]])
		return device

	def __dict__(self):
		return {
				"name": self.name,
				"id": self.id,
				"type": self.type,
				"buttons": [dict(button) for button in self.buttons]
				}

	def __iter__(self):
		yield from self.__dict__().items()

	def __repr__(self):
		return f"Device({self.name}\tid: {self.id}\ttype: {self.type})"

	def __str__(self):
		return self.__repr__()

	def __eq__(self, other):
		return self.name == other.name


def detect_devices() -> List[Device]:
	"""
	Detect devices connected to this computer
	"""

	devices_list = (xsetwacom.list()).split('\n')

	devices_list = filter(None, [Device.from_string(device) for device in devices_list])

	return list(devices_list)
