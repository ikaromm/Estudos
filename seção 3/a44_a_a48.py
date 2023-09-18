"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
print(f'{variavel: >10}') completa com espaço vazio a esquerda
len() serve para contar qnt de caracter de str
fatiamento[i:f:p] em que p é o passo, o usual é 1 mas pode ser 2 mundo [::2] => mno e o -1 em p inverte
"""
#nome = 'mundo'
#preco = 1000.95897643
#variavel = '%s, o preço é R$%.2f' % (nome, preco)
#print(variavel)
#print('O hexadecimal de %d é %08X' % (1500, 1500))
#print(f'{nome[::2]}')


nome = input('Digite seu Nome: ' )
idade = input('Digite sua idade: ' )
carac_nome = len(nome)
if nome != '' and idade != ''  :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido {nome[::-1]}')
    print(f'Seu nome tem {carac_nome} letras')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A última letra do seu nome é {nome[carac_nome-1:carac_nome]}')
    if ' ' in nome :
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
else:
    print('Desculpe, você deixou campos vazios')        

