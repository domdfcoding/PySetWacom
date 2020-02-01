#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
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

from sh import xsetwacom

from PySetWacom.button import Button


class Device:
	"""
	Models a Device such as a tablet or stylus
	"""
	
	def __init__(self, name, id, type):
		"""
		:param name: The name of the device
		:type name: str
		:param id: The id of the device
		:type id: str
		:param type:
		:type type:
		"""
		
		self.name = name
		self.id = id
		self.type = type
		self._buttons = []
	
	def add_button(self, button):
		"""
		Add the button to the device
		
		:param button:
		:type button: Button
		"""
		
		self._buttons.append(button)
	
	def add_multiple_buttons(self, button_list):
		"""
		Add multiple buttons to the device
		
		:param button_list:
		:type button_list: list of Button
		"""
		
		self._buttons += button_list
	
	@property
	def buttons(self):
		"""
		Returns the buttons of the device
		
		:rtype: list of Button
		"""
		
		return self._buttons
	
	@classmethod
	def from_string(cls, raw_string):
		"""
		Create a Device object from a string

		:param raw_string:
		:type raw_string: str

		:return:
		:rtype: Device
		"""
		
		if raw_string.strip() == '':
			return
		
		elements = raw_string.split("\t")
		
		name = elements[0].strip()
		id = elements[1].strip().replace("id: ", '')
		type = elements[2].strip().replace("type: ", '')

		return cls(name, id, type)
	
	@classmethod
	def from_dict(cls, data_dict):
		"""
		Create a Device object from a string

		:param data_dict:
		:type data_dict: dict

		:return:
		:rtype: Device
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
		for key, value in self.__dict__().items():
			yield key, value
	
	def __repr__(self):
		return f"Device({self.name}\tid: {self.id}\ttype: {self.type})"
		
	def __str__(self):
		return self.__repr__()
	
	def __eq__(self, other):
		return self.name == other.name


def detect_devices():
	"""
	Detect devices connected to this computer
	
	:return:
	:rtype: list of Device
	"""
	
	devices_list = (xsetwacom.list()).split("\n")
	
	devices_list = filter(None, [Device.from_string(device) for device in devices_list])
	
	return list(devices_list)
