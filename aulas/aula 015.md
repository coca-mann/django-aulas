# Strings e seus Métodos
Strings são um tipo primitivo de dados e significam um *conjunto de caracteres*, ou então *texto*. Esse tipo de dado possui diversos métodos de utilização.

Para testarmos as strings, devemos primeiro declarar uma varíavel com um tipo de dado *string* dentro;

```python
texto = 'AULA PYCODEBR'
```

Strings lembram bastante uma cadeia de caracteres. E cada caracter possui um **índice**, que é uma posição definida nessa lista de caracteres, inclusive espaços.

## Métodos de manipulação de strings


| Método | Descrição | Saída |
| :---: | :--- | :---: |
| **texto[0]** | Indicar um valor de índice dentro de colchetes para buscar o caracter que esta naquele índice | 'A' |
| **texto[5:11]** | Indicar um intervalo entre índices para buscar os caractéres dentro do intervalo | 'PYCODE' |
| **texto[5:]** | Indicar a posição inicial de um intervalo de índices mas não indicar uma posição final fará a impressão de todos os caracteres após a posição inicial | 'PYCODEBR' |
| **texto[:4]** | Indicar apenas a posição final de um intervalo de indíces trará todos os caracteres antes da posição informada | 'AULA' |
| **len(texto)** | Retorna o tamanho da string em um número inteiro | 13 |
| **texto.count('A')** | Função utilizada para contar quantas vezes um caracter se encontra na string. Serve também para procurar palavras. | 2 |
| **texto.count('A', 5, 11)** | Contar quantas vezes o caracter se encontra dentro de um intervalo de indices | 0 |
| **texto.find('PYCODEBR')** | Realiza uma busca dentro da string com os caractéres informados e retorna somente posição inicial do índice encontrado | 5 |
| **texto.upper()** | Retorna todos os caracteres da string em letras maiúsculas | 'AULA PYCODEBR' |
| **texto.lower()** | Retorna todos os caracteres da string em letras minúsculas | 'aula pycodebr' |
| **texto.capitalize()** | Retorna todos os caracteres da string colocando somente a primeira letra maíuscula | 'Aula pycodebr' |
| **texto.title()** | Retorna todas as palavras da string e coloca letra maiúscula em todas as primeiras letras das palabras | 'Aula Pycodebr' |
| **texto.split()** | Retorna todas as palavras da string dívidas por espaço, em uma lista de palavras | ['AULA', 'PYCODEBR'] |
| **lista_de_palavras = texto.split() ⤵️''.join(lista_de_palavras)** | O comando join irá unir as palavras da lista e utilizará o(s) separador(es) informado(s) antes da função para separar as palavras | 'AULAPYCODEBR' |
| **texto = '   AULA PYCODEBR   ' ⤵️ texto.strip()** | Remove espaços em branco no começo e no final das strings | 'AULA PYCODEBR' |
| **texto = '   AULA PYCODEBR   ' ⤵️ texto.rstrip()** | Remove os espaços vazios a direita (right) da string | '   AULA PYCODEBR' |
| **texto = '   AULA PYCODEBR   ' ⤵️ texto.lstrip()** | Remove os espaços vazios a esquerda (left) da string | 'AULA PYCODEBR   ' |
