from conn import conn, cursor


def criaTabCompraProduto():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS compra_produtos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_compra INTEGER NOT NULL,
                valor FLOAT NOT NULL,
                id_produto INTEGER NOT NULL,
                FOREIGN KEY(id_compra) REFERENCES historico_de_compra(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY(id_produto) REFERENCES produtos(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
        ''')

        conn.commit()
    except Exception as e:
        print(e)
