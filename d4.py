#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
a=str(input('Introduza a letra: '))
def vogal (v):
    if v in "aeiou":
        print ('Vogal')
    else:
        print ('Consoante')

vogal(a)