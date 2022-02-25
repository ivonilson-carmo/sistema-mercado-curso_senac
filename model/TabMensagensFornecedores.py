from conn import conn, cursor

def criaTabMensagensFornecedores():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensagens_fornecedores(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_horario_mensagem DATETIME NOT NULL,
                tipo TEXT NOT NULL,
                mensagem TEXT NOT NULL,
                id_fornecedor INTEGER NOT NULL,
                FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id)
                    ON DELETE CASCADE
                    ON DELETE CASCADE
            );
        ''')
        conn.commit()
        # print('========== Tabela mensagens_fornecedores criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')