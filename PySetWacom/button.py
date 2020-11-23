#  !/usr/bin/env python
#
#  button.py
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

__all__ = ["Button", "get_mappings"]


class Button:
	"""
	Models a button on a tablet or stylus
	"""

	def __init__(self, id: int, mapping: str):
		"""
		:param id: The id of the button
		:param mapping: The mapping of the button
		"""

		self.id = id
		self.mapping = mapping

	@classmethod
	def from_string(cls, raw_string: str) -> Optional["Button"]:
		"""
		Create a Button object from a string

		:param raw_string:
		"""

		if raw_string.strip() == '':
			return None

		elements = (raw_string.strip('"').split('" "'))
		id = elements[0]
		mapping = elements[1]

		return cls(int(id), mapping)

	@classmethod
	def from_dict(cls, data_dict: Dict) -> "Button":
		"""
		Create a Button object from a string

		:param data_dict:
		"""

		return cls(**data_dict)

	def __dict__(self):
		return {
				"id": self.id,
				"mapping": self.mapping,
				}

	def __iter__(self):
		yield from self.__dict__().items()

	def __repr__(self):
		return f"Button({self.id} --> {self.mapping})"

	def __str__(self):
		return f"{self.id} --> {self.mapping}"


def get_mappings(device_name: str) -> List[Button]:
	"""
	Return the mappings for the device with the given name

	:param device_name:
	"""

	all_properties = xsetwacom("-s", "get", device_name, "all")

	buttons = []

	for prop in all_properties:
		if prop.startswith(f'xsetwacom set "{device_name}" "Button"'):
			button = Button.from_string(
					prop.replace(f'xsetwacom set "{device_name}" "Button"', '').rstrip('\n').strip()  # noqa: Q000
					)
			buttons.append(button)

	return list(filter(None, buttons))
