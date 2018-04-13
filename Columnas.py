import csv
import Variables as vb

def columnas():
    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')

        primera=next(leido)
        contador=len(primera)
        vb.titulos = []
        #if vb.c_col==0:
        for i in range(contador - 1):
            vb.titulos.append("Titulo")
        #vb.c_col=1
    return contador