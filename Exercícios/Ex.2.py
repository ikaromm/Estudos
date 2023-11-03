# Exercícios com funções
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

tabela_num = []
cte = 0


def mult(*args):
    total_mult = 1
    for numero in args:
        total_mult *= numero
    return total_mult


numeros = input("Escreva os números com um espaço de diferença ")

numeros_split = numeros.split()

for rank in numeros_split:
    tabela_num.append(int(rank))

print(mult(*tabela_num))
