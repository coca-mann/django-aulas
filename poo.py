import os

os.system('cls')

class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def calcular(self, v1, v2):
        return v1 + v2

celular = Celular()

print(celular.marca)

celular.despertador()
celular.jogar_cobrinha()

resultado = celular.calcular(2, 4)
print(resultado)