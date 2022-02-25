from conn import conn, cursor


def criaTabFornecedores():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fornecedores(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_fornecedor TEXT NOT NULL,
                email TEXT NOT NULL,
                whatsapp TEXT
            );
        ''')
        conn.commit()
        # print('========== Tabela fornecedores criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')