
"""		Pyautomator Framework de teste 

			santander"""

from Pyautomators import *
from Pyautomators.web import Web
from Pyautomators import Ambiente
from pages.pages.main_page import Navegacao
from pages.pages.Financia_veiculo_page import Financiamento
from time import sleep

def before_all(context):
	
	context.app = Web('Chrome','driver/chromedriver.exe')
	context.app.maximiza()
	context.app.pagina('https://www.cliente.santanderfinanciamentos.com.br/originacaocliente/#/simulacao?ori=SB&utm_source=portal-comercial&utm_medium=link-financie-seu-veiculo')
	context.main = Navegacao(context.app)
	context.financa = Financiamento(context.app)
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	pass

