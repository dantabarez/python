# compara dos palabras y te dice cual de ellas es mas larga

palabra1=input("ingrese palabra 1: ")
palabra2=input("ingrese palabra 2: ")

if len(palabra1)>len(palabra2):
    print(palabra1," es mas larga que ",palabra2)
if len(palabra1)<len(palabra2):
    print(palabra2," es mas larga que ",palabra1)
if len(palabra1)==len(palabra2):
    print(palabra1," es igual de larga que ",palabra2)

