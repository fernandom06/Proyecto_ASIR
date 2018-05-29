from cx_Freeze import setup, Executable

# NOTE: you can include any other necessary external imports here aswell

executables = [Executable("Main.py", base="Win32GUI")]

build_exe_options = {
    "packages": ["wx", "Graficas", "Previsualizar", "Variables", 'numpy.core._methods', 'numpy.lib.format',
                 "matplotlib.backends.backend_wxagg"],
    "include_files": ["socio2.png", "player_pause.png", "player_play.png", "settings.json", "barra-azul.png",
                      "barra-amarillo.png", "barra-blanco.png", "barra-morado.png", "barra-negro.png", "barra-rojo.png",
                      "barra-verde.png", "barra-rosa.png"]}

setup(
    name="Proyecto",
    version="5.0",
    py_modules=["wx"],
    options={"build_exe": build_exe_options},
    executables=executables,
)
