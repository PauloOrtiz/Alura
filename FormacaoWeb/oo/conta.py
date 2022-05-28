
class Conta:

    def __init__(self, numero, titular, saldo, limite):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = (self.__saldo + self.__limite)
        return valor <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O saldo insuficiente, saldo atual é R${}".format(self.__saldo))

    def transferir(self, valor, destino):

        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return print(self.__saldo)

    @property
    def titula(self):
        return print(self.__titular)

    @property
    def limite(self):
        return print(self.__limite)

    @property
    def numero(self):
        return print(self.__numero)

    @limite.setter
    def limite(self, limite):
       self.__limite = limite

    @staticmethod
    def codigo_banco(self):
        return print(self.__codigo_banco)