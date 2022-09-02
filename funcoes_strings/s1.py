#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

def escada(a):
    for i in range(len(a)+1):
        print(f'{a[:i]}  ')

nome=input('Insira o nome: ')
escada(nome)