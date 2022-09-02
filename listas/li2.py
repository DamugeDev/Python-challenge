#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista =[]

for i in range(10):
    n=int(input("Insira o numero: "))
    lista.append(n)
print('================')

invertido=list(reversed(lista))
print(invertido)