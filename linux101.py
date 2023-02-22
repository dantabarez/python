#un programa en python que lea los archivos de una carpeta, los ordene por fecha de creacion y los imprima en pantalla
import os
import datetime


# Especifica la ruta de la carpeta a analizar
ruta_carpeta = "/var/log"

# Crea una lista de tuplas que contiene el nombre del archivo y la fecha de creación
lista_archivos = [(archivo, os.path.getctime(os.path.join(ruta_carpeta, archivo))) for archivo in os.listdir(ruta_carpeta)]

# Ordena la lista de tuplas por fecha de creación
lista_archivos_ordenados = sorted(lista_archivos, key=lambda x: x[1])

# Imprime los nombres de archivo y la fecha de creación ordenados por fecha de creación
for archivo in lista_archivos_ordenados:
    fecha_creacion = datetime.datetime.fromtimestamp(archivo[1])
    print(archivo[0] + " - " + str(fecha_creacion))