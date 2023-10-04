caminho_arq = 'salvar.json'
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
p3 = Pessoa('Maria', 20)        

bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(caminho_arq, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()