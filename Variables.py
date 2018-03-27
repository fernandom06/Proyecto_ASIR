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
fuente_tit = "sans-serif"
tamanno_tit = "large"
titulo_gr = "black"

titulo1 = "Atención"
titulo2 = "Emoción"

# Reproductor

back_rep = "WHITE"

contador=0
# Posiciones: Grafica, SocioGraph y Reproductor

l_gr = 640
t_gr = 530

l_rep = 640
t_rep = 0

l_soc = 1400
t_soc = 0

barra_tiempo=[]
# Teimpo entrada y salida de video
s_entrada=0
s_salida=len(barra_tiempo)
c_segundos=1

def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)
