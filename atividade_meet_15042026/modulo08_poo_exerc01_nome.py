
class Carro:
    # primeiro se coloca os atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # segundo fazer os metodos 
    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"
    

meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.exibir_info())