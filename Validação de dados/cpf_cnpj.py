from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError ("Quantidade de digitos esta incorreta!!!")
        
class DocCpf:
    def __init__(self,documento):
        if self.valida(documento):
            self._cpf = documento
        else:
            raise ValueError("Cpf inválido!!!")
        
    def __str__(self):
        return self.formatado()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)        
    
    def formatado(self):
        mascara = CPF()
        return mascara.mask(self._cpf)
    
class DocCnpj:
    def __init__(self,documento):
        if self.valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!!")
        
    def __str__(self):
        return self.formatado()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)        
    
    def formatado(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)

"""
class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self._tipo_documento = tipo_documento
        documento = str(documento)        
        if self._tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self._cpf = documento
            else:
                raise ValueError ("CPF invalido!!")
        elif self._tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self._cnpj = documento
            else:
              raise ValueError ("CNPJ invalido!!")  
        else:
            raise ValueError ("Documento invalido!!")


    def __str__(self):
        if self._tipo_documento == "cpf":
            return self.cpf_formatado()
        else:
            return self.cpnj_formatado()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError ("Quantidade de digitos inválida")
        
    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self._cpf)

    def cnpj_eh_valido(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError ("Quantidade de digitos inválida")
        
    def cpnj_formatado(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)
"""
