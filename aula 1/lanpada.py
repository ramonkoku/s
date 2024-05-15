class Lampada:
    def __init__(self):
        self.estado = False  # Começa desligada
        
    def alterar_estado(self, novo_estado=None):
        if novo_estado is not None:
            self.estado = novo_estado
        else:
            self.estado = not self.estado
            
        if self.estado:
            print("Lâmpada ligada.")
        else: 
            print("Lâmpada desligada.")

if __name__ == "__main__":
    lampada = Lampada()
    print("Digite 'ligar' para ligar a lâmpada ou 'desligar' para desligar:")
    while True:
        comando = input("Comando: ").lower()
        if comando == 'ligar':
            lampada.alterar_estado(True)
        elif comando == 'desligar':
            lampada.alterar_estado(False)
        else:
            print("Comando inválido. Digite 'ligar' ou 'desligar'.")
