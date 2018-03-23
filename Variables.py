#Archivo que sirve para guardar los valores que no se pueden retornar con los eventos
import sys

csv="real_madrid.csv"
video="madrid.mp4"
# Variables de las graficas
color_linea1="blue" # Color de la lina de la grafica
color_linea2="blue"
contorno1="black" # color del contorno que rodea a la grafica
contorno2="black"
background_gr="white" # Color de fondo de la imagen
background1="white" # color de fondo de la primera grafica (de momento no las utilizo)
background2="white"
label1="black" # Color de las etiquetas
label2="black"
titulo1="Atención"
titulo2="Emoción"

#Reproductor

background_rep="WHITE"


def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)
