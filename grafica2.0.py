import csv
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

with open("real_madrid.csv") as fichero:
    leido = csv.reader(fichero, delimiter=';')

    tiempo = []
    x = []
    y = []
    z = []

    for line in leido:
        tiempo.append(line[0])
        y.append(float(line[1]))
        z.append(float(line[2]))

# tiempo tiene todos los valores del tiempo del csv
print(tiempo)
print(len(tiempo))

# Elegir cada cuanto quieres las etiquetas en la grafica
usuario = 10

# for para guardar solo los tiempos que interesan
for i in range(0, len(tiempo), usuario):
    x.append(tiempo[i])

print(x)

# la variable array tienen el numero de posiciones
array = []

for i in range(0, len(x)):
    array.append(i)

array = np.array(array)
print(array)

fig = plt.figure()
gra1 = fig.add_subplot(2, 1, 1)
gra1.plot(tiempo, y)

# Establece donde empieza y donde acaba el eje x, con esa formula ajusta la grafica perfectamente
gra1.set_xlim(0,x[len(x)-1])

gra1.set_xticks(x)
#gra1.xaxis.set_ticks(start,end,10)

gra2 = fig.add_subplot(2, 1, 2)
gra2.plot(tiempo, z)
gra2.set_xticks(x)
#plt.locator_params(axis='x', nticks=10)

plt.show()
#plt.savefig("grafico.png")
