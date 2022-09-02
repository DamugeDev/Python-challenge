#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
def extenso(a):
    meses=['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    
    b=a.split('/')
    dia=b[0]
    mes=b[1]
    mes_ext=meses[int(mes)-1]
    ano=b[2]
    return(f'{dia} de {mes_ext} de {ano}')

#OS ERROS NAO FORAM TRATADOS
a=input('Insira a data DD/MM/AAAA: ')
print(extenso(a))