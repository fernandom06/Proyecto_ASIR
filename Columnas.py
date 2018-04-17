import csv
import Variables as vb


def columnas():
    with open(vb.csv) as fichero:
        leido = csv.reader(fichero, delimiter=';')

        # Se lee la primera linea del CSV para ver cuantas columnas tiene
        primera = next(leido)
        contador = len(primera)
        vb.titulos = []
        for i in range(contador - 1):
            vb.titulos.append(f"Titulo {i+1}")
    return contador
