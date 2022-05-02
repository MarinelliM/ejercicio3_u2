import csv

from Registro import *

from CMenu import *

if __name__ == "__main__":
    archivo = open('mes.csv')
    reader = csv.reader(archivo, delimiter=',')
    lista = []
    for i in range(30):
        lista.append([Registro(0, 0, 0)]*24)
    for fila in reader:
        temp = int(fila[2])
        hum = int(fila[3])
        pres = int(fila[4])
        lista[int(fila[0])-1][int(fila[1])-1] = Registro(temp, hum, pres)
    archivo.close()
    print("Ingrese la opcion")
    print("1: Mostrar para cada variable el día y hora de menor y mayor valor.")
    print("2: Indicar la temperatura promedio mensual por cada hora.")
    print("3: Listar los valores de las tres variables. ")
    op = int(input("4: salir : "))
    menuopciones = Menuop(lista, op)
    menuopciones.menu()
