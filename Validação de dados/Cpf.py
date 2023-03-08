class Cpf:
    def __init__(self, documento):
        documento == str(documento)        
        if self.cpf_eh_valido(documento):
            self._cpf = documento
        else:
            raise ValueError ("CPF invalido!!")


    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
        
     