#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida

def escada(a):
    for i in range(len(a),0,-1):
        print(f'{a[:i]}  ')

nome=input('Insira o nome: ')
escada(nome)