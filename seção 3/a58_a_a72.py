# https://docs.python.org/pt-br/3/library/stdtypes.html
# Imutáveis que vimos: str, int, float, bool
# while e break, break serve para parar o laço mais próximo
# continue serve para pular um loop do while e voltar ao começo
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

# nome = 'ikaro moribayashi'
# tam_nome = len(nome)
# n = 0
# new_name= ' '
# while n < tam_nome:
#     print(f'{nome[n]} esssa letra está na posição {n}')
#     new_name += f'*{nome[n]}'
#     n += 1
# print(new_name)    

frase = 'aaaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)