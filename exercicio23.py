#Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

meses=["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

a=int(input("Insira a cardinalidade do mes: "))

if(a>0 and a<13):
    print(meses[a-1])
else:
    print("Nao existe mes com este numero")