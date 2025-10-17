import sqlite3
import os

DB_FILE = "produto.db"


def conectar_bd():
    conexao = sqlite3.connect(DB_FILE)
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            preco FLOAT NOT NULL
        );
    """)
    conexao.commit()
    print("Tabela produto verificada/criada com sucesso.")


def adicionar_produto(conexao, nome, tipo, preco):
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO produto (nome, tipo, preco)
            VALUES (?, ?, ?);
        """, (nome, tipo, preco))
        conexao.commit()
        print(f"Produto: '{nome}' adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print("Houve um erro ao adicionar o produto. Verifique se o tipo é único.")

def listar_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto;")
    produto = cursor.fetchall()

    if not produto:
        print("Nenhum")
        return

    print("\n--- Lista de prduto ---")
    for produto in produto:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, preco: {produto[2]}")
    print("-------------------------\n")


def atualiza_produto(conexao, id, nome_produto, novo_valor):
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE produto
        SET nome = ?,
            preco = ?
        WHERE id = ?;
    """, (nome_produto, novo_valor, id))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Produto com id '{id}' atualizado com sucesso.")
    else:
        print(f"Nenhum produto encontrado com o id '{id}'.")


def deletar_produto(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM produto
        WHERE id = ?;
    """, (id,))  # A vírgula é necessária para que o Python entenda que é uma tupla
    conexao.commit()

def main():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Arquivo de banco de dados '{DB_FILE}' antigo removido.")


    conexao = conectar_bd()
    if conexao:
        with conexao:
            criar_tabela(conexao)

    if conexao:
        with conexao:
            adicionar_produto(conexao, "Camiseta", "Roupas", 29.99)
            adicionar_produto(conexao, "Calça Jeans", "Roupas", 59.99)
            adicionar_produto(conexao, "Tênis Esportivo", "Calçados", 89.99)

    if conexao:
        with conexao:
            listar_produtos(conexao)

    if conexao:
        with conexao:
            atualiza_produto(conexao, 2, "Calça Jeans Slim", 64.99)

    if conexao:
        with conexao:
            listar_produtos(conexao)

    if conexao:
        with conexao:
            deletar_produto(conexao, 1)

    if conexao:
        with conexao:
            listar_produtos(conexao)

if __name__ == "__main__":
    main()