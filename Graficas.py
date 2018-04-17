import csv
import matplotlib.pyplot as plt
from datetime import datetime
import Variables as vb


def grafica():
    # Aqui se genera la imagen con la grafica

    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')
        letras=["y","z","t","u","v","w"]
        eje_y=[]
        # tiempo tiene todos los valores del tiempo del csv
        tiempo = []
        # Se crean tantas listas como columnas hay, siempre la del eje x y dinamicamente las del eje y de cada grafica,
        # dependiendo de cuantas columnas tenga el CSV
        x = []
        for i in range(len(vb.titulos)):
            letras[i]=[]
            eje_y.append(letras[i])
        barra = []

        # Bucle for para guardar los valores en las listas
        for line in leido:
            tiempo.append(line[0])
            barra.append(datetime.strptime(line[0], '%H:%M:%S'))
            for i in range(len(vb.titulos)):
                eje_y[i].append(float(line[i+1]))

    # if que en caso de que el usuario no indique el momento de salida del video se pondra por defecto el maximo
    if vb.s_salida == 0:
        vb.s_salida = len(tiempo)
    # for para guardar solo los tiempos que se mostraran en las etiquetas del eje x
    for i in range(vb.s_entrada, vb.s_salida, vb.etiquetas):
        x.append(tiempo[i])

    fig = plt.figure(figsize=(8.3,4.8))
    fig.subplots_adjust(top=0.95, bottom=0.15, left=0.18, right=0.97, hspace=0.1)

    # For en el que se crean las graficas
    for i in range(len(vb.titulos_input)):
        gra = fig.add_subplot(len(vb.titulos_input), 1, i + 1)
        gra.plot(tiempo, eje_y[i], color=vb.color_linea, linewidth=vb.grosor)
        gra.set_facecolor(vb.background_gr)
        # Establece donde empieza y donde acaba el eje x, con ese metodo ajusta la grafica
        gra.set_xlim(vb.s_entrada, vb.s_salida)
        # If que comprueba si es la ultima grafica para colocarle las etiquetas en el eje x
        if i == len(vb.titulos_input) - 1:
            gra.set_xticks(x)
            plt.xticks(rotation=vb.angulo_gr, fontsize=vb.tamanno_label, fontname=vb.fuente_label)
        gra.set_ylabel(vb.titulos[i], family=vb.fuente_tit, color=vb.titulo_gr, size=vb.tamanno_tit)
        gra.spines['bottom'].set_color(vb.contorno)
        gra.spines['top'].set_visible(False)
        gra.spines['right'].set_color(vb.contorno)
        gra.spines['left'].set_color(vb.contorno)
        # si no es la ultima grafica se eliminan las marcas del eje x
        if i != len(vb.titulos_input) - 1:
            gra.tick_params(axis='both', colors=vb.label, labelbottom="off", bottom='off')
        else:
            gra.tick_params(axis='both', colors=vb.label)
        gra.get_yaxis().set_label_coords(-0.1, 0.5)
        plt.yticks(fontsize=vb.tamanno_label, fontname=vb.fuente_label)


    fig.set_facecolor(vb.background_gr)
    # Guarda el grafico con los colores especificados
    plt.savefig("grafico.png", facecolor=fig.get_facecolor())
    return barra
