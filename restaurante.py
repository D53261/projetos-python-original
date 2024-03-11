import random

class Empregados:
    def __init__(self):
        self.funcionarios = []

    def mostra_lista(self):
        print(self.funcionarios)

class Funcionarios:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        self.id = None
        self.cargo = None
        self.salario_total = 0
        
    def define_id(self):
        numero = str(random.randint(0, 999))
        self.id = self.nome[0] + numero
        return self.id

    def calcula_salario(self):
        return self.salario_base
    
    def adiciona_funcionario(self, empregados: list):
        empregados.append([self.nome, self.id, self.cargo])


class Garçom(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.cargo = "Garçom"

    def calcula_salario(self):
        self.salario_total = (super().calcula_salario() * 0.15) + super().calcula_salario()

    def mostrar_funcionarios(self):
        for i in self.funcionarios:
            if self.funcionarios[i][2] == "Garçom":
                print(f'Nome: {self.nome} / ID: {self.__define_id()} / Salário base: {self.salario_base} / Salário total: {self.salario_total} / Cargo: {self.cargo}')
    
class Gerente(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.cargo = "Gerente"

    def calcula_salario(self):
        self.salario_total = (super().calcula_salario() * 0.2) + super().calcula_salario()

    def mostrar_funcionarios(self):
        for i in self.funcionarios:
            if self.funcionarios[i][2] == "Gerente":
                print(f'Nome: {self.nome} / ID: {self.__define_id()} / Salário base: {self.salario_base} / Salário total: {self.salario_total} / Cargo: {self.cargo}')

class Chef(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.cargo = "Chef"

    def calcula_salario(self):
        self.salario_total = (super().calcula_salario() * 0.25) + super().calcula_salario()

    def mostar_funcionarios(self):
        for i in self.funcionarios:
            if self.funcionarios[i][2] == "Chefe":
                print(f'Nome: {self.nome} / ID: {self.__define_id()} / Salário base: {self.salario_base} / Salário total: {self.salario_total} / Cargo: {self.cargo}')

class Menu:
    def __init__(self):
        self.menu_geral = []
        self.cafe = []
        self.almoco = []
        self.jantar = []

    def adicionar_item(self, nome, descricao, categoria, preco):
        item = [nome.title(), descricao, categoria, preco]
        self.menu_geral.append(item)

    def remover_item(self, item):
        if not self.menu_geral:
            print("Não há itens!!!")
        for i in self.menu_geral:
            if item.title() == i[0]:
                self.menu_geral.remove(i)
                print(f"Item {item} removido!!")
                return
            print("Item não encontrado!!")
    
    def classificar_itens(self):
        if not self.menu_geral:
            print("Não há itens!!!")
        for i in self.menu_geral:
            if i[2] == 1:
                self.cafe.append(i)
                print("Item adicionado ao menu Café da manhã!!")
            elif i[2] == 2:
                self.almoco.append(i)
                print("Item adicionado ao menu Almoço")
            elif i[2] == 3:
                self.jantar.append(i)
                print("Item adicionado ao menu Jantar")

    def procura_item(self):
        if not self.menu_geral:
            print("Não há itens!!!")
        escolha = int(input("Opção 1: Mostrar determinada categoria \nOpção 2: Procurar item manualmente \nDigite a opção: "))
        if escolha == 1:
            escolha2 = int(input("Opção 1: Café da manhã \nOpção 2: Almoço \nOpção 3: Jantar \nDigite a opção: "))
            if escolha2 == 1:
                if not self.cafe:
                    print("Não há itens!!!")
                else:
                    print(f'Café da Manhã: {self.cafe}')
            elif escolha2 == 2:
                if not self.almoco:
                    print("Não há itens!!!")
                else:
                    print(f'Almoço: {self.almoco}')
            elif escolha2 == 3:
                if not self.jantar:
                    print("Não há itens!!!")
                else:
                    print(f'Jantar: {self.jantar}')
        
        elif escolha == 2:
            if not self.menu_geral:
                print("Não há itens!!!")
            else:
                procura = input("Digite o nome do alimento procurado: ").title()
                for item in self.menu_geral:
                    if item[0] == procura:
                        print(f'Item encontrado!!\n{item}')
                        return
                print('Item não encontrado!!')

class Financeiro:
    def __init__(self):
        self.receita = 0

    def __str__(self):
        return f'Receita do dia: {self.receita}'

class Pedidos:
    def __init__(self, cliente_nome):
        self.cliente_nome = cliente_nome
        self.responsavel = None
        self.pedido = []

    def adicionar_pedido(self, menu, pedido):
        for i in menu.menu_geral:
            if pedido == i[0]:
                self.pedido.append(i)
                return
        print("Esse item solicitado não existe!!")

    def responsavel_pedido(self, empregados):
        garcom = []
        for i in empregados.funcionarios:
            if i[2] == "Garçom":
                garcom.append(i)
        if garcom:
            self.responsavel = random.choice(garcom)
        else:
            print("Não há garçons disponíveis!")



    def __str__(self):
        return f'Nome: {self.cliente_nome} \nPedido: {self.pedido} \nResponsavel: {self.responsavel}'
        
    def pagar_pedido(self, financeiro):
        soma = 0
        for i in self.pedido:
            soma += i[3]
        financeiro.receita += soma
        print(f"Pedido: {self.pedido} / Cliente: {self.cliente_nome}")
        print(f"Pedido pago!! A receita do dia agora é R${round(financeiro.receita, 2)}")


if __name__ == "__main__":
    # Criando uma instância de Empregados
    empregados = Empregados()

    # Adicionando funcionários
    garcom1 = Garçom("João", 1000)
    gerente1 = Gerente("Carlos", 2000)
    chef1 = Chef("Ana", 2500)
    garcom1.define_id()
    gerente1.define_id()
    chef1.define_id()
    garcom1.adiciona_funcionario(empregados.funcionarios)
    gerente1.adiciona_funcionario(empregados.funcionarios)
    chef1.adiciona_funcionario(empregados.funcionarios)

    # Testando se os funcionários foram adicionados corretamente
    print("--- Testando adicionar funcionários ---")
    empregados.mostra_lista()

    # Criando uma instância de Menu
    menu = Menu()

    # Adicionando itens ao menu
    menu.adicionar_item("Hamburguer", "Hamburguer de carne com queijo e alface", 1, 10.99)
    menu.adicionar_item("Pizza", "Pizza de pepperoni", 2, 12.99)
    menu.adicionar_item("Salada", "Salada fresca com vegetais diversos", 3, 6.99)

    # Classificando os itens do menu
    menu.classificar_itens()

    # Procurando um item no menu
    print("\n--- Testando procurar item no menu ---")
    menu.procura_item()

    # Criando uma instância de Pedidos
    pedidos = Pedidos("Cliente 1")

    # Fazendo um pedido
    pedido = input("Digite o que deseja: ").title()
    pedidos.adicionar_pedido(menu, pedido)
    pedidos.responsavel_pedido(empregados)
    print("\n--- Testando fazer um pedido ---")

    print(pedidos)

    # Criando uma instância de Financeiro
    financeiro = Financeiro()

    # Pagar o pedido
    print("\n--- Testando pagar um pedido ---")
    pedidos.pagar_pedido(financeiro)

    # Verificando a receita do dia
    print("\n--- Testando a receita do dia ---")
    print(financeiro)
