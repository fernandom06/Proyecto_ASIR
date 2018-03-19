import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Ejemplo de uso en uso.py

class Grafica:
    def __init__(self, archivo, delimitador=';'):
        # De momento suponemos que se tienen 3 campos
        self.archivo = archivo
        # self.campos=campos
        self.delimitador = delimitador

    def leer_csv(self):
        with open(self.archivo) as fichero:
            leido = csv.reader(fichero, delimiter=self.delimitador)
            x, y, z=self.guardar_datos(leido)
            return x, y, z

    def guardar_datos(self, archivo_leido):
        x = []
        y = []
        z = []
        for line in archivo_leido:
            x.append(datetime.strptime(line[0], '%H:%M:%S'))
            y.append(float(line[1]))
            z.append(float(line[2]))
        return x, y, z

    def dibujar_graficas(self, x, y, z):
        fig1 = plt.figure()
        fig2 = plt.figure()
        gra1 = fig1.add_subplot(111)
        gra2 = fig2.add_subplot(111)

        gra1.plot(x, y)
        gra2.plot(x, z)

        plt.show()
