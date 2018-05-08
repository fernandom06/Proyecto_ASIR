import csv
import numpy
import json
import matplotlib.pyplot as plt
from datetime import datetime
import Variables as vb


def grafica(numero):
    # Aqui se genera la imagen con la grafica

    data = json.load(open("settings.json", encoding='utf-8'))

    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')
        letras = ["y", "z", "t", "u", "v", "w"]
        # Se crean tantas listas vacias dentro de eje_y como columnas hay
        eje_y = []
        eje_y_ticks = []
        # tiempo tiene todos los valores del tiempo del csv
        tiempo = []
        # Se crean tantas listas como columnas hay, siempre la del eje x y dinamicamente las del eje y de cada grafica,
        # dependiendo de cuantas columnas tenga el CSV
        x = []
        for i in range(len(vb.titulos)):
            letras[i] = []
            eje_y.append(letras[i])
        barra = []

        # Bucle for para guardar los valores en las listas
        for line in leido:
            tiempo.append(line[0])
            barra.append(datetime.strptime(line[0], '%H:%M:%S'))
            for i in range(len(vb.titulos)):
                eje_y[i].append(float(line[i + 1]))
    # if que en caso de que el usuario no indique el momento de salida del video se pondra por defecto el maximo
    if vb.s_salida == 0:
        vb.s_salida = len(tiempo) - 1
    # for para guardar solo los tiempos que se mostraran en las etiquetas del eje x
    for i in range(vb.s_entrada, vb.s_salida, vb.etiquetas):
        x.append(tiempo[i])

    quitar_filas = 0
    total_filas = 0
    for i in range(len(data["graficas"]["grafica"])):
        total_filas += data["graficas"]["grafica"][i]["filas"]

    # Si si que se quieren elegir las etiquetas se crean arrays con la ayuda de la libreria numpy para poder introducir
    # valores de tipo float
    if vb.c_yticks == 1:
        for j in range(len(vb.titulos)):
            eje_y_ticks.append(numpy.arange(vb.ytick_entrada_fin[j], vb.ytick_salida_fin[j], vb.ytick_salto_fin[j]))

    fig = plt.figure(figsize=(vb.w_inch, vb.h_inch))
    fig.subplots_adjust(top=0.95, bottom=0.25, left=0.18, right=0.97, hspace=0.1)

    if vb.c_titulos == 0:
        # For en el que se crean las graficas
        for i in range(vb.contador_col - 1):
            gra = plt.subplot2grid((total_filas, 1), (quitar_filas, 0), rowspan=data["graficas"]["grafica"][i]["filas"])
            quitar_filas += data["graficas"]["grafica"][i]["filas"]
            gra.plot(tiempo, eje_y[i], color=data["graficas"]["grafica"][i]["color_lineas_grafica"],
                     linewidth=data["graficas"]["grafica"][i]["pixeles_linea"])
            gra.set_facecolor(vb.background_gr)
            # Establece donde empieza y donde acaba el eje x, con ese metodo ajusta la grafica
            gra.set_xlim(vb.s_entrada, vb.s_salida)
            # If que comprueba si es la ultima grafica para colocarle las etiquetas en el eje x
            if i == vb.contador_col - 2:
                gra.set_xticks(x)
                plt.xticks(rotation=vb.angulo_gr, fontsize=data["graficas"]["grafica"][i]["tamanno_etiqueta"],
                           fontname=data["graficas"]["grafica"][i]["fuente_etiqueta"])
            gra.set_ylabel(data["graficas"]["grafica"][i]["titulo"],
                           family=data["graficas"]["grafica"][i]["fuente_titulo"],
                           color=data["graficas"]["grafica"][i]["color_titulos"],
                           size=data["graficas"]["grafica"][i]["tamanno_titulo"])
            gra.spines['bottom'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
            gra.spines['top'].set_visible(False)
            gra.spines['right'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
            gra.spines['left'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
            # si no es la ultima grafica se eliminan las marcas del eje x
            if i != vb.contador_col - 2:
                gra.tick_params(axis='both', colors=data["graficas"]["grafica"][i]["color_etiquetas"],
                                labelbottom=False, bottom=False)
            else:
                gra.tick_params(axis='both', colors=data["graficas"]["grafica"][i]["color_etiquetas"])
            gra.get_yaxis().set_label_coords(-0.1, 0.5)
            if vb.c_yticks == 1:
                gra.set_ylim(min(eje_y_ticks[i]), max(eje_y_ticks[i]))
                gra.set_yticks(eje_y_ticks[i])
            plt.yticks(fontsize=data["graficas"]["grafica"][i]["tamanno_etiqueta"],
                       fontname=data["graficas"]["grafica"][i]["fuente_etiqueta"])
    if vb.c_titulos == 1:
        # For en el que se crean las graficas
        contador_true = vb.col_checked.count(True)
        contador = 1
        for i in range(vb.contador_col - 1):
            if vb.col_checked[i]:
                gra = plt.subplot2grid((total_filas, 1), (quitar_filas, 0),
                                       rowspan=data["graficas"]["grafica"][i]["filas"])
                quitar_filas += data["graficas"]["grafica"][i]["filas"]
                gra.plot(tiempo, eje_y[i], color=data["graficas"]["grafica"][i]["color_lineas_grafica"],
                         linewidth=data["graficas"]["grafica"][i]["pixeles_linea"])
                gra.set_facecolor(vb.background_gr)
                # Establece donde empieza y donde acaba el eje x, con ese metodo ajusta la grafica
                gra.set_xlim(vb.s_entrada, vb.s_salida)
                # If que comprueba si es la ultima grafica para colocarle las etiquetas en el eje x
                if contador_true == contador:
                    gra.set_xticks(x)
                    plt.xticks(rotation=vb.angulo_gr, fontsize=data["graficas"]["grafica"][i]["tamanno_etiqueta"],
                               fontname=data["graficas"]["grafica"][i]["fuente_etiqueta"])
                gra.set_ylabel(data["graficas"]["grafica"][i]["titulo"],
                               family=data["graficas"]["grafica"][i]["fuente_titulo"],
                               color=data["graficas"]["grafica"][i]["color_titulos"],
                               size=data["graficas"]["grafica"][i]["tamanno_titulo"])
                gra.spines['bottom'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
                gra.spines['top'].set_visible(False)
                gra.spines['right'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
                gra.spines['left'].set_color(data["graficas"]["grafica"][i]["color_contorno_grafica"])
                # si no es la ultima grafica se eliminan las marcas del eje x
                if contador_true != contador:
                    gra.tick_params(axis='both', colors=data["graficas"]["grafica"][i]["color_etiquetas"],
                                    labelbottom=False, bottom=False)
                else:
                    gra.tick_params(axis='both', colors=data["graficas"]["grafica"][i]["color_etiquetas"])
                gra.get_yaxis().set_label_coords(-0.1, 0.5)
                if vb.c_yticks == 1:
                    gra.set_ylim(min(eje_y_ticks[i]), max(eje_y_ticks[i]))
                    gra.set_yticks(eje_y_ticks[i])
                plt.yticks(fontsize=data["graficas"]["grafica"][i]["tamanno_etiqueta"],
                           fontname=data["graficas"]["grafica"][i]["fuente_etiqueta"])
                contador += 1
    fig.set_facecolor(vb.background_gr)
    # Guarda el grafico con los colores especificados
    if numero == 0:
        plt.savefig("grafico.png", facecolor=fig.get_facecolor())
    else:
        plt.savefig("otra.png", facecolor=fig.get_facecolor())
    return barra
