# stdlib
import signal

# 3rd party
import wx
from pubsub import pub

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
gi.require_version('Nautilus', '3.0')

from gi.repository import Gtk
from gi.repository import AppIndicator3
from gi.repository import Notify


EVT_APPINDICATOR_BUTTON = wx.NewEventType()
myEVT_APPINDICATOR_BUTTON = wx.PyEventBinder(EVT_APPINDICATOR_BUTTON, 1)

EVT_APPINDICATOR_CHECKBOX = wx.NewEventType()
myEVT_APPINDICATOR_CHECKBOX = wx.PyEventBinder(EVT_APPINDICATOR_CHECKBOX, 1)

EVT_APPINDICATOR_RADIOBUTTON = wx.NewEventType()
myEVT_APPINDICATOR_RADIOBUTTON = wx.PyEventBinder(EVT_APPINDICATOR_RADIOBUTTON, 1)


class AppIndicatorItem:
	def __init__(
			self, parentMenu=None, id=wx.ID_SEPARATOR, text="", help_string="",
			kind=wx.ITEM_NORMAL, submenu=None, radiogroup=None):
		"""
		An AppIndicatorItem represents an item in an AppIndicator menu.
		
		:param parentMenu: Menu that the menu item belongs to. Can be None if the item is going to be added to the menu later.
		:type parentMenu: AppIndicatorMenu
		:param id: Identifier for this menu item. May be ID_SEPARATOR , in which case the given kind is ignored and taken to be ITEM_SEPARATOR instead.
		:type id: int
		:param text: Text for the menu item, as shown on the menu. See SetItemLabel for more info.
		:type text: str
		:param help_string: Optional help string that will be shown on the status bar.
		:type help_string: str
		:param kind: May be ITEM_SEPARATOR , ITEM_NORMAL , ITEM_CHECK or ITEM_RADIO .
		:type kind: wx.ItemKind
		:param submenu: If not None, indicates that the menu item is a submenu.
		:type submenu: AppIndicatorMenu
		:param radiogroup:
		:type radiogroup: AppIndicatorItem
		"""
		
		self._id = id
		self._label = text
		self._help_string = help_string
		self._kind = kind
		self._text = text
		
		if kind == wx.ITEM_SEPARATOR:
			self._gtkitem = Gtk.SeparatorMenuItem()
		elif kind == wx.ITEM_CHECK:
			self._gtkitem = Gtk.CheckMenuItem(label=text, use_underline=False)
			self._gtkitem.set_active(False)
		elif kind == wx.ITEM_RADIO:
			if radiogroup:
				self._gtkitem = Gtk.RadioMenuItem(group=radiogroup._gtkitem, label=text, use_underline=False)
			else:
				self._gtkitem = Gtk.RadioMenuItem(label=text, use_underline=False)
			self._gtkitem.set_active(False)
		else:
			self._gtkitem = Gtk.MenuItem(label=text, use_underline=False)
			if submenu:
				self._gtkitem.set_submenu(submenu._gtk_menu)
			
	# 	self._gtkitem.connect('activate', self.on_click)
	#
	# def on_click(self, source):
	# 	pass
	
	def Check(self, check=True):
		"""
		Checks or unchecks the menu item.
		
		Note that this only works when the item is already appended to a menu.
		
		:type check: book
		"""
		
		self._gtkitem.set_active(check)
		
	def Enable(self, enable=True):
		"""
		Enables or disables the menu item.
		
		:type enable: bool
		"""
		
		self._gtkitem.set_sensitive(enable)

	def GetHelp(self):
		"""
		Returns the help string associated with the menu item.
		
		:rtype: str
		"""
		
		return self._help_string

	def GetId(self):
		"""
		Returns the menu item identifier.
		
		:rtype: int
		"""
		
		return self._id

	def GetLabel(self):
		"""
		Returns the text associated with the menu item
		
		:rtype: str
		"""
		
		return self._text

	def GetKind(self):
		"""
		Returns the item kind, one of wxITEM_SEPARATOR, wxITEM_NORMAL,
		wxITEM_CHECK or wxITEM_RADIO.
		
		:rtype: wx.ItemKind
		"""
		
		return self._kind

	def GetMenu(self):
		"""
		Returns the menu this menu item is in, or NULL if this menu item is
		not attached.
		"""
		# TODO
		return Menu

	def GetSubMenu(self):
		"""
		Returns the submenu associated with the menu item, or NULL if there
		isn't one.
		"""
		# TODO
		return Menu

	def IsCheck(self):
		"""
		Returns true if the item is a check item.
		
		:rtype: bool
		"""
		
		return self._kind == wx.ITEM_CHECK

	def IsCheckable(self):
		"""
		Returns True if the item is checkable.

		Notice that the radio buttons are considered to be checkable as well,
		so this method returns True for them too. Use IsCheck if you want to
		test for the check items only.

		:rtype: bool
		"""
		
		return self._kind in {wx.ITEM_CHECK, wx.ITEM_RADIO}

	def IsChecked(self):
		"""
		Returns true if the item is checked.
		
		:rtype: bool
		"""
		
		return self._gtkitem.get_active()

	def IsEnabled(self):
		"""
		Returns true if the item is enabled.
		
		:rtype: bool
		"""
		
		return self._gtkitem.is_sensitive()

	def IsRadio(self):
		"""
		Returns true if the item is a radio button.
		
		:rtype: bool
		"""
		
		return self._kind == wx.ITEM_RADIO

	def IsSeparator(self):
		"""
		Returns true if the item is a separator.
		
		:rtype: bool
		"""
		
		return self._kind == wx.ITEM_SEPARATOR

	def IsSubMenu(self):
		"""
		IsSubMenu() -> bool
		
		Returns true if the item is a submenu.
		"""
		# TODO
		return False

	def SetHelp(self, help_string):
		"""
		SetHelp(help_string)
		
		Sets the help string.
		"""
		# TODO
		pass

	def SetItemLabel(self, label):
		"""
		Sets the label associated with the menu item.
		
		:type label: str
		"""

		self._gtkitem.set_label(label)

	def SetMenu(self, menu):
		"""
		SetMenu(menu)
		
		Sets the parent menu which will contain this menu item.
		"""
		# TODO
		pass

	def SetSubMenu(self, menu):
		"""
		Sets the submenu of this menu item.
		
		:param menu:
		:type menu: AppIndicatorMenu
		"""
		
		self._gtkitem.set_submenu(menu._gtk_menu)
		
	
	@property
	def Enabled(self):
		return self.IsEnabled()
		
	@Enabled.setter
	def Enabled(self, value):
		self.Enable(value)
		
	@property
	def Help(self):
		return self.GetHelp()
	
	@Help.setter
	def Help(self, value):
		self.SetHelp(value)
		
	@property
	def Id(self):
		return self.GetId()
		
	@property
	def ItemLabel(self):
		return self.GetLabel()
	
	@ItemLabel.setter
	def ItemLabel(self, value):
		self.SetItemLabel(value)
		
	@property
	def ItemLabelText(self):
		return self.GetLabel()
	
	@property
	def Kind(self):
		return self.GetKind()
		
	@property
	def Menu(self):
		return self.GetMenu()
	
	@Menu.setter
	def Menu(self, value):
		self.SetMenu(value)
		
	@property
	def SubMenu(self):
		return self.GetSubMenu()
	
	@SubMenu.setter
	def SubMenu(self, value):
		self.SetSubMenu(value)


class AppIndicator:
	def __init__(self, id, icon_name, category):
		"""
		Constructs an AppIndicator object.
	
		An AppIndicator is a n icon with a popup (or pull down) menu with a list
		of items, one of which may be selected before the menu goes away
		(clicking elsewhere dismisses the menu).
		"""
		
		self._menu = AppIndicatorMenu()
		
		self._indicator = AppIndicator3.Indicator.new(id, icon_name, category)
		
		
		self._indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
		self._indicator.set_menu(self._menu._gtk_menu)
		
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		Notify.init(id)
		
		

	def Show(self):
		Gtk.main()
	

class AppIndicatorMenu:
	def __init__(self):

		self._gtk_menu_items = []
		self._gtk_menu = Gtk.Menu()

	def Append(self, id=wx.ID_ANY, item="", help_string="", kind=wx.ITEM_NORMAL, radiogroup=None):
		"""
		Adds a menu item.
		
		:param id: The menu command identifier. See Window IDs for more information about IDs (same considerations apply to both window and menu item IDs).
		:type id: int
		:param item: The string to appear on the menu item. See wx.MenuItem.SetItemLabel for more details.
		:type item: str
		:param help_string: An optional help string associated with the item. By default, the handler for the wxEVT_MENU_HIGHLIGHT event displays this string in the status line.
		:type help_string: str
		:param kind: May be ITEM_SEPARATOR , ITEM_NORMAL , ITEM_CHECK or ITEM_RADIO .
		:type kind: wx.ItemKind
		:param radiogroup:
		:type radiogroup:
		
		:rtype: AppIndicatorItem
		"""
		
		item = AppIndicatorItem(self, id, item, help_string, kind, radiogroup=radiogroup)
		self.AppendMenuItem(item)
		
		return item
	
	def AppendMenuItem(self, menuItem):
		"""
		Adds a menu item object.
		
		:param menuItem:
		:type menuItem:
		"""
		
		self._gtk_menu_items.append(menuItem)
		self._gtk_menu.append(menuItem._gtkitem)
		self._gtk_menu.show_all()
		menuItem._gtkitem.connect('activate', self.on_item_activated)
	
	def on_item_activated(self, source):
		
		# Find the AppIndicatorItem object that contains the item that was activated
		for item in self._gtk_menu_items:
			if item._gtkitem == source:
				pub.sendMessage("menu_item_activated", item=item)
				break
		
	def AppendCheckItem(self, id, item, help_string=None):
		"""
		Adds a checkable item to the end of the menu.
		
		:param id:
		:type id: int
		:param item:
		:type item: str
		:param help_string:
		:type help_string: str
		
		:return:
		:rtype: AppIndicatorItem
		"""
		
		return self.Append(id, item, help_string, kind=wx.ITEM_CHECK)
		
	def AppendRadioItem(self, id, item, help=None, group=None):
		"""
		Adds a radio item to the end of the menu.
		
		:param id:
		:type id: int
		:param item:
		:type item: str
		:param help:
		:type help: str
		:param group:
		:type group: AppIndicatorItem
		
		:return:
		:rtype: AppIndicatorItem
		"""

		# TODO: add to group when added to menu
		return self.Append(id, item, help, kind=wx.ITEM_RADIO, radiogroup=group)
	
	def AppendSeparator(self):
		"""
		Adds a separator to the end of the menu.

		:return:
		:rtype: AppIndicatorItem
		"""
		
		return self.Append(id=wx.ID_ANY, kind=wx.ITEM_SEPARATOR)
	
	def AppendSubMenu(self, submenu, text, help_string=None):
		"""
		Adds the given submenu to this menu.

		:param submenu:
		:type submenu:
		:param text:
		:type text:
		:param help_string:
		:type help_string:
		:return:
		:rtype:
		"""
		
		item = AppIndicatorItem(self, text=text, help_string=help_string, submenu=submenu)
		self.AppendMenuItem(item)
		
		return item
	
	def Check(self, id, check):
		"""
		Check(id, check)

		Checks or unchecks the menu item.
		
		:param id: The menu item identifier.
		:type id: int
		:param check: If True, the item will be checked, otherwise it will be unchecked.
		:type check: bool
		"""
		
		for item in self._gtk_menu_items:
			if item.id == id:
				item.Check(check)
	
	def Delete(self, *__args):
		"""
		Delete(id) -> bool
		Delete(item) -> bool

		Deletes the menu item from the menu.
		"""
		return False

	def DestroyItem(self, *__args):
		"""
		DestroyItem(id) -> bool
		DestroyItem(item) -> bool
		
		Deletes the menu item from the menu.
		"""
		return False

	def Enable(self, id, enable):
		"""
		Enable(id, enable)
		
		Enables or disables (greys out) a menu item.
		
		:param id: The menu item identifier.
		:type id: int
		:param enable: If True, the item will be enabled, otherwise it will be unenabled.
		:type enable: bool
		"""
		
		for item in self._gtk_menu_items:
			if item.id == id:
				item.Enable(enable)

	def FindChildItem(self, id):
		"""
		FindChildItem(id) -> (MenuItem, pos)
		
		Finds the menu item object associated with the given menu item
		identifier and, optionally, the position of the item in the menu.
		
		:param id: The identifier of the menu item to find.
		:type id: int
		
		:return:
		:rtype:
		"""
		
		for index, item in enumerate(self._gtk_menu_items):
			if item.id == id:
				return item, index

	def FindItem(self, itemString):
		"""
		FindItem(itemString) -> int
		FindItem(id) -> (MenuItem, menu)
		
		Finds the menu id for a menu item string.
		
		:param itemString: Menu item string to find.
		:type itemString: str
		
		:return: Menu item identifier, or wx.NOT_FOUND if none is found.
		:rtype: int
		"""
		
		for index, item in enumerate(self._gtk_menu_items):
			if item.label == itemString:
				return item.id
		
		return wx.NOT_FOUND
		
	def FindItemById(self, id):
		"""
		Finds the menu item object associated with the given menu item
		identifier.
		
		:param id: Menu item identifier.
		:type id: int
		
		:return:
		:rtype:
		"""
		
		for item in self._gtk_menu_items:
			if item.id == id:
				return item

	def FindItemByPosition(self, position):
		"""
		FindItemByPosition(position) -> MenuItem
		
		Returns the wxMenuItem given a position in the menu.
		
		:param position:
		:type position: int
		
		:return:
		:rtype:
		"""
		
		for index, item in enumerate(self._gtk_menu_items):
			if index == position:
				return item

	def GetHelpString(self, id):
		"""
		GetHelpString(id) -> String
		
		Returns the help string associated with a menu item.
		
		:param id: The menu item identifier.
		:type id: int
		
		:return: The help string, or the empty string if there is no help string or the item was not found.
		:rtype: str
		"""
		
		return self.FindItemById(id).GetHelp()

	def GetInvokingWindow(self):
		""" GetInvokingWindow() -> Window """
		# TODo
		return Window

	def GetLabel(self, id):
		"""
		GetLabel(id) -> String
		
		Returns a menu item label.
		
		:param id: The menu item identifier.
		:type id: int
		
		:return: The item label, or the empty string if the item was not found.
		:rtype: str
		"""

		return self.FindItemById(id).GetLabel()

	def GetMenuItemCount(self):
		"""
		GetMenuItemCount() -> size_t
		
		Returns the number of items in the menu.
		
		:rtype: int
		"""
		
		return len(self._gtk_menu_items)

	def GetMenuItems(self):
		"""
		GetMenuItems() -> MenuItemList
		
		Returns the list of items in the menu.
		"""
		
		return self._gtk_menu_items

	def GetParent(self):
		""" GetParent() -> Menu """
		# TODO
		return Menu

	def GetStyle(self):
		""" GetStyle() -> long """
		# TODo
		return 0

	def GetWindow(self):
		""" GetWindow() -> Window """
		return Window

	def Insert(self, pos, *__args):
		"""
		Insert(pos, menuItem) -> MenuItem
		Insert(pos, id, item=EmptyString, help_string=EmptyString, kind=ITEM_NORMAL) -> MenuItem
		Insert(pos, id, text, submenu, help=EmptyString) -> MenuItem
		
		Inserts the given item before the position pos.
		"""
		return MenuItem

	def InsertCheckItem(self, pos, id, item, help_string=None):
		"""
		InsertCheckItem(pos, id, item, help_string=EmptyString) -> MenuItem
		
		Inserts a checkable item at the given position.
		"""
		return MenuItem

	def InsertItem(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def InsertMenu(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def InsertRadioItem(self, pos, id, item, help_string=None):
		"""
		InsertRadioItem(pos, id, item, help_string=EmptyString) -> MenuItem
		
		Inserts a radio item at the given position.
		"""
		return MenuItem

	def InsertSeparator(self, pos):
		"""
		InsertSeparator(pos) -> MenuItem
		
		Inserts a separator at the given position.
		"""
		return MenuItem

	def IsAttached(self):
		""" IsAttached() -> bool """
		return False

	def IsChecked(self, id):
		"""
		IsChecked(id) -> bool
		
		Determines whether a menu item is checked.
		"""
		return False

	def IsEnabled(self, id):
		"""
		IsEnabled(id) -> bool
		
		Determines whether a menu item is enabled.
		"""
		return False

	def Prepend(self, *__args):
		"""
		Prepend(menuItem) -> MenuItem
		Prepend(id, item=EmptyString, help_string=EmptyString, kind=ITEM_NORMAL) -> MenuItem
		Prepend(id, text, submenu, help=EmptyString) -> MenuItem
		
		Inserts the given item at position 0, i.e. before all the other
		existing items.
		"""
		return MenuItem

	def PrependCheckItem(self, id, item, help_string=None):
		"""
		PrependCheckItem(id, item, help_string=EmptyString) -> MenuItem
		
		Inserts a checkable item at position 0.
		"""
		return MenuItem

	def PrependItem(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def PrependMenu(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def PrependRadioItem(self, id, item, help_string=None):
		"""
		PrependRadioItem(id, item, help_string=EmptyString) -> MenuItem
		
		Inserts a radio item at position 0.
		"""
		return MenuItem

	def PrependSeparator(self):
		"""
		PrependSeparator() -> MenuItem
		
		Inserts a separator at position 0.
		"""
		return MenuItem

	def Remove(self, *__args):
		"""
		Remove(id) -> MenuItem
		Remove(item) -> MenuItem
		
		Removes the menu item from the menu but doesn't delete the associated
		C++ object.
		"""
		return MenuItem

	def RemoveItem(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def RemoveMenu(*args, **kw): # reliably restored by inspect
		# no doc
		pass

	def SetHelpString(self, id, help_string):
		"""
		SetHelpString(id, help_string)
		
		Sets an item's help string.
		"""
		pass

	def SetInvokingWindow(self, win):
		""" SetInvokingWindow(win) """
		pass

	def SetLabel(self, id, label):
		"""
		SetLabel(id, label)
		
		Sets the label of a menu item.
		"""
		pass

	def SetParent(self, parent):
		""" SetParent(parent) """
		pass

	def SetTitle(self, title):
		"""
		SetTitle(title)
		
		Sets the title of the menu.
		"""
		pass

	def TryAfter(self, *args, **kwargs):
		pass

	def TryBefore(self, *args, **kwargs):
		pass

	def UpdateUI(self, source=None):
		"""
		UpdateUI(source=None)
		
		Sends events to source (or owning window if NULL) to update the menu
		UI.
		"""
		pass

	InvokingWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetInvokingWindow() -> Window"""

	MenuItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetMenuItemCount() -> size_t

Returns the number of items in the menu."""

	MenuItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetMenuItems() -> MenuItemList

Returns the list of items in the menu."""

	Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetParent() -> Menu"""

	Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetStyle() -> long"""

	Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetTitle() -> String

Returns the title of the menu."""

	Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
	"""GetWindow() -> Window"""

