
# Created by Srce Cde

import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("port_scanner.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Mini Port Scanner",
    options = {"build_exe": {"packages":["tkinter"], "include_files":["icon.ico", "out.txt"]}},
    version = "0.01",
    description = "Fast and Multithreaded Port Scanner",
    executables = executables
)
