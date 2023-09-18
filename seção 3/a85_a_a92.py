#Quando se usa o list(adasd).copy ele copia a lista
# se fizer um lista a = lista b como é mutavel significa que se mudar na a muda na b
"""
Introdução ao empacotamento e desempacotamento
"""
"""
Tipo tupla - Uma lista imutável
"""
# nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
# print(nomes[-1])
# print(nomes)

# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome)

# lista = ['a','b','c']
# len_lista = len(lista)
# n=0


# while n < len_lista:
#     for letra in lista:
#         print(f'{letra} e o local na lista é {n} ')
#         n +=1

# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])        


lista_compra  = []

while True:
    acao_lista = input('escreva [i]nserir, [a]pagar ou [l]istar: ')
    
    if acao_lista == 'a':
        apagar_lista = input('Digite o indice a ser apagado')
        try:
            if int(apagar_lista) < len(lista_compra):
                del lista_compra[int(apagar_lista)]
        except:    
            print('digite um valor valido')
       
    
    elif acao_lista == 'i':
        add_lista = input('Nome do Item a ser adicionado: ')
        lista_compra.append(add_lista)
        

    elif acao_lista == "l":
        for indice, item in enumerate(lista_compra):
            print(indice, item)
            

    else:
        print('Escreva apenas  i, a ou l')

"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))                   