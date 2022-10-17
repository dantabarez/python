#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
# nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
# combinando mayúsculas y minúsculas como quiera.

userName=str(input("cual es tu nombre: "))

print("el nombre original es: "+userName)

#capitalized
capUserName=userName.capitalize()

print("el nombre capitalizado es: "+capUserName)

#upper case
uppUserName=userName.upper()

print("el nombre en mayusculas es: "+uppUserName)

#lower case
lwrUserName=userName.lower()

print("el nombre en minusculas es: "+lwrUserName)