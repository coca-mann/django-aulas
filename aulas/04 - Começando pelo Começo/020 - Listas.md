# Listas em Python
Uma lista é um array de dados atribuída à uma varíavel, que pode conter qualquer tipo de dado dentro do mesmo array.

A lista é definida entre colchetes e os dados são separados por vírgulas.

```python
lista = [10, 'Nove', True, {'veiculo': 'Carro','Marca': 'Fiat', 'Ano': 2007}, [19, 'Treze'], 25.05]
```
Na lista acima temos todos os tipos de dados possíveis em Pyhton, e cada item da lista pode ser acessado e impresso no console. Inclusive, pode ser impresso cada tipo de item utilizando o código abaixo:

```python
for i, item in enumerate(lista):
    if i == len(lista):
        break
    else:
        print(type(lista[i]))
```
A saída do código deve ser a seguinte:

```plain text
<class 'int'>
<class 'str'>
<class 'bool'>
<class 'dict'>
<class 'list'>
<class 'float'>
```
Cada item da lista pode ser acessado e seu tipo é definido conforme foi confirmado com a execução do código anterior.

## Adicionar itens à lista
Para adicionar um dado à uma lista, podemos utilizar o método `append` e informar o valor desejado. Esse método sempre adicionará o item ao final da lista.

```python
lista.append('Cartas')
print(lista[len(lista)-1])
```
A execução do código deve resultar na adição do dado à lista informada, e o print exibirá no console apenas a última posição da lista, que foi o nosso valor inserido.

Ao selecionarmos o tamanho da lista e subtrairmos 1, teremos o último índice existente da lista, visto que o índice 0 é o primeiro item da lista.

## Inserir itens na lista
Diferente do método `append` podemos utilizar o método `insert` para inserir um item na lista em qualquer posição. 

Esse método não substitui nenhum dado, ele apenas adiciona o dado na posição informada e empurra os itens a sua frente para as próximas posições.

Nesse caso o método pede dois parametros:
- **Posição**: o valor da posição, do índice, em que deseja adicionar o dado
- **Valor**: o valor, o dado, a ser adicionado naquela posição

```python
lista.insert(1, 'Queijo')
print(lista)
```
Ao executar o código acima, o dado 'Queijo' será inserido na posição 1 da lista, e em seguida é impresso a lista completa que deve ser assim:

```plain text
[10, 'Queijo', 'Nove', True, {'veiculo': 'Carro', 'Marca': 'Fiat', 'Ano': 2007}, [19, 'Treze'], 25.05, 'Cartas']
```

## Remover itens da lista
Seguem algumas formas de remover itens de uma lista.

1. Podemos utilizar um método muito famoso para remover itens da lista chamado `pop`.

Ao ser executado sem nenhum parametro, esse método removerá sempre o último elemento da lista.

```python
lista.pop()
print(lista)
```
A saída do console deve ser a seguinte:

```plain text
[10, 'Queijo', 'Nove', True, {'veiculo': 'Carro', 'Marca': 'Fiat', 'Ano': 2007}, [19, 'Treze'], 25.05]
```

2. Outra forma também é utilizar a função `del`, que é nativa do Python, e nessa função é possível informar o índice do item que será removido da lista.

```python
del lista[2]
print(lista)
```
O item com índice 2 será removido da lista e a saída do console deve ser a seguinte:

```plain text
[10, 'Queijo', {'veiculo': 'Carro', 'Marca': 'Fiat', 'Ano': 2007}, [19, 'Treze'], 25.05]
```

3. Além dessas duas formas, há também um método chamado `remove` que remove um item da lista informando o valor do item.

```python
lista.remove(25.05)
print(lista)
```
Esse método fará uma busca pelo valor informado na lista, e somente removerá se o valor for encontrado. Após o valor ser encontrado e removida, a saída de console deve ser a seguinte:

```plain text
[10, 'Queijo', 'Nove', True, {'veiculo': 'Carro', 'Marca': 'Fiat', 'Ano': 2007}, [19, 'Treze']]
```

## Contagem de itens da lista
Podemos utilizar o método `count` para contar quantas vezes um valor aparece na lista.

```python
print(lista.count(True))
```
O código acima fará a impressão em console de quantas vezes o termo booleano *True* aparece na lista. No caso da nossa lista aparece somente uma vez, então a saída de console será 1.

## Inverter a ordem da lista
O método `reverse` faz a inversão da ordem da lista, onde os itens finais irão para as primeiras posições e vice-versa.

```python
lista.reverse()
print(lista)
```
A saída de console deve ser a seguinte:

```plain text
[25.05, [19, 'Treze'], {'veiculo': 'Carro', 'Marca': 'Fiat', 'Ano': 2007}, True, 'Nove', 'Queijo', 10]
```

## Ordenar os itens da lista
Para organizar os itens da lista de forma alfanumérica, basta utilizar o método `sort`.

Porém esse método funciona somente em listas que contém somente um tipo de dado, como por exemplo somente strings ou inteiros.

```python
inteiros = [9, 12, 3, 48, 22, 18, 24]
inteiros.sort()
print(inteiros)
strings = ['Nove', 'Doze', 'Queijo', 'Bicicleta']
strings.sort()
print(strings)
```
A saída do console deve ser a seguinte:

```plain text
[3, 9, 12, 18, 22, 24, 48]
['Bicicleta', 'Doze', 'Nove', 'Queijo']
```
