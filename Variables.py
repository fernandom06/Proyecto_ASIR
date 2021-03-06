# Archivo que sirve para guardar los valores que no se pueden retornar con los eventos
import sys
import ctypes
import json

# Obtener la resolucion de la pantalla en la que se ejecuta el programa
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

data = json.load(open("settings.json"))

checkbox = 0

csv = ""
video = ""

# Variables de las graficas
background_gr = data["colores"]["color_fondo_grafica"]  # Color de fondo de la imagen
etiquetas = data["etiquetas"]["intervalos"]

# Responsive, variables de la ventana w=ancho h=alto
w_ant = 1920
h_ant = 1040

# Variables del reproductor
w_player = 640
h_player = 400

w_panel_player = 640
h_panel_player = 500

# Variables del logo
w_logo = 500
h_logo = 183

# Variables slider
w_slider = 640
h_slider = 24

# Variables botones
w_play = 40
h_play = 40

w_pause = 40
h_pause = 40

w_atras = 88
h_atras = 26

w_grabar = 88
h_grabar = 26

# Variables grafica
w_grafica = 830
h_grafica = 480

w_panel_grafica = 930
h_panel_grafica = 580

w_ant_grafica = 830
h_ant_grafica = 480

# Variables barra
w_barra = 4
h_barra = 350

# Variables Boton grafica
w_regrafica = 100
h_regrafica = 26

# Reproductor

back_rep = data["colores"]["color_fondo"]

contador_col = 0
c_col = 0
c_titulos = 0
titulos = []
titulos_input = []
titulos_label = []

# Posiciones: Todos los elementos

l_grafica = 25
t_grafica = 25

l_panel_grafica = 445
t_panel_grafica = 530

l_player = 0
t_player = 0

l_panel_player = 640
t_panel_player = 0

l_logo = 1350
t_logo = 0

t_slider = 420

t_play = 450

l_pause = 45
t_pause = 450

l_atras = 90
t_atras = 464

l_grabar = 185
t_grabar = 464

l_regrafica = 280
t_regrafica = 464

l_barra = 151
t_barra = 15

# Paneles para redimensionar del player
l_izq_video = -5
t_izq_video = 255

l_der_video = 5
t_der_video = 255

l_top_video = 320
t_top_video = -5

l_bottom_video = 320
t_bottom_video = 5

# Paneles para redimensionar del grafica
l_izq_grafica = -5
t_izq_grafica = 260

l_der_grafica = 5
t_der_grafica = 260

l_top_grafica = 465
t_top_grafica = 2

l_bottom_grafica = 465
t_bottom_grafica = 5

# Angulo de etiquetas

angulo_gr = data["etiquetas"]["rotacion"]

barra_tiempo = []
# Teimpo entrada y salida de video
s_entrada = 0
s_salida = len(barra_tiempo)
c_segundos = 0
c_yticks = 0
pixeles_grafica = 650
delta = (0, 0)
col_checked = []

# resize
c_resize_grafica = 0
c_resize_player = 0
c_resize_logo = 0

# Calcular las pulgadas iniciales dependiendo de la resolucion
w_inch = ancho * 8.3 / 1920
h_inch = alto * 4.8 / 1080

# yticks
ytick_label = []
ytick_entrada = []
ytick_entrada_fin = []
ytick_salida = []
ytick_salida_fin = []
ytick_salto = []
ytick_salto_fin = []


def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)
