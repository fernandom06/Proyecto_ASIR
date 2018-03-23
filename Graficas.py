import csv
import matplotlib.pyplot as plt
from datetime import datetime
import Variables as vb

def grafica():
    # Aqui se genera la imagen con la grafica

    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')

        tiempo = []
        x = []
        y = []
        z = []
        barra = []

        for line in leido:
            tiempo.append(line[0])
            barra.append(datetime.strptime(line[0], '%H:%M:%S'))
            y.append(float(line[1]))
            z.append(float(line[2]))

    # tiempo tiene todos los valores del tiempo del csv

    # Elegir cada cuanto quieres las etiquetas en la grafica
    usuario = 10

    # for para guardar solo los tiempos que interesan
    for i in range(0, len(tiempo), usuario):
        x.append(tiempo[i])

    # Cambia el color del fondo de la figura
    # fig = plt.figure(facecolor='red')
    fig = plt.figure()
    fig.subplots_adjust(top=0.95, bottom=0.15, left=0.08, right=0.97, hspace=0.60)

    gra1 = fig.add_subplot(2, 1, 1)
    gra1.plot(tiempo, y, color=vb.color_linea)
    gra1.set_facecolor(vb.background_gr)
    # Establece donde empieza y donde acaba el eje x, con esa formula ajusta la grafica
    gra1.set_xlim(0, tiempo[len(tiempo) - 1])
    gra1.set_xticks(x)
    gra1.set_title(vb.titulo1, family="serif")
    gra1.spines['bottom'].set_color(vb.contorno)
    gra1.spines['top'].set_color(vb.contorno)
    gra1.spines['right'].set_color(vb.contorno)
    gra1.spines['left'].set_color(vb.contorno)
    gra1.tick_params(axis='both', colors=vb.label)
    plt.xticks(rotation=70)

    gra2 = fig.add_subplot(2, 1, 2)
    gra2.plot(tiempo, z, color=vb.color_linea)
    gra2.set_facecolor(vb.background_gr)
    gra2.set_xlim(0, tiempo[len(tiempo) - 1])
    gra2.set_xticks(x)
    gra2.set_title(vb.titulo2)
    gra2.spines['bottom'].set_color(vb.contorno)
    gra2.spines['top'].set_color(vb.contorno)
    gra2.spines['right'].set_color(vb.contorno)
    gra2.spines['left'].set_color(vb.contorno)
    gra2.tick_params(axis='both', colors=vb.label)

    plt.xticks(rotation=70)
    # plt.show()
    fig.set_facecolor(vb.background_gr)
    print(fig.get_facecolor())
    # Guarda el grafico con los colores especificados
    plt.savefig("grafico.png",facecolor=fig.get_facecolor())
    #plt.savefig("grafico.png")
    return barra