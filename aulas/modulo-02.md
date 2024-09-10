# Aula 007 - O que é PIP?
O PIP é um gerenciador de pacotes para projetos Pyhton. É com ele que instalamos, removemos e atualizamos pacotes em nossos projetos. É similar aos conhecidos `npm` e `composer`, por exemplo.

O PIP possui uma página onde nós conseguimos buscar os pacotes disponíveis para utilização. Nela podemos pesquisar por um pacote específico ou até uma palavra-chave:

[pypi.org](https://pypi.org/)

## Instalar pacotes
Para instalar os pacotes da comunidade PyPI, basta utilizar a função `install` no terminal. Lembre-se de estar com o terminal aberto dentro da pasta do projeto.

```bash
pip install [nome_pacote]
```

```bash
pip install selenium
```

O comando acima instalará a biblioteca Selenium, muito utilizada para automações na Web.

## Desinstalar pacotes
Para desinstalar pacotes instalados no projeto, basta utilizar o comando `uninstall` conforme demonstrado abaixo:

```bash
pip uninstall [nome_pacote]
```

```bash
pip uninstall selenium
```
Nesse momento o pip fará a remoção do pacote e suas dependecias do seu projeto.

## Salvado dependencias
Em um projeto colaborativo, ou até mesmo pessoal, é muito interessante salvar as dependencias que seu projeto utiliza para caso outra pessoa trabalhe nele, ela também pode ajustar seu ambiente de acordo com as necessidades do seu projeto.

Para verificar as dependencias instaladas no projeto, utilize a função `freeze` do pip:

```bash
pip freeze
```

Essa função listará todas os pacotes e dependencias instalados no projeto e suas versões.

Para salvar as dependencias, basta salvar a saída do comando acima em um arquivo de texto. O ideal, e o mais comum visto na comunidade, é salvar o arquivo de texto com nome **requirements.txt**. Veja como:

```bash
pip freeze > requirements.txt
```

Dessa forma todos os pacotes serão exportados para um arquivo e ficarão disponíveis no projeto.

Para instalar os pacotes através do arquivo exportado, execute o seguinte comando:

```bash
pip install -r caminho/do/arquivo.txt
```


# Ambientes Virtuais (venv)
