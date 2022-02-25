from conn import conn, cursor

def criaTabMercado():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mercado(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                acesso_administrador TEXT NOT NULL,
                cnpj TEXT NOT NULL,
                data_hora_estreia DATETIME NOT NULL,
                descricao_mercado TEXT NOT NULL,
                endereco TEXT NOT NULL,
                horario_funcionamento TEXT NOT NULL,
                email_mercado TEXT,
                telefone_mercado TEXT
            );
        ''')
        conn.commit()
    except Exception as erro:
        print(erro)
        print('Erro ao criar Tabela')