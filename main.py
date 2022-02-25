from model.conn import conn, cursor
from controllers.admin import Administrador
from controllers.auxiliar import AuxiliarAdministrador
from controllers.estoquista import Estoquista
from controllers.operador import Operador
from getpass import getpass
from model.schemmas import setup
from utils.utils import *
from time import sleep


class Mercado():
    def __init__(self):
        # atributos
        self.admin = Administrador()
        self.auxiliar = AuxiliarAdministrador()
        self.operador = Operador()
        self.estoquista = Estoquista()

        try:
            setup()
            # obtem tudo da tabela mercado
            cursor.execute(''' SELECT * FROM mercado ''')
            result = cursor.fetchall()
            
            # se o resultado da busca na tabela mercado for "vazio"
            # significa que o sistema não foi registrado
            if (result == []):
                # se não tiver registro do sistema, chama função para realiza-lo
                self.criaSistema()
            else:
                # se tiver registro, vai para seção de acesso do sistema
                self.acesso()

        except Exception:
            # se ocorrer algum erro, exibe mensagem de erro
            print('Erro 0 - iniciar sistema')

    def criaSistema(self):
        """ Função responsavel pelo pré-registro do sistema no banco de dados """
        print('====================== Hora de criar cadastra seu sistema ======================')
        print('====================== Será pedido algumas informações ======================\n\n')

        print('====================== significados =======================')
        print('hh -> hora')
        print('mm -> minuto')
        print('exemplo: hh:mm -> 19:00')
        print('DD -> dia')
        print('MM -> mês')
        print('YYYY -> ano')
        print('exemplo: DD-MM-YYYY -> 15-01-2003')
        print('-=' * 40 + '\n')
        
        # obtem informações importantes para o registro
        acesso_adm = input('Acesso do administrador? ')
        # obtem a data no padrão do exemplo e salva no padrão YYYY-MM-DD
        estreia = input('Data de estreia do mercado(Padrão: DD-MM-YYYY): ').strip().split('-')
        estreia = '-'.join(estreia[::-1])

        cnpj = input('CNPJ do estabelecimento: ')
        descricao_mercado = input('Descricao do mercado: ')
        localizacao = input('Localização do estabelecimento principal: ')
        horario_func = input('Horario de funcionamento do mercado(Padrão: hh:mm - hh:mm): ')
        email = input('Email de contanto [caso não possua tecle enter]: ')
        telefone = input('Telefone de contato[caso não possua tecle enter]: ')
        dados = (acesso_adm, cnpj, estreia, descricao_mercado, localizacao, horario_func, email, telefone)

        try:
            # insere registro no banco de dados
            cursor.execute('''
            INSERT INTO mercado (
                acesso_administrador,
                cnpj,
                data_hora_estreia,
                descricao_mercado,
                endereco,
                horario_funcionamento,
                email_mercado,
                telefone_mercado)
            VALUES(?,?,?,?,?,?,?,?);
            ''', dados)
            
            conn.commit()  # salva informações
            
            # exibe mensagem de sucesso do registro
            print('\n\n')
            print('============================================'.center(90))
            print('Mercado cadastrado com sucesso!!'.center(90))
            print('============================================\n\n'.center(90))
            
            # após ser feito o registro do sistema
            # muda para seção de acesso ao sistema
            self.acesso()
        except Exception as e:
            print('Erro 0 - Registro do sistema')
        except KeyboardInterrupt:
            print('* Saindo do sistema!')
    
    def acesso(self):
        """ Gerencia o aceso ao sistema """


        try:
            # exibe mensagens de boas vindas e solicita acesso ao sistema
            print('============= Bem vindo ao sistema ==================\n\n')
            acesso = input('Digite seu acesso: ')
            
            # busca no registro de funcionários se há algum funcionário com o cpf igual o acesso digitado
            cursor.execute(f'''
                SELECT * FROM funcionarios
                INNER JOIN funcao_funcionario ON funcionarios.id_funcao_funcionario = funcao_funcionario.id
                WHERE cpf="{acesso}"
                ''')
            
            # salva os resultado da busca numa variavel
            result = cursor.fetchall()
            # se o resultado for vazio(nada)
            # significa que não é um funcionário, deve-se verificar se é o acesso do administrador
            if result == []:
                # busca na tabela mercado um registro em que o acesso recebido seja igual ao acesso do adiministrador
                cursor.execute(f'SELECT * FROM mercado WHERE acesso_administrador="{acesso}"')
                result = cursor.fetchall()

                # se o resultado da nova busca for vazio(nada)
                if (result == []):
                    # significa que não é o acesso do administrador nem dos funcionário
                    # exibe mensagem "acesso não encontrado" e pede outro acesso
                    print('\nAcesso não encontrado, tente novamente!')
                    self.acesso()
                else:
                    # se não for vazio o resultado da busca, significa que o acesso é do administrador
                    self.funcionalidadeAdministrador()
            
            else:  # se o resultado da busca aos funcinarios não for vazio
                # significa que o acesso obtido foi de um funcionário
                
                # obtem o nome da função
                funcao = result[0][-3]
                
                # chama uma função especifica de acordo com a função do funcionário que ta tentando acessar o sistema
                if funcao == 'operador de caixa':
                    self.funcionalidadeOperador()
                
                elif funcao == 'estoquista':
                    self.funcionalidadeEstoquista()
                
                elif funcao == 'auxiliar administrativo':
                    self.funcionalidadeAuxiliar()
        
        except Exception as erro:
            print('Erro 0 - Acesso do sistema')
        except KeyboardInterrupt:
            print('* Saindo do sistema!')
    
    def funcionalidadeAuxiliar(self):
        try:
            while True:
                sleep(.5)
                print('''
        ============================== Funcionalidades ==============================
            01 - Registrar no sistema uma nova função(dos funcionários)
            02 - Registrar no sistema um novo funcionário.
            03 - Registrar no sistema uma nova categoria.
            04 - Registrar no sistema um novo produto.
            05 - Registrar no sistema uma nova mensagem áos fornecedores.
            06 - Registrar no sistema relatório de alteração.
            07 - Registrar no sistema um gasto realizado.
            08 - Visualizar o historico de compra.
            09 - Visualizar lista com as finanças.
            10 - Visualizar categorias presente.
            11 - Visualizar lista dos produtos em estoque.
            12 - Visualizar lista de funcionários.
            13 - Visualizar lista das funções dos funcionários.
            14 - Visualizar relatórios feitos pelo estoquista.
            15 - Visualizar a lista dos fornecedores de produtos do mercado.
            16 - Visualizar mensagens áos fornecedores.
            17 - Atualizar perfil de algum funcionário.
            18 - Sair do sistema.
            ''')
                opcao = int(input('\t Numero da opção: '))

                if (opcao == 1):
                    self.auxiliar.cadastraFuncao()

                    novos_cadastro = int(input('Digite [1] para cadastrar outro funcionário ou [0] para voltar ao menu: '))
                    
                    while (novos_cadastro == 1):
                        self.auxiliar.cadastraFuncao()
                        novos_cadastro = int(input('Digite [1] para cadastrar outro funcionário ou [0] para voltar ao menu: '))
                
                elif (opcao == 2):
                    self.auxiliar.cadastraFuncionario()
                    # pergunta se deseja cadastrar novo funcionario ou se deseja voltar ao menu
                    novos_cadastro = int(input('Digite [1] para cadastrar outro funcionario ou [0] para voltar ao menu: '))

                    while (novos_cadastro == 1):
                        self.auxiliar.cadastraFuncionario()
                        novos_cadastro = int(input('Digite [1] para cadastrar outro funcionario ou [0] para voltar ao menu: '))

                        if novos_cadastro not in (0, 1):
                            showTitleCustom('** Opção invalida.')
                        elif novos_cadastro == 0:
                            continue
                
                elif (opcao == 3):
                    self.auxiliar.cadastraCategoria()

                    novos_cadastro = int(input('Digite [1] para continuar o cadastro de categoria ou [0] para voltar ao menu:'))

                    while (novos_cadastro == 1):
                        self.auxiliar.cadastraCategoria()
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de categoria ou [0] para voltar ao menu:'))
                
                elif (opcao == 4):
                    self.auxiliar.cadastraProduto()

                    novos_cadastro = int(input('Digite [1] para continuar o cadastro de produto ou [0] para voltar ao menu:'))

                    while (novos_cadastro == 1):
                        self.auxiliar.cadastraProduto()
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de produto ou [0] para voltar ao menu:'))
                
                elif (opcao == 5):
                    self.auxiliar.registraMensagemFornecedor()
                
                elif (opcao == 6):
                    self.auxiliar.RegistraRelatorioAlterações()
                
                elif (opcao == 7):
                    self.auxiliar.registraGasto()
                
                elif (opcao == 8):
                    self.auxiliar.exibeHistoricoCompra()
                
                elif (opcao == 9):
                    self.auxiliar.exibeFinancas()
                
                elif (opcao == 10):
                    self.auxiliar.exibeCategoria()
                
                elif (opcao == 11):
                    self.auxiliar.exibeDadosEstoque()
                
                elif (opcao == 12):
                    self.auxiliar.exibeListaFuncionario()
                
                elif (opcao == 13):
                    self.auxiliar.exibeFuncao()
                
                elif (opcao == 14):
                    self.auxiliar.exibeRelatorioEstoquista()
                
                elif (opcao == 15):
                    self.auxiliar.exibeFornecedores()
                
                elif (opcao == 16):
                    self.auxiliar.exibeMensagensFornecedor()
                
                elif (opcao == 17):
                    self.auxiliar.alteraDadosFuncionario()
                
                elif (opcao == 18):
                    break
                
                else:
                    print('Essa opção não existe...\n')

                continua = input('Click [enter] pra voltar ao menu! ')
        except KeyboardInterrupt:
            print('* Fechando aplicação de sistema de mercado.')
        except ValueError:
            print('* Erro 2 - É esperado que seja digitado um número!')
            self.funcionalidadeAuxiliar()
    
    def funcionalidadeAdministrador(self):
        try:
            while True:
                sleep(.5)
                print('''
        ============================== Funcionalidades ==============================
            01 - Registrar nova função(dos funcionários)
            02 - Registrar novo funcionário.
            03 - Registrar nova categoria.
            04 - Registrar novo produto.
            05 - Registrar novo fornecedor
            06 - Visualizar historico de compras.
            07 - Visualizar finanças.
            08 - Visualizar categorias presentes.
            09 - Visualizar produtos em estoque.
            10 - Visualizar lista de funcionários.
            11 - Visualizar funções dos funcionários.
            12 - Visualizar relatórios feitos pelo auxiliar.
            13 - Visualizar relatórios feito pelo estoquista.
            14 - Visualizar lista de fornecedores
            15 - Visualizar mensagens aos fornecedores.
            16 - Atualizar perfil de algum funcionário.
            17 - Atualizar informações no regitro do mercado.
            18 - Atualizar informações das funções dos funcionários.
            19 - Sair do sistema. ''')

                opcao = int(input('\t Numero da opção: '))

                if (opcao == 1):
                    self.admin.cadastraFuncao()

                    novos_cadastro = int(input('Digite [1] para cadastrar outra função ou [0] para voltar ao menu: '))
                    
                    while novos_cadastro not in (0, 1):
                        novos_cadastro = int(input('Digite [1] para cadastrar outra função ou [0] para voltar ao menu: '))
                    
                    while (novos_cadastro == 1):
                        self.admin.cadastraFuncao()
                        novos_cadastro = int(input('Digite [1] para cadastrar outra função ou [0] para voltar ao menu: '))

                    if novos_cadastro == 0:
                        continue
                
                elif (opcao == 2):
                    self.admin.cadastraFuncionario()
                    # pergunta se deseja cadastrar novo funcionario ou se deseja voltar ao menu
                    novos_cadastro = int(input('Digite [1] para cadastrar outro funcionario ou [0] para voltar ao menu: '))

                    while novos_cadastro not in (0, 1):
                        novos_cadastro = int(input('Digite [1] para cadastrar outro funcionario ou [0] para voltar ao menu: '))
                    
                    while (novos_cadastro == 1):
                        self.admin.cadastraFuncionario()
                        novos_cadastro = int(input('Digite [1] para cadastrar outro funcionario ou [0] para voltar ao menu: '))
                        
                    if novos_cadastro == 0:
                        continue
                
                elif (opcao == 3):
                    self.admin.cadastraCategoria()
                    novos_cadastro = int(input('Digite [1] para continuar o cadastro de categoria ou [0] para voltar ao menu: '))
                    
                    while novos_cadastro not in (0, 1):
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de categoria ou [0] para voltar ao menu: '))
                    
                    while (novos_cadastro == 1):
                        self.admin.cadastraCategoria()
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de categoria ou [0] para voltar ao menu: '))

                    if novos_cadastro == 0:
                        continue

                
                elif (opcao == 4):
                    self.admin.cadastraProduto()

                    novos_cadastro = int(input('Digite [1] para continuar o cadastro de produto ou [0] para voltar ao menu: '))

                    while novos_cadastro not in (0, 1):
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de produto ou [0] para voltar ao menu: '))

                    while (novos_cadastro == 1):
                        self.admin.cadastraProduto()
                        novos_cadastro = int(input('Digite [1] para continuar o cadastro de produto ou [0] para voltar ao menu: '))
                    
                    if novos_cadastro == 0:
                        continue
                
                elif (opcao == 5):
                    self.admin.registrarFornecedor()
                
                elif (opcao == 6):
                    self.admin.exibeHistoricoCompra()
                
                elif (opcao == 7):
                    self.admin.exibeFinancas()
                
                elif (opcao == 8):
                    self.admin.exibeCategoria()
                
                elif (opcao == 9):
                    self.admin.exibeDadosEstoque()
                
                elif (opcao == 10):
                    self.admin.exibeListaFuncionario()
                
                elif (opcao == 11):
                    self.admin.exibeFuncao()
                
                elif (opcao == 12):
                    self.admin.exibeRelatorioAuxiliar()
                
                elif (opcao == 13):
                    self.admin.exibeRelatorioEstoquista()
                
                elif (opcao == 14):
                    self.admin.exibeFornecedores()
                
                elif (opcao == 15):
                    self.admin.exibeMensagensFornecedor()
                
                elif (opcao == 16):
                    self.admin.alteraDadosFuncionario()
                    novos_cadastro = int(input('Digite [1] para continuar alterando perfil de funcionario ou [0] para voltar ao menu: '))

                    while novos_cadastro not in (0,1):
                        novos_cadastro = int(input('Digite [1] para continuar alterando perfil de funcionario ou [0] para voltar ao menu: '))
                    
                    while (novos_cadastro == 1):
                        self.admin.alteraDadosFuncionario()
                        novos_cadastro = int(input('Digite [1] para continuar alterando perfil de funcionario ou [0] para voltar ao menu: '))
    
                    if novos_cadastro == 0:
                        continue
                
                elif (opcao == 17):
                    self.admin.alteraCadastroMercado()
                
                elif (opcao == 18):
                    self.admin.alteraDadosFuncao()
                
                elif (opcao == 19):
                    break
                
                else:
                    print('Essa opção não existe...\n')

                continua = input('Click [enter] pra voltar ao menu! ')
        except ValueError:
            print('* Erro 2 - É esperado que seja digitado um número.')
            self.funcionalidadeAdministrador()
        except KeyboardInterrupt:
            print('* Fechando aplicação de sistema de mercado.')


    def funcionalidadeOperador(self):
        try:
            while True:
                sleep(.5)
                print('''
        ============================== Funcionalidades ==============================
            01 - Adcionar item de compra.
            02 - Remover item de compra.
            03 - Finalizar Compra
            04 - Visualizar items de compras atuais
            05 - Sair do sistema
            ''')
                
                opcao = int(input('Numero da opção: '))
                print()
                
                if (opcao == 1):
                    self.operador.addItemProduto()
                    # pergunta se deve continuar adcionando item ou se deseja voltar ao menu
                    continua_adcionando = int(input('\nDigite [1] para continuar acrescentando item ou [0] para voltar para o menu.\n\t>>> '))
                    
                    while (continua_adcionando == 1):
                        self.operador.addItemProduto()
                        continua_adcionando = int(input('\nDigite [1] para continuar acrescentando item ou [0] para voltar para o menu.\n\t>>> '))
                
                elif (opcao == 2):
                    self.operador.removeItemProduto()
                    # pergunta se deve continuar removendo item ou se deseja voltar ao menu
                    continua_removendo = int(input('\nDigite [1] para continuar removendo item ou [0] para voltar para o menu.\n\t>>> '))
                    
                    while (continua_removendo == 1):
                        self.operador.removeItemProduto()
                        continua_removendo = int(input('\nDigite [1] para continuar removendo item ou [0] para voltar para o menu.\n\t >>> '))
                
                elif (opcao == 3):
                    self.operador.finalizaCompra()
                
                elif (opcao == 4):
                    self.operador.exibeItemsCompras()
                elif (opcao == 5):
                    break
                
                else:
                    print('Essa opção não existe...\n')
        except KeyboardInterrupt:
            print('* Fechando aplicação de sistema de mercado.')
        except ValueError:
            print('Erro 2 - É esperado que seja digitado um número.')
            self.funcionalidadeOperador()
    
    def funcionalidadeEstoquista(self):
        try:
            while True:
                sleep(.5)
                print('''
        ============================== Funcionalidades ==============================
            01 - Registrar um relatorio
            02 - Exibir uma lista com as categorias atuais no sistema
            03 - Exibir uma lista com os produtos presente no sistema
            04 - Alterar algum item de produto
            05 - sair do sistema
            ''')

                opcao = int(input('Numero da opção: '))
                print()

                if (opcao == 1):
                    self.estoquista.registraRelatorio()
                
                elif (opcao == 2):
                    self.admin.exibeCategoria()

                elif (opcao == 3):
                    self.admin.exibeDadosEstoque()
                
                elif (opcao == 4):
                    self.estoquista.alteraEstoque()
                
                elif (opcao == 5):
                    break

                else:
                    print('Essa opção não existe...\n')
        except KeyboardInterrupt:
            print('* Fechando aplicação de sistema de mercado.')
        except ValueError:
            print('Erro 2 - É esperado que seja digitado um número.')

if __name__ == '__main__':
    Mercado()