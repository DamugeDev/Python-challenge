#Faça um Programa que peça dois números e imprima o maior deles.

a=int(input("Introduza o primeiro numero: "))

b=int(input("Introduza o segundo numero: "))

if(a>b):
    print('O primeiro é maior')
elif(b>a):
    print('O segundo é maior')
else:
    print('Os numeros introduzidos sao iguais')