#este programa trata de hackear un numero random que ingresas por teclado, puede tomar mas o menos tiempo depende del numero ingresado
import random
pin=int(input("ingresa pin de 6 digitos: \n"))

while True:
    pinHackeado=random.randint(0,999999)
    print("hackeando tu pin de banco", pinHackeado)
    if pin==pinHackeado:
        break

print("tu pin fue: ", pinHackeado)