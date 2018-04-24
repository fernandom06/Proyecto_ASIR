# =============================================================================
#     Author: K Perkins
#     Date:   Jul 25, 2013
#     Taken From: http://programmingnotes.org/
#     File:  setup.py
#     Description: This is the cx_Freeze setup file for creating an exe program
# =============================================================================
import sys
from cx_Freeze import setup, Executable

# NOTE: you can include any other necessary external imports here aswell

executables = [Executable("Main.py", base="Win32GUI")]

build_exe_options = {
    "packages": ["wx","Graficas","Previsualizar","Variables",'numpy.core._methods', 'numpy.lib.format',"matplotlib.backends.backend_wxagg"],
    "include_files": ["barra2.png","socio2.png","player_pause.png","player_play.png"]}

setup(
    name="Proyecto",
    version="2.0",
    py_modules=["wx"],
    options={"build_exe": build_exe_options},
    executables=executables,
)
# http://programmingnotes.org/
