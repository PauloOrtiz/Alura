import re

class TelefonesBR:
    def __init__(self,telefone) -> None:
        if self.valida_telefone(telefone):
            self._numero = telefone
        else:
            raise ValueError("Numero incorreto!!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao =  "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
        
    def format_numero(self):
        padrao =  "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        reposta = re.search(padrao, self._numero)
        numero_formatado = "+{}({}){}-{}".format(
            reposta.group(1),
            reposta.group(2),
            reposta.group(3),
            reposta.group(4))
        
        return numero_formatado