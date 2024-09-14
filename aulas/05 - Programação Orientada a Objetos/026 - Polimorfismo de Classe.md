# Polimorfismo de Classe
A ideia do Polimorfismo é permitir que classes diferentes que herdam funções e propriedades de uma mesma classe, possam ter propriedades, métodos e funções com o mesmo nome, mas que executam coisas diferentes.

O conceito de polimorfismo indica que é possível reescrever uma função já existente na classe pai, em uma classe filha. Por exemplo, veja a classe pai e suas funções:

```python
class Animal:

    def emitir_som(self):
        print('Qualquer som...')
```
Um animal emite um som, mas os animais não emitem o mesmo som. Agora vamos criar classes de dois tipos de animais diferentes que vão herdar da classe acima:

```python
class Cachorro(Animal):

    def emitir_som(self):
        print('Au Au!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau!')
```
Podemos ver que, utilizando o polimorfismo, nós reescrevemos a `função emitir_som()` para que cada animal pudesse emitir seu som específico. Porém o restante dos métodos e funções continuam sendo herdados da classe pai.

