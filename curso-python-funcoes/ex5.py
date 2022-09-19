#Alanderson quer saber se um endereço IP é válido. Faça um programa para ajudar Alanderson a testar se um endereço é válido. Para isso, a entrada deve ser um endereço IP (digitado pelo usuário) e o programa deve escrever na tela se é válido ou não. Um endereço IPv4 é composto por 4 números inteiros entre 0 e 255, separados por um ponto.

from pickle import TRUE
from xmlrpc.client import boolean




def ip(x):
    
    xi=x.split(".") #Separei os numeros e criei uma lista
    if(len(xi)==4): #Garantia de que o tamanho da lista[] deve ser de 4
        cc=0 # variavel contadora
        for cont in range(4):
            if(int(xi[cont])>=0 and int(xi[cont])<=255): #Intervalo dos numeros
                cc+=1
        if(cc==4): # O 4 representa o numero de instrucoes verdadeiras da condicao anterior
            print("Endereco Valido")        
        else:
            print("Endereco Invalido")   
    else:
            print("Endereco Invalido") 
    

a="244.128.y.5"
b="233.454.0.22"
ip(a)

#NB: NAO CONSIDEREI CASOS EM QUE EXISTEM ENTRADA DE CARACTERES EX: 132.168.k.1