import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud_contrasena = 25

for i in range(30):
    contrasena_generada = generar_contrasena(longitud_contrasena)
    contrasena_separada = '-'.join([contrasena_generada[i:i+5] for i in range(0, len(contrasena_generada), 5)])
    print(f"{contrasena_separada}")
