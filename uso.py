import clase

hola = clase.Grafica('real_madrid.csv')

x, y, z = hola.leer_csv()

hola.dibujar_graficas(x, y, z)