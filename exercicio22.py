#Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.
import math
a=int(input("Insira o numero: "))

if(a>=0):
    print(math.sqrt(a))
else:
    print(a**2)
