from conn import conn, cursor


def criaTabFuncionarios():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                cpf TEXT NOT NULL,
                tipo TEXT NOT NULL,
                tempo TEXT NOT NULL,
                id_funcao_funcionario INTEGER NOT NULL,
                FOREIGN KEY (id_funcao_funcionario) REFERENCES funcao_funcionario(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            );
        ''')
        conn.commit()
        # print('========== Tabela funcionarios criada com sucesso =========')
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela funcionarios')