#Crie uma função que receba 3 valores e calcula as raízes da fórmula de Bh¯askara.
import math


def quadratica(a,b,c):
    delta=b**2-4*a*c
    if(delta>=0):
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print( "x1 = ",x1,"\nx2 = ",x2)
    else:
        print("NAO TEM RAIZES")    

quadratica(1,-4,-4)