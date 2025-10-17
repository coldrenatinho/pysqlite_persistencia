# produto.py
from tipoproduto import TipoProduto

class Produto:
    def __init__(self, id=None, nome=None, tipo=None , preco=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Tipo: {self.tipo}, Preço: {self.preco:.2f}"