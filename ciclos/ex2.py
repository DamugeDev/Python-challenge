#Ler do teclado uma lista com 5 inteiros e imprimir o menor valor
lista=[]
for i in range(5):
    a=int(input("Insira o numero: "))
    lista.append(a)

print("Menor valor: ", min(lista))