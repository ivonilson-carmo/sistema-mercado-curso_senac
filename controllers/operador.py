from datetime import datetime
from conn import conn, cursor
from utils.utils import showTitleCustom


class Operador:
    def __init__(self):
        self.produtosCompra = []
        self.valorTotalProdutos = float()
        self.tipoPagamento = str()
        self.valorRecebido = float()
        self.trocoPagamento = float()
        self.notaFiscal = ''
    
    def addItemProduto(self):
        """ insere um item na lista de items da compra atual"""
        try:
            # solicita o codigo do produto(codigo de barras)
            produto = int(input('\n Digite o codigo do produto: '))
            # verifica se existe no sistema
            cursor.execute(f'SELECT * FROM produtos WHERE codigo="{produto}" ')
            result = cursor.fetchall()
            # se não existir, exibe mensagem e volta ao menu
            if result == []:
                showTitleCustom('* Produto não encontrado no sistema')
                return
            
            # o item existe, adciona o item na lista de items
            self.produtosCompra.append(produto)
            # incrementa o valor do produto a variavel valorTotalProdutos
            self.valorTotalProdutos += result[0][3]
            
            # exibe mensagem de sucesso
            showTitleCustom(
                '* Item adcionado com sucesso.',
                f'Total: R$ {self.valorTotalProdutos:.2f}'.rjust(28, '.')
            )

        except KeyboardInterrupt:
            print('Voltando ao Menu')
        except Exception:
            print('* erro 1 - adicionando items de compras\n')
    
    def removeItemProduto(self):
        """ remove um determinado item da lista de items da compra atual """
        try:
            # Se a lista de compras não tiver vazia
            if len(self.produtosCompra):
                # exibe os items da lista de compras atual
                self.exibeItemsCompras()
                # codigo de barra do item que será removido da lista
                produto = int(input('Digite o codigo do produto: '))

                # obtem o valor do item que será removido
                cursor.execute(f'SELECT valor FROM produtos WHERE codigo="{produto}"')
                valor = cursor.fetchall()[0][0]
                
                # remove o item da lista de produtos da compra atual
                del self.produtosCompra[produto]
                self.valorTotalProdutos -= valor  #diminui o valor do produto no total dos produtos
            
            else:
                print('* Lista Vazia')
        
        except KeyboardInterrupt:
            print('\n*Voltando ao menu')
        except Exception:
            print('* Erro 0 - removendo items de compras')
    
    def finalizaCompra(self):
        """ Exibe opções para voltar ao menu, desistir da compra e realizar passos para finalizar a compra """
        try:
            if self.valorTotalProdutos == 0.0:
                print('* Nenhum produto para compra :(')
            else:
                self.exibeItemsCompras()

                self.tipoPagamento = int(input('''
                Digite [1] para pagamento por cartão, [2] para pagamento por dinheiro, [3] voltar ao menu, [4] desistir da compra: '''))

                while (self.tipoPagamento not in (1,2,3, 4)):
                    print('Opção diferente da esperada, tente novamente!!\n')
                    
                    self.tipoPagamento = int(input('''
                Digite [1] para pagamento por cartão, [2] para pagamento por dinheiro, [3] voltar ao menu, [4] desistir da compra: '''))
                
                if (self.tipoPagamento == 1):
                    self.tipoPagamento = 'cartão'
                    self.recebePagamento()
                
                elif (self.tipoPagamento == 2):
                    self.tipoPagamento = 'dinheiro'
                    self.recebePagamento()
                
                elif (self.tipoPagamento == 3):
                    return
                
                self.clearHistory()

        except KeyboardInterrupt:
            print('\n* Voltando ao menu')
            self.clearHistory()
        except ValueError:
            print('\n*Erro 1 - É esperado que se digite um número')
            self.finalizaCompra()
        except Exception:
            self.clearHistory()
            print('\n*Erro 0 - Finalização de uma compra')
    
    def recebePagamento(self):
        """ Obtem o pagamento e após ser efetuado realiza registro da compra no sistema """
        try:
            print(f' {"=" * 50} \n')

            if (self.tipoPagamento == 'cartão'):
                print('* Pagamento feito por cartão!')
                continua = input('Tecle [enter] após o pagamento for efetuado ou [-1] caso não tenha funcionado!').strip()
                
                if continua == '-1':
                    return
            
            elif (self.tipoPagamento == 'dinheiro'):
                print('* Pagamento por dinheiro')
                self.valorRecebido = float(input('Valor do pagamento recebido: '))
                
                while self.valorRecebido < self.valorTotalProdutos:
                    print('Valor do pagamento insuficiente, obtenha um valor igual ou maior que o valor da compra!')
                    self.valorRecebido = float(input('Valor do pagamento recebido: '))
                
                self.trocoPagamento = self.valorRecebido - self.valorTotalProdutos
                print(f'Troco: {self.trocoPagamento:.2f}')
            
            self.RegistraAtualizacoes()
        except KeyboardInterrupt:
            print('\n* Voltando ao menu')
            self.clearHistory()
        except ValueError:
            print('\nErro 2 - É esperado que se digite um número.')
            self.recebePagamento()
        except Exception:
            print('\nerro 0 - Escolha do tipo de pagamento...')
            self.clearHistory()

    def imprimeNotaFiscal(self):
        """ Exibe nota fiscal """
        cursor.execute('SELECT cnpj,endereco,descricao_mercado FROM mercado')
        cnpj, endereco, desc = cursor.fetchall()[0]
        
        data = datetime.today().strftime("%d-%m-%Y - %H:%M") # obtem a data e hora atual
        cpf = input('Deseja cpf na nota[s/n]: ').strip().lower()

        print('\n\n* Exibindo nota Fiscal ')
        
        
        # gera nota fiscal 
        self.notaFiscal += '''
    ========================================
    {:^40}
    {:^40}
    {:^40}
    ========================================
    '''.format(data, endereco, f'{cnpj} - {desc}')
        if ((cpf == 's') or (self.valorTotalProdutos > 10000)):
            cpf = input('Digite o cpf do cliente: ')
            
            self.notaFiscal +=  f'CPF do cliente: {cpf}'.center(40)

        
        for index, itemCompra in enumerate(self.produtosCompra):
            cursor.execute(f'SELECT * FROM produtos WHERE codigo = "{itemCompra}"')
            result = cursor.fetchall()
            
            self.notaFiscal += f'\n{index} - {result[0][2].ljust(20, ".")} R$ {result[0][3]:.2f}'
        self.notaFiscal += f'\n* Total: R${self.valorTotalProdutos:.2f}'
        
        if self.trocoPagamento > 0:
            self.notaFiscal += f'\n* Valor recebido: {self.valorRecebido:.2f}'
            self.notaFiscal += f'\n* Troco: {self.trocoPagamento:.2f}\n\n'
        
        print(self.notaFiscal)
        input('Click enter para voltar ao menu.')
        self.clearHistory()
    
    def RegistraAtualizacoes(self):
        """ Registra compra realizada no sistema """
        try:
            data = datetime.today().strftime('%Y-%m-%d %H:%M')
            dados = (data, self.valorTotalProdutos, self.tipoPagamento)
            
            cursor.execute('''
            INSERT INTO historico_de_compra(
                data_horario, valor, meio_de_pagamento
            ) VALUES(?, ?, ?);
            ''', dados)
            
            conn.commit()

            self.idCompra = cursor.lastrowid

            for item in self.produtosCompra:
                cursor.execute(f'SELECT valor, quantidade FROM produtos WHERE codigo = {item}')
                valor, quant = cursor.fetchall()[0]
                id = cursor.execute(f'SELECT id FROM produtos WHERE codigo={item}')
                id = cursor.fetchall()[0][0]

                
                cursor.execute('INSERT INTO compra_produtos (id_compra, valor, id_produto) VALUES(?,?,?)', (self.idCompra, valor, id))
                newQuant = quant - 1
                cursor.execute(f'UPDATE produtos SET quantidade = {newQuant} WHERE id = {id}')
                
            
            conn.commit()

            self.imprimeNotaFiscal()
        except KeyboardInterrupt:
            print('* Voltando ao menu')
            self.clearHistory()
        except ValueError:
            print('\nErro 1 - É Esperado que se digite um número')
            self.clearHistory()
        except Exception as e:
            self.clearHistory()
            print('Erro 0 - Registra compra realizada no sistema.')
    
    def clearHistory(self):
        """ Retorna os valores padrão das variaveis importantes para a compra. """
        self.produtosCompra.clear()
        self.valorRecebido = 0.0
        self.trocoPagamento = 0.0
        self.notaFiscal = ''
        self.valorTotalProdutos = 0.0

    def exibeItemsCompras(self):
        # Exibe lista dos items de compra atual
        if (self.valorTotalProdutos > 0):
            for index, itemCompra in enumerate(self.produtosCompra):
                cursor.execute(f'SELECT * FROM produtos WHERE codigo = "{itemCompra}"')
                result = cursor.fetchall()
                
                print(f'{index} - {result[0][2].ljust(20, ".")} R$ {result[0][3]:.2f}')
            print(f'* Total: R${self.valorTotalProdutos:.2f}')
        else:
            print('* Nã há nenhum item na lista de compra atual')
