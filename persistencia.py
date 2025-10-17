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
            tipo TEXT NOT NULL UNIQUE,
            preco FLOAT NOT NULL
        );
    """)
    conexao.commit()
    print("Tabela produto verificada/criada com sucesso.")


def adicionar_produto(conexao, nome, tipo, preco):
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO contatos (nome, email, telefone)
            VALUES (?, ?, ?);
        """, (nome, tipo, preco))
        conexao.commit()
        print(f"Produto: '{nome}' adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print("Houve um erro ao adicionar o produto. Verifique se o tipo é único.")

def listar_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos;")
    produto = cursor.fetchall()

    if not produto:
        print("Nenhum")
        return

    print("\n--- Lista de prduto ---")
    for produto in produto:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Email: {produto[2]}, Telefone: {produto[3]}")
    print("-------------------------\n")


def atualiza_produto(conexao, id, nome_produto, novo_valor):
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE produto
        SET nome = ?,
        SET preco = ?,
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
        # O bloco 'with' garante que a conexão será fechada mesmo se ocorrer um erro
        with conexao:
            # 1. CRIAR a estrutura
            criar_tabela(conexao)


# Ponto de entrada do script
if __name__ == "__main__":
    main()