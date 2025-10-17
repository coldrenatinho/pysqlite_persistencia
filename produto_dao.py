# produto_dao.py
import sqlite3
import os
from produto import Produto

class ProdutoDAO:
    def __init__(self, db_file="produto.db"):
        self.db_file = db_file
        self.conexao = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.db_file)
        return self.conexao

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()

    def criar_tabela(self):
        conexao = self.conectar()
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
        self.fechar_conexao()

    def adicionar(self, produto):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO produto (nome, tipo, preco)
            VALUES (?, ?, ?);
        """, (produto.nome, produto.tipo, produto.preco))
        conexao.commit()
        self.fechar_conexao()
        print(f"Produto: '{produto.nome}' adicionado com sucesso.")

    def listar_todos(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produto;")
        rows = cursor.fetchall()
        produtos = [Produto(id=row[0], nome=row[1], tipo=row[2], preco=row[3]) for row in rows]
        self.fechar_conexao()
        return produtos

    def atualizar(self, id, novo_nome, novo_preco):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE produto
            SET nome = ?,
                preco = ?
            WHERE id = ?;
        """, (novo_nome, novo_preco, id))
        conexao.commit()
        self.fechar_conexao()
        print(f"Produto ID: {id} atualizado com sucesso.")

    def deletar(self, id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produto WHERE id = ?;", (id,))
        conexao.commit()
        self.fechar_conexao()
        print(f"Produto ID: {id} deletado com sucesso.")

