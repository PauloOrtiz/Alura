endereco = "Rua da Flores 72, apartamento 1002, laranjeiiras, Rio de Janeiro, RJ, 23440120"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)




url ="www.bytebank.com.br/cambio"


print("A URL é Valida")

