#en este programa vamos a ingresar dos numeros para sumarlos, numeros enteros, 
# luego analiza si al ser mayor a 100 lo determina como grande

valor1=int(input("ingresa numero: \n"))
valor2=int(input("ingresa numero2 \n"))
valor3=valor1+valor2

print("la suma es",valor3)

if valor3 >= 100 :
    print("wow el numero es grande")
else:
    print ("bueno el numero no es tan grande")