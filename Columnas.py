import csv
import Variables as vb

def columnas():
    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')

        primera=next(leido)
        contador=len(primera)
    return contador