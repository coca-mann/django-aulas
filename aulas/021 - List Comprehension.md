# Compreensão de listas
Compreensão de listas, ou *list comprehension*, é um recurso do Python em que você consegue aplicar uma **expressão** ou **função** para cada um dos itens de uma lista, retornando assim uma nova lista com os itens alterados conforme a expressão/função que foi executada neles.

```python
list_comprehension = [expr for item in lista]
```
Em outras palavras: aplique a expressão `expr` em cada `item` da `lista`.

Veja um exemplo de *list comprehension*:

```python
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)
```
O resultado do código acima deve ser:

```plain text
[2, 4, 6, 8, 10]
```

Também é possível aplicar o *list comprehension* em listas com strings. Segue um exemplo:

```python
nomes = ['Juliano', 'Sara', 'Felipe']
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)
```
No código acima estamos pegando todos as strings da lista `nomes` e transformando em strings maiusculas utilizando o método `upper()` para cada string da lista.

O resultado deve ser o seguinte:
```txt
['JULIANO', 'SARA', 'FELIPE']
```


## Função em compreensão de listas
Podemos utilizar funções definidas anteriormente nas expressões utilizadas nas compreensões de listas. Veja um exemplo:

```python
def dobro(numero):
    return numero * 2

numeros_dobrados [dobro(numero) for numero in numeros]
print(numeros_dobrados)
```
O resultado do código acima será exatamente igual ao resultado anterior pois essencialmente os dois códigos estão fazendo a mesma coisa, a única diferença é que este está utilizando a função `dobro()` como expressão.

## Compreensão de listas com condicionais
Digamos que da nossa lista de nomes, queremos retornar em caixa alta somente os nomes que começam com a letra F. É possível fazer colocando uma condicional na expressão do *list comprehension* da seguinte forma:

```python
list_comprehension_cond = [expr for item in lista cond]
```
Em outras palavras: aplique a expressão `expr` em cada `item` da `lista` que atende a condição `cond`.

Segue abaixo um exemplo prático da sintaxe acima:

```python
nomes = ['Juliano', 'Sara', 'Felipe', 'Antonio', 'Fernando']
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'F']
print(nomes_maiusculos)
```
No código acima adicionamos uma condição utilizando o `if` e dizendo que SE o índice 0 de cada `nome` for "F", então retorne esses nomes e coloque-os em caixa alta.

A saída do código deve ser a seguinte:

```txt
['FELIPE', 'FERNANDO']
```

