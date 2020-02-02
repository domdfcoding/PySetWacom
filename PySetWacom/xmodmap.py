#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  xmodmap.py
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

"""
Some keys, for example bracketright (]) and bracketleft ([), need overrides in xmodmap.

If the key combination set does not enter the right key, you can lookup
any keycodes that enter that key with, for example:

	$ xmodmap -pk|grep -i bracket

	17    	0x0038 (8)	0x002a (asterisk)	0x0038 (8)	0x002a (asterisk)	0x005b (bracketleft)	0x0ac9 (trademark)
	18    	0x0039 (9)	0x0028 (parenleft)	0x0039 (9)	0x0028 (parenleft)	0x005d (bracketright)	0x00b1 (plusminus)
	34    	0x005b (bracketleft)	0x007b (braceleft)	0x005b (bracketleft)	0x007b (braceleft)	0xfe57 (dead_diaeresis)	0xfe58 (dead_abovering)
	35    	0x005d (bracketright)	0x007d (braceright)	0x005d (bracketright)	0x007d (braceright)	0xfe53 (dead_tilde)	0xfe54 (dead_macron)

From the output it can be seen that bracketleft if assigned to keycode 17 (the number 8) and keycode 34 (bracketleft).
bracketleft needs to be removed from the list for keycode 17, which can be done by setting an override.

Overrides can be set in the dictionary below, where the key is the keycode and
the value is a list of keys to set for that keycode. For example, the following
will replace bracketleft has been replaced by 8, the normal value for keycode 17.

overrides = {
		17: [8, "asterisk", 8, "asterisk", 8, "trademark"],
		}

You must ensure that the keycodes you assign to the key match the default
values, which may differ from those in the example above if your keyboard
uses a different layout.


"""

overrides = {
		17: [8, "asterisk", 8, "asterisk", 8, "trademark"],
		18: [9, "parenleft", 9, "parenleft", 9, "plusminus"],
		}


#### Source code below this line ####

import os


def apply_overrides():
	print("Applying xmodmap overrides")
	for key, value in overrides.items():
		os.system(f"xmodmap  -e 'keycode  {key} = {' '.join([str(x) for x in value])}'")


apply_overrides()
