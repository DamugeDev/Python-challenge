#Crie uma função que receba um valor de temperatura em Fahrenheit e transforme em Celsius.

def f_c(t):
    f=t-32
    return f"{t} ºC = {f}º F"

print(f_c(40))