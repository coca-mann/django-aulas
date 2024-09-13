import os

os.system('cls')

a = False
b = False

if a or b:
    print('Atendeu')
else:
    print('Não atendeu')

idade = 25
nome = 'Juliano'
peso = 90

if (nome == 'Juliano' or idade == 24) and peso == 90:
    print('Dados corretos')
else:
    print('Dados incorretos')


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


def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

for cliente in clientes:
    envia_email(cliente)

for i, cliente in enumerate(clientes):
    print(i, cliente)

numero = 0

while numero < 5:
    print(numero)
    numero += 1

for i in range(0, 100, 10):
    print(i)

for i, cliente in enumerate(clientes):
    if i == 2:
        continue
    envia_email(cliente)

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

lista = [10, 'Nove', True, 'Doze', 25]

for i, item in enumerate(lista):
    if i == len(lista):
        break
    else:
        print(type(lista[i]))

lista.append('Cartas')
print(lista[len(lista)-1])

lista.insert(1, 'Queijo')
print(lista)

lista.pop()
print(lista)

lista.reverse()
print(lista)

print(lista.count(True))

inteiros = [9, 12, 3, 48, 22, 18, 24]
inteiros.sort()
print(inteiros)
strings = ['Nove', 'Doze', 'Queijo', 'Bicicleta']
strings.sort()
print(strings)

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)

nomes = ['Juliano', 'Sara', 'Felipe']
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)

nomes = ['Juliano', 'Sara', 'Felipe', 'Antonio', 'Fernando']
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'F']
print(nomes_maiusculos)