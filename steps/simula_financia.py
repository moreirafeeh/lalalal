import time

@given(u'Santander Financimentos')
def step_impl(context):
    #context.main.acessa_financia_veiculo()
    #time.sleep(5)  
    pass


@when(u'Preencher Dados do veiculo')
def step_impl(context):
    time.sleep(4)
    context.financa.preenche_dados_veiculos()
    pass


@then(u'Botao Continuar Habilitado')
def step_impl(context):
    pass


@when(u'Preencher Dados Pessoais')
def step_impl(context):
    context.financa.preenche_dados_pessoais()
    pass


@then(u'Preço do financimento')
def step_impl(context):
    pass