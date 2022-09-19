#Utilizando a função anterior, faça a impressão da temperatura, em graus Celsius, de 0 °C a 100 °C, e todos os valores correspondentes em Fahrenheit.

for t in range(101):
    f=t-32
    print (f"{t} ºC = {f}º F")