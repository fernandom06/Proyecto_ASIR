# Archivo que sirve para guardar los valores que no se pueden retornar con los eventos
import sys

numero = 1

csv = "real_madrid.csv"
video = "madrid.mp4"

# Variables de las graficas
color_linea = "blue"  # Color de la lina de la grafica
contorno = "black"  # color del contorno que rodea a la grafica
background_gr = "white"  # Color de fondo de la imagen
label = "black"  # Color de las etiquetas
etiquetas = 30
grosor = 1.5
fuente_tit = "Arial"
tamanno_tit = "large"
titulo_gr = "black"


# Responsive, variables de la ventana w=ancho h=alto
w_ant=1920
h_ant=1040

# Variables del reproductor
w_player=640
h_player=400

# Variables del logo
w_logo=431
h_logo=183

# Variables slider
w_slider=640

#Variables botones
w_play=40
h_play=40

w_pause=40
h_pause=40

w_atras=88
h_atras=26

w_grabar=88
h_grabar=26

# Variables grafica
w_grafica=640
h_grafica=480
w_otra=640
h_otra=480

# Variables barra
w_barra=4
h_barra=382


titulo1 = "Atención"
titulo2 = "Emoción"

# Reproductor

back_rep = "WHITE"

contador_col = 0
c_col = 0
c_titulos = 0
titulos = []
titulos_input = []
titulos_label = []
# for i in range(contador_col - 1):
#    titulos.append("hola")

# Posiciones: Todos los elementos

l_gr = 640
t_gr = 530

l_rep = 640
t_rep = 0

l_soc = 1400
t_soc = 0

t_slider=420

t_play=450

l_pause=45
t_pause=450

l_atras=90
t_atras=464

l_grabar=185
t_grabar=464

l_barra=116
t_barra=30

# Angulo de etiquetas

angulo_gr = 70
fuente_label = "arial"
tamanno_label = "medium"

barra_tiempo = []
# Teimpo entrada y salida de video
s_entrada = 0
s_salida = len(barra_tiempo)
c_segundos = 0


def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)
