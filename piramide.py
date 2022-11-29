#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo, de altura el número introducido.
# solucion propia

numero=int(input("ingrese numero pisos de la piramide: "))
asterisco="*"

for i in range(numero):
    print(asterisco)
    asterisco=asterisco+"*"