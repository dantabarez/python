#este programa permite dividir en bloques un archivo de texto plano para que sea digerible para chatgpt 3.5 y 4
def separar_texto_en_bloques(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        texto_completo = archivo.read()
        palabras = texto_completo.split()

        bloques = []
        bloque_actual = []

        for palabra in palabras:
            if len(' '.join(bloque_actual + [palabra])) <= 4000:
                bloque_actual.append(palabra)
            else:
                bloques.append(' '.join(bloque_actual))
                bloque_actual = [palabra]

        bloques.append(' '.join(bloque_actual))

        return bloques

#los archivos de origen y destino deben estar en la misma ruta del script
ruta_archivo = 'texto.txt'
bloques = separar_texto_en_bloques(ruta_archivo)

with open('bloques.txt', 'w') as archivo_salida:
    for bloque in bloques:
        archivo_salida.write(bloque + '\n')
