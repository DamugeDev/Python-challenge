#Faça um programa para imprimir
    #1   
   # 2   2
    #3   3   3
    #.....
    #n   n   n   n   n   n  ... n
n=int(input('Insira o numero limite: '))
for i in range(n+1):
    print(f'{i}  '*i)