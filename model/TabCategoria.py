from conn import conn, cursor


def criaTabCategorias():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );
        ''')
        conn.commit()
        # print('========== Tabela categorias criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')