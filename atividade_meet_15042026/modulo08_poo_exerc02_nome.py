class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        # O super() inicializa a marca e o modelo na classe pai
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    # Estendemos o método exibir_info para incluir a bateria
    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia: {self.autonomia_bateria}km"

# Exemplo de uso:
meu_ev = CarroEletrico("Tesla", "Model Y", 450)
print(meu_ev.exibir_info())