# Polimorfismo de Interface em Python

O **polimorfismo de interface** ocorre quando diferentes classes implementam os mesmos métodos, permitindo que sejam usadas de forma intercambiável, mesmo sem compartilhar uma classe base comum. O foco está em garantir que os métodos tenham a mesma assinatura (nome e parâmetros), permitindo que objetos dessas classes possam ser manipulados de forma polimórfica.

Em Python, isso é facilitado pelo conceito de **duck typing**, onde o tipo ou classe de um objeto é menos importante do que a implementação dos métodos necessários.

```python
class Car:
    def move(self):
        return "The car is driving"

class Airplane:
    def move(self):
        return "The airplane is flying"

# Ambas as classes têm o método `move`, mas não estão relacionadas por herança.
vehicles = [Car(), Airplane()]

for vehicle in vehicles:
    print(vehicle.move())
```
Nesse exemplo, tanto `Car` quanto `Airplane` possuem o método `move`, permitindo que sejam usados de forma intercambiável, mesmo sem herança entre eles. Este é um exemplo clássico de polimorfismo de interface.