# La version 2.0 muestra las dos graficas con los salto de tiempo en los labels que quiere el usuario,
# aqui intentaremos que esos labels esten en otra posicion para que no se monten unos encima de otros

import csv
import matplotlib.pyplot as plt

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
usuario = 14

# for para guardar solo los tiempos que interesan
for i in range(0, len(tiempo), usuario):
    x.append(tiempo[i])

#Cambia el color del fondo de la figura
#fig = plt.figure(facecolor='red')
fig = plt.figure()
fig.subplots_adjust(top=0.96,bottom=0.15,left=0.08,right=0.97,hspace=0.47)

gra1 = fig.add_subplot(2, 1, 1)
gra1.plot(tiempo, y)
# Establece donde empieza y donde acaba el eje x, con esa formula ajusta la grafica perfectamente
gra1.set_xlim(0,x[len(x)-1])
gra1.set_xticks(x)
plt.xticks(rotation=70)

gra2 = fig.add_subplot(2, 1, 2)
gra2.plot(tiempo, z)
gra2.set_xlim(0,x[len(x)-1])
gra2.set_xticks(x)

plt.xticks(rotation=70)
#plt.show()
print(fig.get_facecolor())
# Guarda el grafico con los colores especificados
#plt.savefig("grafico.png",facecolor=fig.get_facecolor())
plt.savefig("grafico.png")
