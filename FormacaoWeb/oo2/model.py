class Filme:
    def __init__(self, nome, ano , duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes (self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:

    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()

print("Nome: {} - Ano {} - Duracao:{} - Likes {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
atlanta = Serie('atlanta', 2016, 2)
atlanta.dar_like()

print("Nome: {} - Ano {} - Temporadas:{} - Likes : {}".format(atlanta.nome, atlanta.ano, atlanta.temporada, atlanta.likes))