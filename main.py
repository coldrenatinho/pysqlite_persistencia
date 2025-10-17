# main.py
import random

from produto import Produto
from produto_dao import ProdutoDAO
from tipoproduto import TipoProduto


def main():
    dao = ProdutoDAO()

    # Criar tabela
    dao.criar_tabela()

    tipos = [
        TipoProduto(descricao="Roupas"),
        TipoProduto(descricao="Calçados"),
        TipoProduto(descricao="Acessórios")
    ]

    # Adicionar produtos
    produtos = [
        Produto(nome="Camiseta", tipo="Roupas", preco=29.99),
        Produto(nome="Calça Jeans", tipo="Roupas", preco=59.99),
        Produto(nome="Tênis Esportivo", tipo="Calçados", preco=89.99)
    ]


    for produto in produtos:
        dao.adicionar(produto)

    # Listar produtos
    print("\n--- Lista de Produtos ---")
    for produto in dao.listar_todos():
        print(produto)

    # Atualizar produto
    dao.atualizar(2, "Calça Jeans Slim", random.random() * 100)

    # Listar produtos atualizados
    print("\n--- Lista Atualizada ---")
    for produto in dao.listar_todos():
        print(produto)

    # Deletar produto
    dao.deletar(1)

    # Listar produtos final
    print("\n--- Lista Final ---")
    for produto in dao.listar_todos():
        print(produto)

if __name__ == "__main__":
    main()