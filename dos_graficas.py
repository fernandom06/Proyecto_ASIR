import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open("real_madrid.csv") as fichero:
    leido = csv.reader(fichero, delimiter=';')

    next(leido)
    x = []
    y = []
    z = []

    for line in leido:
        x.append(datetime.strptime(line[0], '%H:%M:%S').time())
        y.append(float(line[1]))
        z.append(float(line[2]))

# Crear las dos subfiguras
fig = plt.figure()
gra1 = fig.add_subplot(2, 1, 1)
gra1.plot(x, y)
gra2 = fig.add_subplot(2, 1, 2)
gra2.plot(x, z)

#plt.show()
plt.savefig("grafico.png")
