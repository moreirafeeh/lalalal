
"""		Pyautomator Framework de teste 

			santander"""

from Pyautomators import *
from Pyautomators.web import Web
from Pyautomators import Ambiente
from pages.pages.main_page import Navegacao
from pages.pages.Financia_veiculo_page import Financiamento
from Pyautomators import Log
from time import sleep

Log.setup('log/report.log')

@Log.before_all
def before_all(context):
	
	context.app = Web('Chrome','driver/chromedriver.exe')
	context.app.maximiza()
	context.app.pagina('https://www.cliente.santanderfinanciamentos.com.br/originacaocliente/#/simulacao?ori=SB&utm_source=portal-comercial&utm_medium=link-financie-seu-veiculo')
	context.main = Navegacao(context.app)
	context.financa = Financiamento(context.app)
	



def after_all(context):
	context.app.fechar_programa()

