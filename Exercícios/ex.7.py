from itertools import combinations_with_replacement, combinations

def retorna_combinacoes(nome_maiusculo, numero_inteiro):
    return list(combinations_with_replacement(nome_maiusculo, numero_inteiro))

def ordena_combinacoes(lista):
    for i in range(len(lista)):
        lista[i] = sorted(list(lista[i]))
    return lista

def main():
    nome_maiusculo = "HACK"
    numero_inteiro = 2
    
    lista = retorna_combinacoes(nome_maiusculo, numero_inteiro)

    sorted_combination_list = ordena_combinacoes(lista)

    for name in sorted(sorted_combination_list):
        name_1 = "".join(name)
        print(name_1)

# Call the main function
if __name__ == "__main__":
    main()