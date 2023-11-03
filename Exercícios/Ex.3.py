# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def paridade(x):
    if x % 2 == 0:
        return "par"
    return "ímpar"


numero = int(input("Digite o número "))

print(f"O número {numero} é {paridade(numero)}")
