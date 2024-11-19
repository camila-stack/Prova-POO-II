#Não entendi muito bem oque era para fazer

class Animal:
    def falar(self):
        return 'Esse animal faz um som'

class Cachorro(Animal):
    def falar(self):
        return 'O cachorro late'


class Gato(Animal):
    def falar(self):
        return 'O gato mia'
    

fred = Cachorro()
snow = Gato()

print(fred.falar())
print(snow.falar())