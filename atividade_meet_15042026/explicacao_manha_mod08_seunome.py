'''
Programação Orientada ao Objeto (POO)

Encapsulamento:

Herança:

Polimorfismo:


'''

#classe é um molde para criar objetos. Ela define as características (atributos) e comportamentos (métodos) que os objetos criados a partir dela terão.
class Carro:

    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def buzinar(self):
        print(f'O {self.marca} da cor {self.cor} fez: Bip Bip!')


# Objeto é uma instância de uma classe. Ele possui as características (atributos) e comportamentos (métodos) definidos na classe.
meu_carro = Carro('Toyota', 'cinza')

carro_do_cliente = Carro('Honda', 'preto')


meu_carro.buzinar()
carro_do_cliente.buzinar()