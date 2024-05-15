class contados:
    def __init__(self):
        self.__valor= 0
    def incrementar(self):
        self.__valor+= 1
    
    def decrementar(self):
        if self.__valor>0:
            self.__valor-=1
    def get_valor(self):
        return self.__valor
    
contador=contados()
contador.incrementar()
contador.incrementar()
print(contador.get_valor())
contador.decrementar()
print(contador.get_valor())