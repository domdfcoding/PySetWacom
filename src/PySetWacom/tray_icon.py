#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  tray_icon.py
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
import sys

# 3rd party
from pubsub import pub
from domdf_python_tools.doctools import is_documented_by, append_docstring_from

# this package
from PySetWacom.AppIndicator import AppIndicatorItem, AppIndicator, AppIndicatorMenu, Gtk, AppIndicator3, Notify
from PySetWacom.gui import app
from PySetWacom.profile import get_profiles_list, Profile


class TrayIcon(AppIndicator):
	def __init__(self):
		AppIndicator.__init__(
				self, "PySetWacom-tray", "input-tablet",
				AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
				)

		self.profiles = get_profiles_list()
		
		self.build_menu()

		# Create pubsub receiver to listen for menu options being activated
		pub.subscribe(self.menu_item_activated, "menu_item_activated")

		# Create pubsub receiver to listen for GUI changing the Profile
		pub.subscribe(self.gui_changed_profile, "gui_changed_profile")

		# Create pubsub receiver to listen for GUI creating new Profile
		pub.subscribe(self.new_profile_created, "new_profile_created")
		
		# Create pubsub receiver to listen for GUI requesting exit
		pub.subscribe(self.quit, "quit")

		# GUI App
		self.app = app(0)
		self.app.MainLoop()
		
		self.Show()
	
	def new_profile_created(self, selected_profile):
		# Rebuild Menu
		self.profiles = get_profiles_list()
		print("##########")
		print(self.profiles)
		self.build_profiles_menu()
		self.menu_item_profile.SetSubMenu(self._profiles_submenu)
	
	def gui_changed_profile(self, selected_profile):
		print(f"GUI Changed Profile To {selected_profile}")
		for profile in self.profile_menu_items:
			if profile.GetLabel() == selected_profile:
				print("Selecting profile: "+ selected_profile)
				profile.Check(True)
	
	def menu_item_activated(self, item):
		"""
		Handler for menu item being selected.

		:param item:
		:type item: AppIndicatorItem

		:return:
		:rtype:
		"""
		
		# print(f"Item = {item}")
		label = item.GetLabel()
		# print(f"Label = {label}")
		
		if label == "Quit":
			self.quit()
		
		elif label == "Show":
			self.show()
		
		elif label in self.profiles:
			if item.IsChecked():
				self.select_profile(label)
		
	def build_profiles_menu(self):
		self._profiles_submenu = AppIndicatorMenu()
		first_radioitem = self._profiles_submenu.AppendRadioItem(-1, self.profiles[0], None)
		self.profile_menu_items = [first_radioitem]
		
		for profile in self.profiles[1:]:
			item = self._profiles_submenu.AppendRadioItem(-1, profile, group=first_radioitem)
			self.profile_menu_items.append(item)
		
	def build_menu(self):
		item_show = self._menu.Append(item="Show")
		self.build_profiles_menu()
		self.menu_item_profile = self._menu.AppendSubMenu(self._profiles_submenu, 'Select Profile')
		item_quit = self._menu.Append(item="Quit")
		
	def quit(self):
		"""
		Exit the application
		:return:
		:rtype:
		"""
		
		Notify.uninit()
		Gtk.main_quit()
		self.app.Destroy()
		sys.exit(0)
	
	def show(self):
		"""
		Show the PySetWacom GUI
		
		:return:
		:rtype:
		"""
		
		print("Show")
		self.app.Show()
	
	@staticmethod
	def select_profile(profile_name):
		"""
		Select the Profile with the given name
		
		:param profile_name:
		:type profile_name:
		
		:return:
		:rtype:
		"""
		
		print(f"Profile = {profile_name}")
		profile = Profile.load(profile_name)
		profile.apply()
		pub.sendMessage("tray_changed_profile", selected_profile=profile_name)
