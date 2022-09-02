#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória..
from random import sample
def embaralha(palavra):
    a = sample(palavra,len(palavra))
    d = ''.join(a)
    print(a)
    print(d.lower())


palavra = input('Digite algo: ')
embaralha(palavra)