# Herança em Python
Herança é uma função do paradigma de programação orientada a objeto, é uma forma de escrever o código, onde você consegue herdar propriedades e funções de outra classe em uma nova classe que esta desenvolvendo.

Isso evita a duplicação de funções e dados no código, centralizando e simplificando o código.

Por exemplo vamos criar uma classe chamada Carro:

```python
class Carro:
    numero_rodas = 4
    qtd_passageiros = 5

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')
```

Para criarmos uma nova classe que herdará todas as funções e propriedades de outra classe, basta criarmos essa nova classe instanciando em seu nome a classe que desejamos herar.

```python
class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992
```
Dessa forma quando formos utilizar a classe `Uno` poderemos utilizar as funções e propriedades da classe `Carro` também, pois nesse caso herdando tudo dela.
