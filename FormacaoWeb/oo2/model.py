class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2016, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie("Demolidor", 2016, 3)
vingadores.dar_like()
vingadores.dar_like()

print("Nome: {} - Ano {} - Duracao:{} - Likes {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
atlanta.dar_like()

print("Nome: {} - Ano {} - Temporadas:{} - Likes : {}".format(atlanta.nome, atlanta.ano, atlanta.temporada, atlanta.likes))

filmes_e_serie = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_serie)

print("Tamanho do playlist: {}".format(len(playlist_fim_de_semana)))


for programa in playlist_fim_de_semana:
    print(programa)