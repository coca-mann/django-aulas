import os
import api

os.system('cls')

usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

credenciais = [usuario, senha]
print(credenciais)

login = api.login(usuario, senha)

print(login)
