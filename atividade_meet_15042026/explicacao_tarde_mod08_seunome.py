'''
Programação Orientada a Objetos (POO)

Encapsulamento:

Herança:

Polimorfismo:
--------------------------------------------------------------------------------------------------------
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def buzinar(self):
        print(f'O {self.marca} da cor {self.cor} fez Bip Bip! ')

meu_carro = Carro('Toyota', 'cinza')

carro_do_cliente = Carro('Honda', 'preto')

meu_carro.buzinar()

carro_do_cliente.buzinar()

EXERCICIO PRÁTICO: SIMULE UM CARREGAMENTO DE UM SMARTFONE, QUANDO ESTIVER A 5%. MENSAGEM, QUANDO ESTIVER
85% AVISE QUE ESTÁ CARREGADO.

'''

class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100

    def ligar(self):
        self.ligado = True
        print(f'{self.modelo} está ligado.')

    def carregar(self):
        self.bateria = 100
        print(f'{self.modelo} está carregado.')


meu_celular = Celular('Apple', 'iPhone 16')
meu_celular.ligar()
meu_celular.bateria = 5
print(f'{meu_celular.modelo} está com {meu_celular.bateria}% de bateria.')