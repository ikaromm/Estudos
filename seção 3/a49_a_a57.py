"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
comentar direto crtl + ;
"""
# try:
#    numero_float = float(numero_str)
#    print('FLOAT:', numero_float)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# except:
#    print('Isso não é um número')
# id() é o valor na memoria 
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = Identidade
# condicao = False
# passou_no_if = None
# if condicao:
#     passou_no_if = True
#     print('Faça algo')
# else:
#     print('Não faça algo')
# if passou_no_if is None:
#     print('Não passou no if')
# else:
#     print('Passou no if')

'''
ex 1
'''

# numero = input('digite um número inteiro: ')

# if numero.isdigit():
#     numero_int= int(numero)
#     div_por_2 = numero_int % 2 == 0
#     if div_por_2 == True:
#         print(f'seu número {numero_int} é par')
#     else:
#         print(f'seu número {numero_int} é ímpar')

# else:
#     print("Por favor, digite um número inteiro válido.")

"""
ex 2
"""


# hora= input('Digite somente a hora: ')

# if hora.isdigit():
#     hora_int=int(hora)
#     if hora_int>= 0 and hora_int<11: 
#         print('Bom dia')
#     elif hora_int>=11 and hora_int<17:
#         print('Boa tarde')
#     elif hora_int>=17 and hora_int <=23:
#         print('Boa noite')
# else:    
#     print('digite somente a hora')  

nome = input('Escreva seu nome')

tamanho_nome = len(nome)

if tamanho_nome <= 4: 
    print(f'Seu nome: {nome} é pequeno')
elif tamanho_nome <= 6:
    print(f'Seu nome: {nome} é grande')
else:
    print(f'Seu nome: {nome} é muito grande')       

