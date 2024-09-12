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

## Manipulando itens no dicionário
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