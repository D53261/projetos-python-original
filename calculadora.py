class Calculadora:

    def soma(self, a, b):
        soma = a + b
        print(soma)

    def subtracao(self, a, b):
        subtracao = a - b
        print(subtracao)

    def multiplicacao(self, a, b):
        multiplicacao = a * b
        print(multiplicacao)

    def divisao(self, a, b):
        divisao = a / b
        print(divisao)

    def potencia(self, base, expoente):
        potencia = base ** expoente
        print(potencia)

calculadora = Calculadora()
calculadora.soma(30, 30)
calculadora.subtracao(60, 30)
calculadora.multiplicacao(30, 30)
calculadora.divisao(30, 3)
calculadora.potencia(2, 5)

