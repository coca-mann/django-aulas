class Animal:
    mamifero = True
    def emitir_som(self):
        print('Qualquer som...')

class Cachorro(Animal):

    def emitir_som(self):
        print('Au Au!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau!')

cachorro = Cachorro()
cachorro.emitir_som()
gato = Gato()
gato.emitir_som()
print(gato.mamifero)

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polimorfismo de herança: diferentes classes filhas têm o mesmo método `sound`, mas comportamentos diferentes.
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

class Car:
    def move(self):
        return "The car is driving"

class Airplane:
    def move(self):
        return "The airplane is flying"

# Polimorfismo de interface: ambas as classes possuem um método `move`, mas não têm relação de herança.
vehicles = [Car(), Airplane()]

for vehicle in vehicles:
    print(vehicle.move())