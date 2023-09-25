# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def mult(x,y):
    return x * y
tabela = []
numeros = input('Digite a quatidade de vezes a ser multiplicado e o número: ')

numeros_split = numeros.split()

for numero in numeros_split:
    tabela.append(int(numero))

print(mult(*tabela))


# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar


# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))