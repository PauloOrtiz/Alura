from codigo.bytebank import Funcionario

#lucas = Funcionario("Lucas Carvalho", "13/03/2000", 1000)

#print(lucas.idade())


def teste_idade():
    funcionario_teste = Funcionario('teste', "13/03/2000", 1111)
    print('Teste igual = {}'.format(funcionario_teste.idade()))

teste_idade()