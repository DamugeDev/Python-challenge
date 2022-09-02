#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def reverso(n):
    
    b=n[::-1]
    return(b)

n=(input('Insira o numero: '))
print(f'Reverso: {reverso(n)}')