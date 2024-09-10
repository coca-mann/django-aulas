# Operadores lógicos no Python
Operadores lógicos são operadores que irão ajudar na execução de uma condição para obter um resultado booleano. Tudo no computador é binário, ou seja, 0 ou 1. Então toda condição pode ser *True* ou *False*.

## Tabela Verdade AND
Compara o valor de duas variáveis onde o mesmo busca a condição verdadeira entre as duas, e retorna o resultado utilizando o operador **AND**.

| A | B | A and B |
| :---: | :---: | :---: |
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

## Tabela Verdade OR
Compara o valor de duas variáveis onde somente uma delas precisa ser verdadeira, e retorna o resultado utilizando o operador **OR**.

| A | B | A or B |
| :---: | :---: | :---: |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

## Condição composta
É possível montar condições compostas onde uma ou mais condições é colocada entre parenteses e em seguida é comparado com outro dado, criando uma condição composto. Exemplo:

```python
idade = 25
nome = 'Juliano'
peso = 90

if (nome == 'Juliano' or idade == 24) and peso == 90:
    print('Dados corretos')
else:
    print('Dados incorretos')
```
