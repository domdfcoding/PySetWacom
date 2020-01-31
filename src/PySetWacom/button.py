#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
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

from sh import xsetwacom


class Button:
	"""
	Models a button on a tablet or stylus
	"""
	
	def __init__(self, id, mapping):
		"""
		:param id: The id of the button
		:type id: int
		:param mapping: The mapping of the button
		:type mapping: str
		"""

		self.id = id
		self.mapping = mapping
		
	@classmethod
	def from_string(cls, raw_string):
		"""
		Create a Button object from a string
		
		:param raw_string:
		:type raw_string: str
		
		:return:
		:rtype: Button
		"""
		
		if raw_string.strip() == '':
			return
		
		elements = (raw_string.strip('"').split('" "'))
		id = elements[0]
		mapping = elements[1]
		
		return cls(id, mapping)
	
	@classmethod
	def from_dict(cls, data_dict):
		"""
		Create a Button object from a string

		:param data_dict:
		:type data_dict: dict

		:return:
		:rtype: Button
		"""
		
		return cls(**data_dict)
	
	def __dict__(self):
		return {
				"id": self.id,
				"mapping": self.mapping,
				}
	
	def __iter__(self):
		for key, value in self.__dict__().items():
			yield key, value
	
	def __repr__(self):
		return f"Button({self.id} --> {self.mapping})"
	
	def __str__(self):
		return f"{self.id} --> {self.mapping}"


def get_mappings(device_name):
	"""
	Return the mappings for the device with the given name
	
	:param device_name:
	:type device_name: str
	
	:return:
	:rtype: list of Button
	"""
	
	all_properties = xsetwacom("-s", "get", device_name, "all")
	
	buttons = []
	
	for prop in all_properties:
		if prop.startswith(f'xsetwacom set "{device_name}" "Button"'):
			button = Button.from_string(
					prop.replace(f'xsetwacom set "{device_name}" "Button"', "").rstrip("\n").strip()
					)
			buttons.append(button)
		
	return buttons
