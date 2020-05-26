def create_dotdesktop(version):
	# Create .desktop file
	with open("PySetWacom.desktop", "w") as desktop:
		desktop.write(f"""[Desktop Entry]
Version={version}
Name=PySetWacom
Comment=A GUI utility for configuring buttons on graphics tablets and styli
Exec=PySetWacom
Icon=input-tablet
Terminal=false
Type=Application
Categories=Utility;Application;
""")
