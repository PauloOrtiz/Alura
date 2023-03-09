import requests
class BuscaEndereco:
    
    def __init__(self,cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self._cep = cep
        else:
            raise ValueError ("Cep invalido!!!!")
    
    def __str__(self):
        return self.cep_formatado()

    def cep_eh_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def cep_formatado(self):
        return "{}-{}".format(self._cep[:5], self._cep[5:])
    
    def acessa_via_cep(self):
        url ="https://viacep.com.br/ws/{}/json".format(self._cep)
        r = requests.get(url)
        dados = r.json()
        return {
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        }