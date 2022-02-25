from conn import conn, cursor


def criaTabAlteraçõesAuxiliar():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alteracoes_auxiliar(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_horario DATETIME NOT NULL,
                relatorio TEXT NOT NULL
            );
        ''')
        conn.commit()
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela alteracoes_auxiliar')