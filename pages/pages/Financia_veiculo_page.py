import time
from Pyautomators.web_extensao import Teclas_para_driver 


class Financiamento():
    def __init__(self, driver):
        self.driver = driver

    def preenche_dados_veiculos(self):
        #self.driver.select(self.driver.elemento('custom ng-select ng-select-single ng-select-searchable ng-pristine ng-invalid ng-select-bottom ng-touched','class',5)).select_text('AGRALE')
        #self.driver.clica_por_text("div","tag","Selecione a marca da moto")
        #self.driver.clica('//*[@id="brandsBlock"]/ng-select/div/div/div[1]', 'xpath', implicit= 3)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', 'BMW'+Teclas_para_driver.ENTER, 'tag', 0, 10)
        time.sleep(2)
        self.driver.escrever_elemento_lista('input', '2018 DIESEL'+Teclas_para_driver.ENTER, 'tag', 1, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', 'X5 XDRIVE M50D 3.0 381CV DIESEL'+Teclas_para_driver.ENTER, 'tag', 2, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', '150000000'+Teclas_para_driver.ENTER, 'tag', 3, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', 'Alagoas'+Teclas_para_driver.ENTER, 'tag', 4, 10)
        self.driver.clica('/html/body/app-root/app-simulation/div/app-vehicle-form/div/div/div/div/form/div[2]/div[5]/div/button', 'xpath')
        time.sleep(2)
    def preenche_dados_pessoais(self):
        self.driver.escrever_elemento_lista('input', 'kimimarux@hotmail.com'+Teclas_para_driver.ENTER, 'tag', 0, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', '11965956965'+Teclas_para_driver.ENTER, 'tag', 1, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', '28/07/1996'+Teclas_para_driver.ENTER, 'tag', 2, 10)
        time.sleep(1)
        self.driver.escrever_elemento_lista('input', '42058968832'+Teclas_para_driver.ENTER, 'tag', 3, 10)
        time.sleep(1)
        self.driver.clica_por_text('/html/body/app-root/app-simulation/div/app-personal-data/div/div/div/form/div[5]/div/label[1]', 'xpath', 'Sim')
        self.driver.clica_por_text('/html/body/app-root/app-simulation/div/app-personal-data/div/div/div/form/app-dealership-autocomplete/form/div[3]/div/label', 'xpath', 'Ainda não sei onde vou comprar')
        # self.driver.escrever_elemento_lista('input', 'Sao Paulo'+Teclas_para_driver.ENTER, 'tag', 4, 10)
        # self.driver.clica('/html/body/app-root/app-simulation/div/app-vehicle-form/div/div/div/div/form/div[2]/div[5]/div/button', 'xpath')
        # time.sleep(5)
        self.driver.clica('/html/body/app-root/app-simulation/div/app-personal-data/div/div/div/form/div[7]/div[1]/div/button', 'xpath')
        time.sleep(20)
        self.driver.ActionChains.send_keys(Teclas_para_driver.TAB, Teclas_para_driver.ENTER).perform()
        self.driver.ActionChains.send_keys(Teclas_para_driver.ENTER).perform()
        time.sleep(4)
        pass

    
