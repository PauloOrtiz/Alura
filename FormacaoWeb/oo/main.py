from conta import Conta
from cliente import Cliente

conta = Conta(123, "Paulo", 55.5, 1000.0)
conta2 = Conta(321, "Carol", 100.0, 1000.0)

conta.extrato()
conta2.extrato()

conta2.transferir(10.0, conta)

conta.extrato()
conta2.extrato()

cliente = Cliente("paulo")

cliente.nome

conta.codigo_banco

