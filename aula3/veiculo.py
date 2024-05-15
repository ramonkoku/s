class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        # Implementação genérica para acelerar
        print(f"{self.marca} está acelerando!")

class Carro(Veiculo):
    def acelerar(self):
        # Implementação específica para carros
        print(f"{self.marca} está acelerando rapidamente!")

class Motocicleta(Veiculo):
    def acelerar(self):
        # Implementação específica para motocicletas
        print(f"{self.marca} está acelerando na estrada!")

# Exemplo de uso
marca_carro = input("Digite a marca do carro: ")
meu_carro = Carro(marca=marca_carro)

marca_moto = input("Digite a marca da motocicleta: ")
minha_moto = Motocicleta(marca=marca_moto)

meu_carro.acelerar()
minha_moto.acelerar()
