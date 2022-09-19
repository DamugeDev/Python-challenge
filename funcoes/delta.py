#Considere uma equação do segundo grau 𝑓(𝑥) = 𝑎 · 𝑥2 + 𝑏 · 𝑥 + 𝑐. A partir dos coeficientes, determine se a equação possui duas raízes reais, uma, ou se não possui.

ax=int(input("Insira o coeficiente de a: "))
bx=int(input("Insira o coeficiente de b: "))
cx=int(input("Insira o coeficiente de c: "))

def delta(a,b,c):
    delt=b**2-(4*a*c)

    if(delt>0):
        print("A equacao tem duas raizes")
    elif(delt==0):
        print("A equacao tem uma raiz")
    else:
        print("A equacao nao tem raizes")