class Animal:
    def __init__(self):
        print(self)

    def mover(self, metros):
        print("O animal se moveu {} metros em relação ao ponto que estava inicialmente".format(metros))

class Mamifero(Animal):
    def __init__(self):
        pass

    def amamentando(self):
        print("O mamifero esta amamentando")

class Cachorro(Mamifero):
    def __init__(self):
        pass

    def latir(self):
        print("O cachorro esta latindo")


cachorro = Cachorro()
cachorro.mover(3)
cachorro.amamentando()
cachorro.latir()
        
        
