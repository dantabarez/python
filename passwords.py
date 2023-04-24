import random
import string

#programa para generar contrasenas tipo iphone en python

def generar_contrasena(longitud):
    # caracteres = string.ascii_letters + string.digits + string.punctuation #con caracteres especiales
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud_contrasena = 20
contrasena_generada = generar_contrasena(longitud_contrasena)

# Separamos la contraseña con guiones cada 5 caracteres
contrasena_separada = '-'.join([contrasena_generada[i:i+5] for i in range(0, len(contrasena_generada), 5)])

print("La contraseña generada es: ", contrasena_separada)
