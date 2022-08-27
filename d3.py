#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
a=str(input('Introduza o sexo (M ou F): '))
if(a.upper()=="M"):
    print('Masculino')
elif(a.upper()=="F"):
    print('Feminino')
else:
    print('Sexo Invalido')

