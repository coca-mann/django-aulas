# Funções em Python
Uma função nada mais é do que um conjunto ou bloco de comandos que executam alguma ação ou tarefa. Geralmente uma função recebe algum parâmetro, executa uma ação e devolve algum resultado que pode ser chamado de **retorno**.

Imagine uma função como um liquidificador, onde você coloca laranjas nele, bate as laranjas e então você tem um suco de laranja pronto. As laranjas podem ser os parâmetros ou dados de **entrada**, logo em seguida você executa a **ação** (ligar o liquidificador), e assim você consegue o **resultado** (suco de laranjas).

## Funções nativas
O Python possui funções que são nativas da linguagem. Essas funções são instaladas junto com o interpretador.

Exemplos de funções são: print, len, dict, input, entre outras.

## Definir uma função em Python
Para definir, ou criar, uma função em Python, é utilizado o termo `def` (definition, definição) e o nome da função, e dentro dessa função deve ser colocado os códigos a serem usados.

```python
def minha_funcao():
    print('Minha função')
```
As funções em Python não precisam obrigatoriamente ter parametros de entrada de dados. Elas podem executar o código interno e retornar ou não algum valor.

## Retorno de funções
Após a execução de uma função, algo pode ser retornado por ela para a execução do código principal através de uma **declaração de retorno de função**, como no exemplo abaixo será a soma de duas variáveis:

```python
def somar(a, b):
    resultado = a + b
    return resultado

somar(1, 2)
```
A saída do código será 3.

## Retorno de função com parametros
Em um caso mais complexo, é possível enviar dados para uma função, executar uma lógica com esses dados, e retornar dados dessa função com alguns parametros. Veja o exemplo abaixo:

```python
def enviar_email(nome, email):
    nome_dest = nome
    email_dest = email
    # Lógica da função
    return f'Email enviado para {nome_dest} na conta de email {email_dest}'

pessoas = [
    {
        'nome': 'Felipe',
        'email': 'felipe@gmail.com'
    },
    {
        'nome': 'Gabriele',
        'email': 'gabriele@gmail.com'
    },
    {
        'nome': 'Pedro',
        'email': 'pedro@gmail.com'
    }
]

for pessoa in pessoas:
    email_enviado = enviar_email(pessoa['nome'], pessoa['email'])
    print(email_enviado)
```
No caso acima é criado uma lista de objetos dentro da variavel `pessoas` onde contém as chaves `nome` e `email` e os valores dessas chaves são passadas para a função executar a sua lógica. A função então retorna dados que são impressos na varíavel `email_enviado`.

O resultado é a saída no console:

```plain text
Email enviado para Felipe na conta de email felipe@gmail.com
Email enviado para Gabriele na conta de email gabriele@gmail.com
Email enviado para Pedro na conta de email pedro@gmail.com
```
