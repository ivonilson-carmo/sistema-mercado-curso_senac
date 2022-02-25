from conn import conn, cursor


def criaTabProdutos():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                nome TEXT NOT NULL,
                valor FLOAT NOT NULL,
                quantidade INTEGER NOT NULL,
                id_categoria INTEGER NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categorias(id)
                    ON DELETE CASCADE
                    ON DELETE CASCADE
            );
        ''')
        conn.commit()
        # print('========== Tabela produtos criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')