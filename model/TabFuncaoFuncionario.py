import imp
from conn import conn, cursor


def criaTabFuncaoFuncionario():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcao_funcionario(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                funcao TEXT NOT NULL,
                descricao_funcao TEXt NOT NULL,
                salario FLOAT NOT NULL
            );
        ''')
        conn.commit()
        # print('========== Tabela funcao_funcionario criada com sucesso =========')
    except Exception as erro:
        print(erro)
        #  print('Erro ao criar Tabela funcao_funcionario')