#Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o resto de uma divisão.

def paridade(a):
    if(a%2==0):
        return "Par"
    return "Impar"

print(paridade(17))