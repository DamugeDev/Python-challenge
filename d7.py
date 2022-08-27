#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1=int(input("Primeiro numero: "))
n2=int(input("Segundo numero: "))
n3=int(input("Terceiro numero: "))
maior=max(n1,n2,n3)
menor=min(n1,n2,n3)
print("Maior: ",maior)
print("Menor: ",menor)