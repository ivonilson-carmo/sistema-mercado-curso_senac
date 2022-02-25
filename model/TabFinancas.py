from conn import conn, cursor


def criaTabFinancas():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS financas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_horario DATETIME NOT NULL,
                valor FLOAT NOT NULL,
                descricao TEXT NOT NULL
            );
        ''')
        conn.commit()
        # print('========== Tabela financas criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')