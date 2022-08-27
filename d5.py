
#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a #média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

#ATT: Resolvido SEM considerar os limites (eg. Media superior a 10)
 
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2
print('Media = ',media)
if(media==10):
    print('Aprovado com distincao')
elif(media>=7):
    print('Aprovado')
else:
    print('Reprovado')
