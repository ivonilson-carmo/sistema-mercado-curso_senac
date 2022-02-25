from conn import cursor, conn
from controllers.admin import Administrador as adm
from datetime import datetime


class Estoquista:
    admin = adm()

    def registraRelatorio(self):
        """ registra relatorio na tabela relatorio_estoquista """
        try:
            # solicita o relatório
            relatorio = input('Digite seu relatório: ')
            data = datetime.today().strftime('%Y-%m-%d %H:%M')  # obtem a data atual

            # registra no sistema
            cursor.execute('''
            INSERT INTO relatorio_estoquista(data_horario, relatorio) VALUES(?,?)
            ''', (data, relatorio))
            conn.commit()
        
        except KeyboardInterrupt:
            print('Erro - Voltando ao menu')
        except Exception:
            print('Erro 0 - Registro de relatório.')
    
    def exibeDadosEstoque(self):
        """ Exibe a lista de produtos registrados no sistema """
        try:
            cursor.execute('SELECT * FROM produtos INNER JOIN categorias ON produtos.id_categoria = categorias.id')
            result = cursor.fetchall()
            
            for linha in result:
                print(f'1 - ID: {linha[0]}')
                print(f'2 - CODIGO: {linha[1]}')
                print(f'3 - NOME: {linha[2]}')
                print(f'4 - VALOR: {linha[3]}')
                print(f'5 - QUANTIDADE: {linha[4]}')
                print(f'6 - CATEGORIA: {linha[7]}')
                print('=' * 50)
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu.')
        except Exception as e:
            print('\n* Erro 0 - Exibindo dados de produtos.')

    def alteraEstoque(self):
        """ Realiza alteração de determinado produto atualmente no sistema"""
        try:
            self.exibeDadosEstoque()
            
            # solicita o identificador do produto que será modificaod
            idProd = int(input('\nDigite o identificador do produto que deseja alterar: '))
            # verifica se o identificador pertence a um produto registrado no sistema
            cursor.execute(f'SELECT * FROM produtos WHERE id={idProd}')
            result = cursor.fetchall()

            # se não pertence, exibe mensagem de erro
            if result == []:
                print('* Nada Encontrado')
                return 
            
            # Identificador inserido está correto!
            # Obtem os items do registro que vai ser alterado
            print('Digite os numeros correspondente as opções que deseja alterar ou tecle [enter] para não realizar nenhuma mudança.')
            opcao = input('\t >>> ').strip().split(' ')

            if (opcao == []):  # se for digitado enter, pula a alteração
                return
            
            for op in opcao:
                op = int(op)
                if (op == 3):
                    newNome = input('Digite novo nome do produto: ')
                    cursor.execute(f'UPDATE produtos SET nome = "{newNome}" WHERE id = {idProd}')
                
                elif (op == 4):
                    newValor = float(input('Digite novo valor do produto: '))
                    cursor.execute(f'UPDATE produtos SET valor = "{newValor}" WHERE id = {idProd}')
                
                elif (op == 5):
                    newQuantidade = int(input('Digite a nova quantidade do item: '))
                    cursor.execute(f'UPDATE produtos SET quantidade = "{newQuantidade}" WHERE id = {idProd}')
                
                elif (op == 6):
                    self.admin.exibeCategoria()

                    newCategoria = int(input('Digite o indice da nova categoria: '))

                    cursor.execute(f'SELECT * FROM categorias WHERE id = {newCategoria}')
                    result = cursor.fetchall()

                    if result == []:
                        print('* Erro ao selecionar nova categoria')
                    else:
                        cursor.execute(f'UPDATE produtos SET id_categoria = {newCategoria} WHERE id = {idProd}')
            print('* Mudanças realizadas com sucesso.')
            conn.commit()
        
        except KeyboardInterrupt:
            print('\n* Voltando ao menu.')
        except ValueError:
            print('\n* Erro 1 - É Esperado que se digite um número.')
        except Exception:
            print('\n* Erro 0 - Alterando informações do estoque.')