# Programação Orientada a Objetos
A programação orientada a objetos é uma forma de você representar coisas da vida real em código.

Um objeto dentro do Python é uma classe que utiliza o método `class` para ser definida.

Dentro de cada objeto pode ter propriedades e funções. Propriedades são caracteristicas do objeto, ou então variáveis. E funções são coisas que aquele objeto faz, conhecidas também por *functions* ou `def`.

Por exemplo, imagine um celular antigo, o famoso Nokia Tijolão. Ele é um objeto da vida real. Aqui estão algumas propriedades dele:
- Marca: Nokia
- Modelo: Tijolão
- Cor: Azul
- Tem câmera? Não
- Bateria: Infinita

E algumas funções que ele possui e executa:
- Fazer ligações
- Jogar o jogo da cobrinha
- Despertador

Esse objeto pode ser representado em código muito facilmente. Veja abaixo:

```python
class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')
```

## Instanciando classes
Para utilizar o objeto, a classe, dentro do seu código, é necessário instanciala, referencia-la, em uma variável para tornar ela uma instancia do objeto.

```python
celular = Celular()
```
Ao instanciar classes, a variável que receber a classe poderá utilizar todos os métodos e dados de dentro da classe.