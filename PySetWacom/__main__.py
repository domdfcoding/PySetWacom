#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  pysetwacom.py
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
import os
import sys
import signal
import pathlib

# 3rd party
from appdirs import user_data_dir
from pid import PidFile, PidFileAlreadyLockedError

# this package
sys.path.append("..")
from PySetWacom import TrayIcon


def main():
	pid_dir = pathlib.Path(user_data_dir("PySetWacom")) / ".pid"
	if not pid_dir.exists():
		pid_dir.mkdir()
	
	print('My PID is:', os.getpid())
	
	try:
		with PidFile(pidname="PySetWacom", piddir=str(pid_dir)) as p:
			
			# Create Tray Icon, which in turn creates GUI
			TrayIcon()
	except (BlockingIOError, PidFileAlreadyLockedError):
		other_pid = int((pid_dir / "PySetWacom.pid").read_text())
		print("PySetWacom already running")
		print('The other PID is:', other_pid)
		os.kill(other_pid, signal.SIGUSR1)


if __name__ == "__main__":
	main()
