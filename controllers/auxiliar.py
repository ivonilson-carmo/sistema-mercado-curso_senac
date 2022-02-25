from conn import conn, cursor
from datetime import datetime

"""
!important

Arquivo operador.py
requisito 016
verificar se ta ok
"""



class AuxiliarAdministrador():
    def cadastraFuncionario(self):
        """ Pede os dados do funcionarios e insere na tabela funcionarios """
        try:
            print('======== cadastro do funcionario ========\n')
            # pede os dados que vai precisar para o cadastro
            nome = input('Nome: ')
            nasc = input('Nascimento(Padrão: DD-MM-YYYY): ').strip().split('-')
            nasc = '-'.join(nasc[::-1])
            cpf = input('CPF(Padrão: 000.000.000-00): ')
            tipo = input('Tipo de funcionario[fixo ou temporario]: ').strip().lower()
            # se o tipo de funcionario for fixo
            if tipo == 'fixo':
                tempo = 365  # recebe o padrão de 365 dias
            else: # senão é requerido que digite o tempo em dias.
                tempo = int(input('Tempo(em dias, ex.: 44): '))
            
            self.exibeFuncao()
            funcao = int(input('ID da função que o funcionário vai receber: '))
            
            dados =  (nome, nasc, cpf, tipo, tempo, funcao)
            # registra informações no banco de dados
            cursor.execute('''
            INSERT INTO funcionarios(
                nome,
                nascimento,
                cpf,
                tipo,
                tempo,
                id_funcao_funcionario
            ) VALUES (?,?,?,?,?,?);
            ''', dados)

            conn.commit()
            
            print('======== Funcionario Cadastrado com sucesso ========\n')
        
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except ValueError:
            print('\n* Erro 1 - É esperado que digite um número.')
    
    def cadastraFuncao(self):
        """ Adciona dados na tabela funcao_funcionario"""
        try:
            print('======== cadstro das funções ========\n')
            # pede os dados para registro
            nome = input('Nome da funçao: ').strip().lower()
            confirmaNome = input('Confirme o nome da função: ').strip().lower()
            # se o nome e a confirmação do nome digitados forem diferentes -> recomeça o regitro
            while (nome != confirmaNome):
                print('Ocorreu um erro tente novamente!')
                self.cadastraFuncao()
                return
                
            
            desc = input('Descrição sobre a função que será exercida: ')
            salario = float(input('Salario de quem recebe a função: '))
            
            dados =  (nome, desc, salario)
            # registra informações no banco de dados
            cursor.execute('''
            INSERT INTO funcao_funcionario (
                funcao,
                descricao_funcao,
                salario
            ) VALUES(?,?,?);
            ''', dados)

            conn.commit()
            print('======== Função registrada com sucesso ========\n')
        
        except KeyboardInterrupt:
            print('* Voltando ao menu...')
        except ValueError:
            print('\n* Erro 1 - É esperado quese digite um número.')
        except Exception:
            print('\n* Erro 0 - Cadastro de função.')
    
    def exibeFuncao(self):
        """ Seleciona todas funcções na tabela funcao_funcionario e exibe cada linha """
        try:
            print('======= Funções dos funcionarios =======')
            
            cursor.execute(' SELECT * FROM funcao_funcionario')
            result = cursor.fetchall()

            for linha in result:
                print(f'1 - ID: {linha[0]}')
                print(f'2 - FUNÇÂO: {linha[1]}')
                print(f'3 - DESCRICAO: {linha[2]}')
                print(f'4 - SALARIO: {linha[3]}')
                print('====================================================== \n ')
            
        except KeyboardInterrupt:
            print('\n* Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Visualização das funções')
    
    def exibeHistoricoCompra(self):
        """ Busca tudo na tabela historico_de_compra  e exibe cada linha"""
        try:
            print('======= Historico das compras =======')
            
            cursor.execute(' SELECT * FROM historico_de_compra')
            result = cursor.fetchall()

            for linha in result:
                print(f'{linha[0]}  |  {linha[1]}  |  {linha[2]:.2f}  |  {linha[3]} \n')
                print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Vizualização do histórico de compras.')
    
    def exibeRelatorioEstoquista(self):
        """ Busca tudo na tabela relatorio_auxiliar e exibe cada linha"""
        try:
            print('======= RELATÓRIOS ESTOQUISTA =======')
            
            cursor.execute(' SELECT * FROM relatorio_estoquista')
            result = cursor.fetchall()

            for linha in result:
                print(f'''
    ID: {linha[0]}
    DATA: {linha[1]}
    RELATORIO: {linha[2]} ''')
                print('-=' * 50 + '\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception as e:
            print('\n* Erro 0 - Visualização dos relatórios feito pelo auxiliar')
          
    def exibeCategoria(self):
        """ busca tudo na tabela categorias e exibe cada linha """
        try:
            print('======= CATEGORIAS =======')
            
            cursor.execute(' SELECT * FROM categorias')
            result = cursor.fetchall()
            
            if (result != []):
                for linha in result:
                    print(f'{linha[0]}  |  {linha[1]}')
                    print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Visualização das categorias.')

    def exibeFinancas(self):
        """ busca tudo na tabela financas e exibe cada linha """
        try:
            print('======= FINANÇAS =======')
            
            cursor.execute(' SELECT * FROM financas')
            result = cursor.fetchall()

            for linha in result:
                print(f'{linha[0]}  |  {linha[1]}  |  {linha[2]}  |  {linha[3]}')
                print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Visualização de dados das finaças.')

    def exibeDadosEstoque(self):
        """ Busca tudo na tabela produtos e exibe cada linha"""
        try:
            print('======= PRODUTOS =======')
            
            cursor.execute(' SELECT * FROM produtos INNER JOIN categorias ON produtos.id = categorias.id')
            result = cursor.fetchall()

            for linha in result:
                print(f'{linha[0]}  |  {linha[1]}  |  {linha[2]}  |  {linha[3]}  |  {linha[4]}  |  {linha[7]}')
                print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception as e:
            print(e)
            print('\n* Erro 0 - Visualização dos produtos em estoque.')
    
    def exibeMensagensFornecedor(self):
        """ Busca tudo na tabela mensagens_fornecedores e exibe cada linha"""
        try:
            print('======= MENSAGENS FORNECEDOR =======')
            
            cursor.execute(' SELECT * FROM mensagens_fornecedores INNER JOIN fornecedores ON mensagens_fornecedores.id_fornecedor = fornecedores.id')
            result = cursor.fetchall()

            for linha in result:
                print(f'ID - {linha[0]}')
                print(f'DATA DA MENSAGEM: {linha[1]}')
                print(f'TIPO DA MENSAGEM: {linha[2]}')
                print(f'\nMENSAGEM: {linha[3]}\n')
                print(f'NOME DO FORNECEDOR: {linha[6]}')
                print(f'EMAIL PARA CONTATO: {linha[7]}')
                print(f'WHATSAPP DO FORNECEDOR: {linha[8]}')
                
                print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Visualização das mensagens áos fornecedores.')
    
    def exibeListaFuncionario(self):
        # busca tudo  na tabela funcionarios e exibe cada linha
        try:
            print('======= FUNCIONARIOS =======')
            
            cursor.execute(' SELECT * FROM funcionarios INNER JOIN funcao_funcionario ON funcionarios.id_funcao_funcionario = funcao_funcionario.id')
            result = cursor.fetchall()

            for linha in result:
                print(f'''
                    1 - ID: {linha[0]}
                    2 - NOME: {linha[1]}
                    3 - NASCIMENTO: {linha[2]}
                    4 - CPF: {linha[3]}
                    5 - TIPO: {linha[4]}
                    6 - TEMPO: {linha[5]}
                    7 - FUNÇÂO: {linha[8]}
                    8 - DESCRIÇÂO: {linha[9]}
                    9 - SALARIO: {linha[10]}
                    ''')
                print('======================================================\n')
            
        except KeyboardInterrupt:
            print('\n * Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Visualização da lista funcionários.')
    
    def alteraDadosFuncao(self):
        """ Exibe os dados registrado na tabela funcao_funcionario e realiza alteração nos dados desejados"""
        print('=============== ALTERA FUNÇÔES DOS FUNCIONÁRIOS =================\n')
        
        self.exibeFuncao()
        try:
            idFuncao = int(input('Digite o identificador da função: '))
            cursor.execute(f'SELECT * FROM funcao_funcionario WHERE id = {idFuncao}')
            
            result = cursor.fetchall()
            if result != []:
                ops = input('Numeros das opções que deseja alterar(separado por espaços) ou [enter] para deixar como estar\n\t>>> ').strip().split()
                for op in ops:
                    op = int(op)

                    if op == 2:
                        newFunc = input('Novo nome função: ')
                        cursor.execute(f'UPDATE funcao_funcionario SET funcao = "{newFunc}"')
                    
                    elif op == 3:
                        newDesc = input('Nova descrição função: ')
                        cursor.execute(f'UPDATE funcao_funcionario SET descricao_funcao = "{newDesc}"')
                    
                    elif op == 4:
                        newSalario = float(input('Novo salario para essa função: '))
                        cursor.execute(f'UPDATE funcao_funcionario SET salario = "{newSalario}"')
                    
                    conn.commit()
            else:
                print('\n** Nada encontrado, Tentee Novamente!!\n')
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu...')
        except ValueError:
            print('\n* Erro 1 - É esperado que se digite um número.')
        except Exception:
            print('\n* Erro 0 - Alteração dados das função dos funcionários.')
    
    def alteraDadosFuncionario(self):
        """ Exibe tudo da tabela funcionarios e obtem o valor que será mudado e realiza a alteração """
        try:
            print('=============== ALTERA PERFIL DOS FUNCIONÁRIOS =================\n')

            self.exibeListaFuncionario()
            cpfDoFuncionario = input('Digite o cpf referente ao perfil do funcionario que deseja modificar: ')

            cursor.execute(f'SELECT * FROM funcionarios WHERE cpf = "{cpfDoFuncionario}" ')
            result = cursor.fetchall()

            if result != []:
                ops = input('''
                    Digite um ou mais items do perfil que deseja editar(separado por espaços) ou tecle [enter] para deixar como estar
                        >>> ''').strip().split()
                for op in ops:
                    op = int(op)
                    
                    if op == 2:
                        newNome = input('Novo nome: ')
                        cursor.execute(f'UPDATE funcionarios SET nome = "{newNome}" WHERE cpf = "{cpfDoFuncionario}"')
                    
                    elif op == 3:
                        newNascimento = input('Nascimento(Padrão: DD-MM-YYYY): ').strip().split('-')
                        newNascimento = '-'.join(newNascimento[::-1])
                        cursor.execute(f'UPDATE funcionarios SET nascimento = "{newNascimento}" WHERE cpf = "{cpfDoFuncionario}"')
                    
                    elif op == 4:
                        newCPF = input('CPF(Padrão: 111.222.333-44): ')
                        cursor.execute(f'UPDATE funcionarios SET cpf = "{newCPF}" WHERE cpf = "{cpfDoFuncionario}"')
                    
                    elif op == 5:
                        newTipo = input('Novo tipo de funcionario(Fixo ou Temporario): ')
                        cursor.execute(f'UPDATE funcionarios SET tipo = "{newTipo}" WHERE cpf = "{cpfDoFuncionario}"')
                    
                    elif op == 6:
                        newTempo = input('Tempo de trabalho do funcionario: ')
                        cursor.execute(f'UPDATE funcionarios SET tempo = "{newTempo}" WHERE cpf = "{cpfDoFuncionario}"')
                    
                    elif op in (7, 8, 9):
                        print('\n** Para editar essas opções altere os dados no registro das funções dos funcionários!\n')
                    
                    # salva informaçõs
                    conn.commit()
            else:
                print('\n** Nada encontrado, Tente Novamente!!\n')
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except ValueError:
            print('\n* Erro 1 - É esperado que se digite um número.')
        except Exception:
            print('\n* Erro 0 - Alteração dados do perfil do  funcionário.')
    
    def cadastraCategoria(self):
        """ Insere uma categoria na tabela categorias"""
        try:
            print('======== Cadastro de Categorias ========\n')
            nome = input('Nome da categoria: ')
            dados =  (nome, )

            cursor.execute('''
                INSERT INTO categorias (nome) VALUES(?);
            ''', dados)

            conn.commit()
            
            print('======== Categoria registrada com sucesso ========\n')
        
        except KeyboardInterrupt:
            print('\n*  Voltando ao menu...')
        except Exception:
            print('\n* Erro 0 - Registro de categoria')
    
    def cadastraProduto(self):
        """ Insere um produto na tabela produto """
        try:
            print('======== Cadastro de produtos ========\n')
            # obtem os valores necessários para o registro de um produto
            codigo = int(input('Código do produto(código de barras): '))
            
            nome = input('Nome do produto: ')
            valor = float(input('Valor do produto: '))
            quantidade = int(input('Quantidade desse produto: '))

            self.exibeCategoria()  # exibe as categorias registrada no sistema
            # obtem do administrador a categoria do produto que está sendo atualmente cadastrado
            id_categoria = int(input('ID da categoria á qual esse produto corresponde: '))
            
            # verifica se o identificador da categoria existe
            result = cursor.execute(f'SELECT * FROM categorias WHERE id={id_categoria}').fetchall()
            # se não existir o identificador da categoria exibe mensagem de não encontrado
            if result == []:
                print('\n* Nada encontrado')
                return
            
            # Existe a categoria!
            # registra os dados no banco de dados
            dados =  (codigo, nome, valor, quantidade, id_categoria)

            cursor.execute('''
                INSERT INTO produtos (codigo, nome,valor, quantidade, id_categoria) VALUES(?,?,?,?,?);
                ''', dados)

            conn.commit()
            
            print('======== Produto registrada com sucesso ========\n')
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu...')
        except ValueError:
            print('\n* Erro 1 - É esperado que se digite um número.')
        except Exception:
            print('\n* Erro 0 - Registro de um produto.')
    
    def RegistraRelatorioAlterações(self):
        """ Registra um relatorio de alteracoes na tabela alteracoes_auxiliar"""
        relatorio = input('Escreva o relatorio: ')
        horario = datetime.today().strftime('%Y-%m-%d')
        dados = (horario, relatorio)

        try:
            cursor.execute('''
            INSERT INTO alteracoes_auxiliar(data_horario, relatorio) values(?,?)
            ''', dados)
            conn.commit()
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu.')
        except Exception:
            print('\n* Erro 0 - Registrando Relatório.')
    
    def registraGasto(self):
        """ registra uma financa na tabela finanças"""
        try:
            print('======== Registro de Financa ========\n')
            
            valor = float(input('Valor: '))
            descricao = input('Descricao: ')
            horario = datetime.today().strftime('%Y-%m-%d')
            
            dados =  (horario, valor, descricao)

            cursor.execute('INSERT INTO financas (data_horario, valor, descricao) VALUES(?,?,?);', dados)

            conn.commit()
            
            print('======== Gasto registrada com sucesso ========\n')
        
        except ValueError:
            print('\n* Erro 1 - É esperado que se digitie um número: ')
        except KeyboardInterrupt:
            print('\n* Voltando ao menu')
        except Exception:
            print('\n* Erro 0 - Registrando um gasto.')
    
    def exibeFornecedores(self):
        """ Exibe todas mensagem dos fornecedores registrada no banco de dados """
        try:
            cursor.execute('SELECT * FROM fornecedores')
            result = cursor.fetchall()

            for linha in result:
                print(f'1 - ID: {linha[0]}')
                print(f'FORNECEDOR: {linha[1]}')
                print(f'EMAIL: {linha[2]}')
                print(f'WHATSAPP: {linha[3]}')
                print('=' * 50)
        
        except KeyboardInterrupt:
            print('\n* Saindo do sistema')
        except Exception:
            print('\n*Erro 0 - Exibindo lista de fornecedores')

    def registraMensagemFornecedor(self):
        """ insere dados de mensagem enviadas ou recebidas na tabela mensagens_fornecedor """
        try:
            # obtem a hora atual e o tipo da mensagem que será registrada
            data = datetime.today().strftime('%Y-%m-%d - %H:%M')
            tipo = input('Tipo da mensagem[enviada ou recebida]: ').strip().lower()
            while tipo not in ('enviada', 'recebida'):  # enquanto o valor da variavel tipo não for "enviada" ou "recebida"
                # solicita o tipo da mensagem
                tipo = input('Tipo da mensagem[enviada ou recebida]: ').strip().lower()
            
            self.exibeFornecedores() #exibe lista dos fornecedores registrados no sistema
            # solicita o identificador do fornecedor
            idFornecedor = int(input('\nIdentificador do Fornecedor: '))
            # se o identificador inserido não corresponder a um fornecedor registrado no sistema
            result = cursor.execute(f'SELECT * FROM fornecedores WHERE id = {idFornecedor}').fetchall()
            if not result:
                # exibe mensagem de erro
                print('* Identificador invalido, voltando ao menu!')
                return
            
            # solicita o conteudo da mensagem com o fornecedor
            mensagem = input('Digite o texto da mensagem recebida: ')
            # registra no sistema as informações
            cursor.execute('''
            INSERT INTO mensagens_fornecedores(data_horario_mensagem, tipo, mensagem, id_fornecedor) VALUES (?,?,?,?)
            ''', (data, tipo, mensagem, idFornecedor))
            conn.commit()
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu')
        except Exception as e:
            print('\n* Erro 0 - Registrando mensagem com um fornecedor')