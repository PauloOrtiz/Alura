#url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

url = ""
#Sanitização da URL
url = url.strip


#Validação do URL
if url == "":
    raise ValueError("A URL está vazia")

#Separa base e paramentos
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmentos
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


def get_url_parametros(self):
    indice_interrogacao = self.url.find('?')
    url_parametros = self.url[indice_interrogacao + 1:]
    return url_parametros





















