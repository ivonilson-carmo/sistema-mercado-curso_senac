from conn import conn, cursor


def criaTabRelatorioEstoquista():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relatorio_estoquista(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_horario DATETIME NOT NULL,
                relatorio TEXT NOT NULL
            );
        ''')
        conn.commit()
        # print('========== Tabela relatorio_estoquista criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')