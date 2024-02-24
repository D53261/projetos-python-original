from abc import ABCMeta, abstractmethod

class Produto(metaclass=ABCMeta):
    def __init__(self, nome, preco, descricao):
        self._nome = nome
        self.preco = preco
        self._descricao = descricao
        self.preco_atual = 0

    @abstractmethod
    def calcular_desconto(self):
        return self.preco

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def __str__(self):
        return f'Produto: {self._nome} / Descrição: {self.descricao} / Preço: {self.preco_atual}'

class Livro(Produto):
    def __init__(self, nome, preco, descricao, ficcao=False):
        super().__init__(nome, preco, descricao)
        self.ficcao = ficcao

    def calcular_desconto(self):
        if self.ficcao == False:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.1)
        else:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.05)


class Eletronico(Produto):
    def __init__(self, nome, preco, descricao, velho_demais=False):
        super().__init__(nome, preco, descricao)
        self.velho_demais = velho_demais

    def calcular_desconto(self):
        if self.velho_demais == False:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.15)
        else:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.08)

class Roupas(Produto):
    def __init__(self, nome, preco, descricao, de_verao=False):
        super().__init__(nome, preco, descricao)
        self.de_verao = de_verao

    def calcular_desconto(self):
        if self.de_verao == False:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.20)
        else:
            self.preco_atual = self.preco - (super().calcular_desconto() * 0.10)

class Promocao:
    def __init__(self, dia_inicio, dia_fim, desconto_promocional):
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.desconto_promocional = desconto_promocional

    def descontar(self, data_atual):
        if data_atual >= self.dia_inicio and data_atual <= self.dia_fim:
            print('A promoção ainda esta em vigor!!')
            self.preco_atual -= self.preco_atual * self.desconto_promocional
        else:
            print('O prazo da promoção terminou!!')

class Lista:
    def __init__(self, nome, produtos):
        self.nome = nome
        self.produtos = produtos

    def __getitem__(self, item):
        return self.produtos[item]

    def __len__(self):
        return len(self.produtos)

livro = Livro("Harry Potter", 50.0, "Um bom livro", False)
livro.calcular_desconto()


eletronico = Eletronico("SmartWach", 300.0, "Um bom aparelho", True)
eletronico.calcular_desconto()


roupa = Roupas("T-shirt", 60.0, "Uma boa camiseta", True)
roupa.calcular_desconto()


listinha = [livro, eletronico, roupa]
lista = Lista("lista", listinha)

for produto in lista:
    print(produto)

print(f"Tamanho da lista: {len(lista)}")



