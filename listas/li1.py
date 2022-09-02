#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
lista =[]
print(len(lista))
for i in range(5):
    n=int(input("Insira o numero: "))
    lista.append(n)
print('================')
for i in range(5):
    print(lista[i])

#OU print(lista)
