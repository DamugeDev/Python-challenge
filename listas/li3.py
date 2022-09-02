#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

acumulador=0
for i in range(4):
    n=int(input("Insira o numero: "))
    acumulador+=n
print('================')
media=acumulador/4
print(f'Media: {media}')