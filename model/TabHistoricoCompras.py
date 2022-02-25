from conn import conn, cursor

def criaTabHistoricoCompras():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historico_de_compra(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_horario DATETIME NOT NULL,
                valor FLOAT NOT NULL,
                meio_de_pagamento TEXT NOT NULL
            );
        ''')
        conn.commit()
        # print('========== Tabela historico_compra criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')