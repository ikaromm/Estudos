class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, *produto):
        self.produtos.extend(produto)

    def soma_total(self):
        return sum([p.preco for p in self.produtos])

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()
p1 = Produto("Camiseta", 50)
p2 = Produto("Caneca", 10)
carrinho.adicionar_produto(p1, p2)
carrinho.soma_total()
#
print(carrinho.soma_total())
print(carrinho.listar_produtos())


#########


# class Carrinho:
#     def __init__(self):
#         self._produtos = []

#     def total(self):
#         return sum([p.preco for p in self._produtos])

#     def inserir_produtos(self, *produtos):
#         # self._produtos.extend(produtos)
#         # self._produtos += produtos
#         for produto in produtos:
#             self._produtos.append(produto)

#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()


# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco


# carrinho = Carrinho()
# p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
# carrinho.inserir_produtos(p1, p2)
# carrinho.listar_produtos()
# print(carrinho.total())
