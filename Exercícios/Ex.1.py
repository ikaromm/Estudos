# Task
# You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
# Input Format
# A single line containing the string  and integer value  separated by a space.
# Constraints
# The string contains only UPPERCASE characters.
# Output Format
# Print the combinations with their replacements of string  on separate lines.

# # Combinations with replacement from '12345' with length 2
# combinations_with_replacement_result = list(combinations_with_replacement('12345', 2))
# print(combinations_with_replacement_result)

# # Combinations from list A with length 2
# A = [1, 1, 3, 3, 3]
# combinations_result = list(combinations(A, 2))
# print(combinations_result)

# ----------------------------------------------------------------------------
from itertools import combinations_with_replacement, combinations

nome_e_qntd = input("")

input_parts = nome_e_qntd.split()

nome = input_parts[0]
numero = input_parts[1]

nome_maiusculo = nome.upper()
numero_inteiro = int(numero)

lista = list(combinations_with_replacement(nome_maiusculo, numero_inteiro))

sorted_lista = sorted(lista)

for name in sorted_lista:
    name_1 = "".join(name)
    print(name_1)
