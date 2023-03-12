from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quanto_idade_recbe_13_03_2000_deve_retornar_23(self):
        entrada ='13/03/2000'# Given-Context
        esperado = 23

        funcionario_teste = Funcionario('Teste',entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retorna_Carvalho(self):
        entrada =' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then

    
    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() #when
        resultado = funcionario_teste.salario

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # Given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # When

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000 # Given
            
            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus() # When

            assert resultado #then