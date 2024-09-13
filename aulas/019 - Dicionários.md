# Dicionários e seus Métodos
Dicionários são estruturas de dados em Python.

Os elementos em dicionário são elementos do tipo chave/valor, onde é possível dar um nome para chave e atribuir qualquer tipo de dado no valor.

```python
meu_dicio = {
    'nome': 'Felipe',
    'idade': 25,
    'profissao': 'Dev'
}
```

A diferença entre listas e dicionários esta baseada em como o dado é acessado. Na lista é necessário informar o índice do item na lista, enquanto no dicionário é necessário informar a chave para ver o dado.

```python
print(meu_dicio['nome'])
```
O código acima irá buscar em todos os elementos do dicionário e listará somente os que possuem a chave `nome`.

Outra forma de capturar os valores de dentro de um dicionário é utilizando o método `get`, informando a chave que deseja capturar.

```python
print(meu_dicio.get('nome'))
```

## Adicionar itens ao dicionário
Para adicionar itens ao dicionário não é necessário nenhum método ou função, basta executar o dicionário informando entre colchetes uma chave que não existe, e atribuir um valor a essa chave.

```python
meu_dicio['ano_nascimento'] = 1997
print(meu_dicio)
```
A ação acima irá adicionar a chave `ano_nascimento` ao dicionário `meu_dicio` e em seguida irá imprimir no console o resultado, que deve ser o seguinte:

```txt
{'nome': 'Felipe', 'idade': 25, 'profissao': 'Dev', 'ano_nascimento': 1997}
```
Esse método serve para qualquer tipo de dado. É possível atribuir strings, inteiros, listas e até dicionários.

E mais, é possível adicionar itens em dicionários dentro do dicionário, basta ir fazendo a navegação com chaves dos dicionários até chegar no distino, como por exemplo utilizando um dicionário mais completo:

```python
pessoa = {
    'nome': 'Felipe',
    'idade': 25,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programacao', 'Notebooks'],
    'pet': {
        'nome': 'Loki',
        'idade': 1,
        'peso': '2kg'
    }
}

pessoa['pet']['ano_nascimento'] = 2022
print(pessoa)
```
A saída do código deve informar a nova chave dentro de `pet`:

```txt
{'nome': 'Felipe', 'idade': 25, 'profissao': 'Dev', 'interesses': ['Python', 'Programacao', 'Notebooks'], 'pet': {'nome': 'Loki', 'idade': 1, 'peso': '2kg', 'ano_nascimento': 2022}}
```

## Remover itens do dicionário
É possível remover elementos de dentro do dicionário utilizando o método `pop` juntamente com a chave do elemento.

```python
meu_dicio.pop('nome')
print(meu_dicio)
```
No código acima estamos usando o método `pop` para remover o item que possui a chave `nome` de dentro do dicionário.

A saída do código deve ser a seguinte:

```txt
{'idade': 25, 'profissao': 'Dev'}
```

## Listar chaves do dicionário
Para listar somente as chaves do dicionário, sem listas os valores, é possível utilizar o método `keys` sem informar nenhum parametro.

```python
print(meu_dicio.keys())
```
A saída do código deve ser a seguinte:

```txt
dict_keys(['idade', 'profissao'])
```

## Listar valores do dicionário
Pode-se listar também somente os valores do dicionário, sem as suas chaves, utilizando o método `values`.

```python
print(meu_dicio.values())
```
A saída do código deve ser a seguinte:

```txt
dict_values([25, 'Dev'])
```

## Apagar os dados do dicionário
Para apagar todas as informações do dicionário, é possível utilizar o método `clear` sem nenhum parametro.

```python
print(meu_dicio.clear())
```
O código acima não resultará nenhuma saída no console mas removerá todos os itens do dicionário.

## Lista dentro de dicionários
Em um dicionário o valor de um item pode ser praticamente qualquer coisa, inclusive uma lista, ou um array.

```python
pessoa = {
    'nome': 'Felipe',
    'idade': 25,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programacao', 'Notebooks']
}
```

E também é possível ter um dicionário dentro de um dicionário, como sendo uma chave e o valor sendo um dicionário.

```python
pessoa = {
    # Os mesmos dados anteriores
    'pet': {
        'nome': 'Loki',
        'idade': 1,
        'peso': '2kg'
    }
}
```
No caso acima estamos criando um dicionário para a chave `pet` e estruturando os dados dentro de um dicionário.

## Buscar item de uma lista no dicionário
É possível buscar um item dentro de uma lista que está em uma chave do dicionário utilizando o método `get` informando a chave da lista. E como o retorno é uma lista, basta definir qual índice do item da lista deseja listar.

```python
print(pessoa.get('interesses')) #Irá retornar a lista da chave 'interesses'
print(pessoas.get('interesses')[0]) #Irá retornar o item de índice 0 da lista 'interesses'
```

## Buscar item de um dicionário dentro do dicionário
Também podemos buscar um item de um dicionário que é o valor de uma chave dentro do nosso dicionário principal. Para isso basta "acessar" o item dicionário com o método `get` e buscar o item do dicionário utilizando o mesmo método novamente.

```python
print(pessoa.get('pet')) #Irá retornar um dicionário com os dados do 'pet'
print(pessoa.get('pet').get('nome')) #Irá retornar o valor da chave 'nome' dentro do dicionário que tem a chave 'pet'

