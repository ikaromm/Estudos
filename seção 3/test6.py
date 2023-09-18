# input('') serve para capturar um dado no formato str
# é uma boa pratica fazer a troca do objeto em outra variavel e não direto no input
# if / elif      / else
# se / se não se / se não

#nome = int(input('Qual o seu nome? '))
#nome1=int(input('asd '))
#print(f'O seu nome é {nome} {nome1} e {nome+nome1=}')
"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'

"""
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
#avaliação de curto circuito

# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

if primeiro_valor > segundo_valor :
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor < segundo_valor :
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')    
else :
    print('os valores são iguais')