class Termometro:
    def __init__(self, temperatura=0):
        self.__temperatura_celsius = temperatura
    
    @property
    def temperatura_celsius(self):
        return self.__temperatura_celsius
    
    @temperatura_celsius.setter
    def temperatura_celsius(self, temperatura):
        self.__temperatura_celsius = temperatura
    
    @property
    def temperatura_fahrenheit(self):
        return (self.__temperatura_celsius * 9/5) + 32
    
    @temperatura_fahrenheit.setter
    def temperatura_fahrenheit(self, temperatura):
        self.__temperatura_celsius = (temperatura - 32) * 5/9

# Uso da classe
temperatura_inicial = float(input("Digite a temperatura inicial em Celsius: "))
termometro = Termometro(temperatura_inicial)

print("Temperatura em Celsius:", termometro.temperatura_celsius)
print("Temperatura em Fahrenheit:", termometro.temperatura_fahrenheit)

nova_temperatura = float(input("Digite a nova temperatura em Celsius: "))
termometro.temperatura_celsius = nova_temperatura
print("Nova temperatura em Celsius:", termometro.temperatura_celsius)
print("Nova temperatura em Fahrenheit:", termometro.temperatura_fahrenheit)
