import random
from abc import ABCMeta, abstractmethod

class MediaItem(metaclass=ABCMeta):
    def __init__(self, nome, autor, ano_de_lancamento):
        self.nome = nome
        self.autor = autor
        self.ano_de_lancamento = ano_de_lancamento
        self.tamanho = 0
        self.likes = 0

    @abstractmethod
    def __str__(self):
        return f'Nome: {self.nome} - Autor/Criador: {self.autor} - Data de lançamento: {self.ano_de_lancamento}'
    
    
class Book(MediaItem):
    def __init__(self, nome, autor, ano_de_lancamento, paginas):
        super().__init__(nome, autor, ano_de_lancamento)
        self.paginas = paginas
        self.likes = random.randrange(1, 21)

    def calcula_tamanho(self):
        self.tamanho = self.paginas * 0.0029
        return self.tamanho
    
    def __str__(self):
        return f'Nome: {self.nome} - Autor/Criador: {self.autor} - Data de lançamento: {self.ano_de_lancamento} - Quantidade de páginas: {self.paginas}'

class Movie(MediaItem):
    def __init__(self, nome, autor, ano_de_lancamento, duracao):
        super().__init__(nome, autor, ano_de_lancamento)
        self.duracao = duracao
        self.likes = random.randrange(1, 21)

    def calcula_tamanho(self):
        self.tamanho = self.duracao * 15
        return self.tamanho
    
    def __str__(self):
        return f'Nome: {self.nome} - Autor/Criador: {self.autor} - Data de lançamento: {self.ano_de_lancamento} - Duração em minutos: {self.duracao}'

class Song(MediaItem):
    def __init__(self, nome, autor, ano_de_lancamento, genero, duracao):
        super().__init__(nome, autor, ano_de_lancamento)
        self.genero = genero
        self.duracao = duracao
        self.likes = random.randrange(1, 21)

    def calcula_tamanho(self):
        self.tamanho = self.duracao * 0.002344
        return self.tamanho

    def __str__(self):
        return f'Nome: {self.nome} - Autor/Criador: {self.autor} - Data de lançamento: {self.ano_de_lancamento} - Genero musical: {self.genero} - Duração em segundos: {self.duracao}'
    
class Library:
    def __init__(self):
        self.colecao = []

    def adiciona_item(self, item):
        self.colecao.append(item)
        print(f'{item.nome} adicionado a lista')

    def exclui_item(self, nome):
        if not self.colecao:
            print("Não há itens!!!")
        for midia in self.colecao:
            if nome == midia.nome:
                self.colecao.remove(midia)
                print(f'{midia.nome} removido da lista')
                return
        print('Item não encontrado!')

    def procura_item_nome(self, nome):
        if not self.colecao:
            print("Não há itens!!!")
        else:
            for item in self.colecao:
                if item.nome == nome:
                    print(f'Item encontrado!!\n{print(item)}')
                    return
            print('Item não encontrado!!')  

    def procura_item_autor(self, autor):
        if not self.colecao:
            print("Não há itens!!!")
        else:
            for item in self.colecao:
                if item.autor == autor:
                    print(f'Item encontrado!!\n{print(item)}')
                    return
            print('Item não encontrado!!')

    def calcula_tamanho_geral(self):
        if not self.colecao:
            print("Não há itens!!!")
        else:
            tamanho = 0
            for item in self.colecao:
                item.calcula_tamanho()
                tamanho += item.tamanho
            print(f'Tamanho geral: {tamanho} MB')
    
    def mostra_lista(self):
        if not self.colecao:
            print("Não há itens!!!")
        else:
            for item in self.colecao:
                print(item)

    def recomenda_item(self):
        if not self.colecao:
            print("Não há itens!!!")
        else:
            likes = []
            for item in self.colecao:
                likes.append(item.likes)
            maior = max(likes)

            for item in self.colecao:
                if item.likes == maior:
                    print(f'Uma boa recomendação por numero de likes é {item.nome}, possuindo {item.likes}')
                    return

def main():
    biblioteca = Library()

    print("Bem vindo ao site de biblioteca virtual, contendo diferentes arquivos para lhe satisfazer!")
    while True:
       
        print("Opção 1: adicionar item")
        print("Opção 2: excluir item")
        print("Opção 3: procurar item")
        print("Opção 4: calcular tamanho em disco")
        print("Opção 5: recomendar item")
        print("Opção 6: mostrar todos os itens")
        print("Opção 7: sair")
        escolha = input("Digite a opção: ")

        if escolha == "1":
            print("Opção 1: livro")
            print("Opção 2: filme")
            print("Opção 3: musica")
            escolha2 = int(input("Digite a opção: "))

            if escolha2 == 1:
                nome = input("Digite o nome do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = int(input("Digite o ano em que o livro foi lançado: "))
                pag = int(input("Digite o numero de paginas do livro: "))
                nome = Book(nome, autor, ano, pag)
                biblioteca.adiciona_item(nome)
                print(nome)

            elif escolha2 == 2:
                nome = input("Digite o nome do filme: ")
                autor = input("Digite o criador do filme: ")
                ano = int(input("Digite o ano em que o filme foi lançado: "))
                duracao = int(input("Digite a duração em minutos do filme: "))
                nome = Movie(nome, autor, ano, duracao)
                biblioteca.adiciona_item(nome)
                print(nome)

            elif escolha2 == 3:
                nome = input("Digite o nome da musica: ")
                autor = input("Digite o autor da musica: ")
                ano = int(input("Digite o ano em que a musica foi lançado: "))
                genero = input("Digite o genero musical a que a musica pertence: ")
                duracao = int(input("Digite a duração em segundos da musica: "))
                nome = Song(nome, autor, ano, genero, duracao)
                biblioteca.adiciona_item(nome)
                print(nome)

            else: 
                print("Escolha uma opção valida...")

        elif escolha == "2":
            excluido = input("Digite o item a ser excluido: ")
            biblioteca.exclui_item(excluido)
        
        elif escolha == "3":
            print("Opção 1: procurar pelo nome")
            print("Opção 2: procurar pelo autor")
            escolha3 = int(input("Digite a opção: "))

            if escolha3 == 1:
                procura = input("Digite o nome do item procurado: ")
                biblioteca.procura_item_nome(procura)
            
            elif escolha3 == 2:
                procura = input("Digite o autor do item procurado: ")
                biblioteca.procura_item_autor(procura)

            else: 
                print("Escolha uma opção valida...")

        elif escolha == "4":
            biblioteca.calcula_tamanho_geral()

        elif escolha == "5":
            biblioteca.recomenda_item()

        elif escolha == "6":
            biblioteca.mostra_lista()
        
        elif escolha == "7":
            print("Saindo...")
            break

        else: 
            print("Escolha uma opção valida...")

if __name__ == "__main__":
    main()

