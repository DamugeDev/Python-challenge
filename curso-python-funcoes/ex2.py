#Faça uma função que calcule a área de um círculo. Insira o raio como argumento
import math
def area(r):
    a=math.pi*(r**2)
    return(a)

print(area(int(input("Insira a area: "))))
