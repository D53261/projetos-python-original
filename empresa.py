class Funcionario:
    def __init__(self, nome, idade, salario_base):
        self._nome = nome.title()
        self._idade = idade
        self._salario_base = salario_base

    def calcular_salario(self):
        return self._salario_base

    def __str__(self):
        return f'{self._nome} - {self._idade} anos - {self._salario_base}R$ de salario base'

class FuncionarioRegular(Funcionario):
    def __init__(self, nome, idade, salario_base):
        super().__init__(nome, idade, salario_base)

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade, salario_base)
        self._bonus = bonus
        self._salario_atual = 0

    def calcular_salario(self):
        self._salario_atual = (super().calcular_salario() + (self._bonus))

    def __str__(self):
        return f'{self._nome} - {self._idade} anos - {self._salario_base}R$ de salario base - {self._salario_atual}R$ de salario atual'

class Diretor(Funcionario):
    def __init__(self, nome, idade, salario_base, departamento):
        super().__init__(nome, idade, salario_base)
        self._departamento = departamento
        self._salario_atual = 0

    def calcular_salario(self):
        self._salario_atual = (super().calcular_salario() + (self._salario_base * 0.1))

    def __str__(self):
        return f'{self._nome} - {self._idade} anos - {self._salario_base}R$ de salario base - {self._salario_atual}R$ de salario atual - Departamento {self._departamento}'


class Lista:
    def __init__(self, nome, funcionarios):
        self._nome = nome
        self._funcionarios = funcionarios

    def __getitem__(self, item):
        return self._funcionarios[item]

    def __len__(self):
        return len(self._funcionarios)



funcionario_base = FuncionarioRegular("denilson", 34, 300.0)

funcionario_pro = Gerente("Clorival", 45, 600.0, 300.0)
funcionario_pro.calcular_salario()
funcionario_adm = Diretor("Valdemar", 60, 1000.0, "Coxinhas")
funcionario_adm.calcular_salario()

empresa = [funcionario_base, funcionario_pro, funcionario_adm]
lista = Lista("Empresa Geral", empresa)
print("Numero de funcionários: {}".format(len(lista)))

for empregados in lista:
    print(empregados)







