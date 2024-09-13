# Variáveis de Ambiente
Variáveis de ambiente nada mais são do que varíaveis que você **salva/configura** no sistema operacional, ou seja, no ambiente em que sua aplicação irá rodar.

Esse tipo de dado é muito utilizado para credenciais de acessos e dados sensíveis, que não ficarão disponíveis no projeto, caso ele seja compartilhado, e o seu código pode utilizá-lo de qualquer forma.

Veja como criar variáveis de ambiente:

Para sistemas operacionais Linux:
```bash
export MINHA_VAR=valor 
```

Para sistemas operacionais Windows CMD:
```bat
set MINHA_VAR valor
```

Para sistemas operacionais Windows PowerShell:
```pwsh
$env:MINHA_VAR = 'valor'
```

> Cuidado ao declarar variáveis de ambiente utilizando o Terminal do VS Code. Muito provavelmente o Terminal esta rodando com PowerShell, e deve ser utilizado o método correto para declarar variáveis de ambiente nesse tipo de Terminal.

## Lendo variáveis de ambiente no Python
Para ler as variáveis de ambiente no seu código Python e atribuí-la a uma variável de executação, é necessário chamar a biblioteca nativa `os` e utilizar o método `environ.get()` passando o nome da variável como parametro. Veja o exemplo:

- Primeiro criamos nossas variáveis de ambiente e atribuímos um valor a elas.
```pwsh
$env:USUARIO_API = 'pycodebr'
$env:SENHA_API = '1234'
```

- Em seguida buscamos as variáveis dentro do código Python
```python
import os

usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

credenciais = [usuario, senha]
print(credenciais)
```
A saída do código deve exibir uma lista com os valores das variáveis de ambiente configuradas no sistema operacional.

```txt
['pycodebr', '1234']
```
