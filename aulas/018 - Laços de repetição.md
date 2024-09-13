# Laços de repetição (FOR/WHILE)
Laços de repetição são execuções de um código dentro do laço FOR ou WHILE que tem sua condição Verdadeira ou Falsa, ou enquanto houver itens em uma lista.

## FOR
O laço de repetição FOR é melhor utilizado quando sabemos que as repetições do laço terão um fim, que são finitas. A condiçãod e saída do laço é a quantidade de vezes que o mesmo será executado.

Por exemplo:

```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

for cliente in clientes:
    envia_email(cliente)
```

No caso do laço de repetição FOR acima, o código dentro do laço será executando enquanto houver itens na lista.

O FOR atribuirá cada item da lista `clientes` para a varíavel declarada `cliente` do laço de repetição, e executará o código dentro do laço toda vez que um item for descoberto na lista. Nesse caso será executada a função `envia_email` definida, passando cada item da cliente no parametro necessário.

Quando acabarem todos os itens da lista `clientes`, o laço será encerrado.

A saída do código acima deve ser:

```txt
Email enviado para o cliente Ana!
Email enviado para o cliente Jonas!
Email enviado para o cliente Felipe!
Email enviado para o cliente Cláudio!
Email enviado para o cliente Renato!
```

## Range no FOR
É possível definir a quantidade de vezes que um laço de repetição FOR é executado, utilizando a função `range` conforme abaixo:

```python
for i in range(10):
    print(i)
```
O laço acima será executa 10 vezes começando pelo zero. A saída do código será uma lista de 0 a 9.

Também é possível definir um intervalo de execução com uma quantidade de pulos a serem dados dentro do intervalo, por exemplo:

```python
for i in range(0, 100, 10):
    print(i)
```
Na definição do `range` do laço acima, o mesmo executará um loop começando pelo 0 e indo no máximo até 100 vezes, porém pulando 10 números de cada vez.

A saída do console deve ser a seguinte:

```txt
0
10
20
30
40
50
60
70
80
90
```


## WHILE
O laço de repetição WHILE é utilizado quando não sabemos a quantidade de vezes que o laço irá executar. A condição de saída do laço é do tipo booleana, ou seja, o código dentro do laço será executado enquanto a condição do laço for True (Verdadeira):

```python
numero = 0

while numero < 5:
    print(numero)
    numero += 1
```
No caso acima, o código dentro do laço começa a ser executado com o valor da varíavel `numero` sendo 0, conforme declarada. O código dentro do laço imprime no console o valor da varíavel e em seguida soma 1 número no valor da varíavel. Em seguida o código é executado novamente, até que na última a condição do while será False, pois 5 não é menor que 5, e o laço de repetição é encerrado.

A saída do console deve ser a seguinte:
```txt
0
1
2
3
4
```

## Numerar itens na saída do código
É possível utilizar uma função no laço de repetição FOR, que fará a numeração dos itens na saída do código, afim de identificar com maior facilidade qual o índice de tal item.

```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

for i, cliente in enumerate(clientes):
    print(i, cliente)
```
No caso acima estamos buscando o índice de cada item da lista e colocando na varíavel `i` do laço de repetição, e também buscando o item em si e colocando na varíavel `clientes`. Dessa forma, a saída de console deve ser a seguinte:

```txt
0 Ana
1 Jonas
2 Felipe
3 Cláudio
4 Renato
```

## Break no laço
A função `break` serve para encerrar o laço de repetição não importa a condição dele. O loop será forçado a ser encerrado dando fim ao laço de repetição.

Ele pode ser utilizado com uma condicional dentro do laço, conforme exemplo abaixo:

```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

for i, cliente in enumerate(clientes):
    if i == 2:
        break
    envia_email(cliente)
```
No laço de repetição acima esta sendo utilizado o índice de cada item da lista para controlar a execução do `break`. Caso a condição do `if` seja verdadeira, ou seja, o índice do item da lista é igual a 2, o código do `if` será executado dando então um fim no loop do laço de repetição.

Enquanto a condição do `if` não é satisfeita, o loop será executado utilizando a função `envia_email()`.

A saída no console deve ser a seguinte:

```txt
Email enviado para o cliente Ana!
Email enviado para o cliente Jonas!
```

## Continue
A função `continue` dentro do laço de repetição serve para pular o loop que esta rodando naquele momento, caso a condição a qual ele esta associado seja satisfeita. Por exemplo:

```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

for i, cliente in enumerate(clientes):
    if i == 2:
        continue
    envia_email(cliente)
```
O laço será executado até `i` for igual a 2. Quando isso acontecer aquele loop será interrompido e um novo loop será iniciado, pulando então aquela execução daquele item da lista e indo para o próximo.

A saída do código deve ser a seguinte:

```txt
Email enviado para o cliente Ana!
Email enviado para o cliente Jonas!
Email enviado para o cliente Cláudio!
Email enviado para o cliente Renato!
```
Pode ser observado que o item 2 da lista não foi executado no loop.

> **Cuidado!** No laço de repetição **WHILE**, a utilização da função `continue` pode gerar uma execução infinita do código.
