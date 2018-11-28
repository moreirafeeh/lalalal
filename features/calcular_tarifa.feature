Feature: Financiamento de Veiculo

Scenario: Calcular Financimanto

    Given Santander Financimentos
    When Preencher Dados do veiculo
    Then Botao Continuar Habilitado
    When Preencher Dados Pessoais
    Then Preco do financimento