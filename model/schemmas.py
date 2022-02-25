from model.TabCategoria import criaTabCategorias
from model.TabProdutos import criaTabProdutos
from model.TabFuncaoFuncionario import criaTabFuncaoFuncionario
from model.TabFuncionarios import criaTabFuncionarios
from model.TabAlteracaoAuxilar import criaTabAlteraçõesAuxiliar
from model.TabRelatorioEstoquista import criaTabRelatorioEstoquista
from model.TabHistoricoCompras import criaTabHistoricoCompras
from model.TabFinancas import criaTabFinancas
from model.TabFornecedores import criaTabFornecedores
from model.TabMensagensFornecedores import criaTabMensagensFornecedores
from model.TabMercado import criaTabMercado
from model.TabCompraProdutos import criaTabCompraProduto

def setup():
    criaTabAlteraçõesAuxiliar()
    criaTabFuncaoFuncionario()
    criaTabFuncionarios()
    criaTabHistoricoCompras()
    criaTabFornecedores()
    criaTabMensagensFornecedores()
    criaTabFinancas()
    criaTabCategorias()
    criaTabProdutos()
    criaTabRelatorioEstoquista()
    criaTabMercado()
    criaTabCompraProduto()
