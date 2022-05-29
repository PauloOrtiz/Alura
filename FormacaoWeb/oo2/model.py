class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes (self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return "{} - {} - {} likes".format(self._nome, self.ano, self._likes)


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} min - {} likes".format(self._nome, self.ano, self.duracao, self._likes)

class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return "{} - {} - {} tp - {} likes".format(self._nome, self.ano, self.temporada, self._likes)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()

print("Nome: {} - Ano {} - Duracao:{} - Likes {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
atlanta = Serie('atlanta', 2016, 2)
atlanta.dar_like()

print("Nome: {} - Ano {} - Temporadas:{} - Likes : {}".format(atlanta.nome, atlanta.ano, atlanta.temporada, atlanta.likes))

filmes_e_serie = [vingadores, atlanta]

for programa in filmes_e_serie:
    print(programa)