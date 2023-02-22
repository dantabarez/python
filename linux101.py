import os

# Especifica la ruta de la carpeta a analizar
ruta_carpeta = "/var/log"

# Crea una lista de tuplas que contiene el nombre del archivo y la fecha de creación
lista_archivos = [(archivo, os.path.getctime(os.path.join(ruta_carpeta, archivo))) for archivo in os.listdir(ruta_carpeta)]

# Ordena la lista de tuplas por fecha de creación
lista_archivos_ordenados = sorted(lista_archivos, key=lambda x: x[1])

# Imprime los nombres de archivo ordenados por fecha de creación
for archivo in lista_archivos_ordenados:
    print(archivo[0])
