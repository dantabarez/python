#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10 y de 10

for i in range(1,10):
    print("La tabla del " , i)
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print("-----------------------")