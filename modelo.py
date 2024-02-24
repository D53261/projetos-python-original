from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title

    @abstractmethod
    def __str__(self):
        return "{} - {} - {} likes".format(self._nome, self.ano, self._likes)

class Verificacao:
    def bom_ou_nao(self):
        if(self._likes <= 4):
            print(f'{self._nome} está ruim!')
        else:
            print(f'{self._nome} está bom!')

class Filme(Programa, Verificacao):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} min - {} likes".format(self._nome, self.ano,self.duracao, self._likes)

class Serie(Programa, Verificacao):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "{} - {} - {} temporadas - {} likes".format(self._nome, self.ano, self.temporadas, self._likes)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)




vingadores = Filme('Vingadores - Guerra Infinita', 2017, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.bom_ou_nao()

ragnarock = Serie('Ragnarock', 2020, 6)
ragnarock.dar_likes()
ragnarock.dar_likes()
ragnarock.dar_likes()
ragnarock.dar_likes()
ragnarock.bom_ou_nao()


the_flash = Serie('The flash', 2015, 9)
the_flash.dar_likes()
the_flash.dar_likes()

PJ = Filme("Percy jackson e o ladrão de raios", 2010, 100)
PJ.dar_likes()
PJ.dar_likes()
PJ.dar_likes()
PJ.dar_likes()
PJ.dar_likes()
PJ.dar_likes()

supernatural = Serie('Supernatural', 2017, 9)
supernatural.dar_likes()
supernatural.dar_likes()
supernatural.dar_likes()
supernatural.dar_likes()
supernatural.dar_likes()
supernatural.dar_likes()
supernatural.dar_likes()


filmes_e_series = [vingadores, ragnarock, the_flash, PJ, supernatural]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
print("Tamanho da playlist: {} itens".format(len(playlist_fim_de_semana)))

for programa in playlist_fim_de_semana:
    print(programa)

