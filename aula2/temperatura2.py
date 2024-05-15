def receber_dados_temperatura():
    return float(input("Digite a temperatura atual: "))

def processar_dados(dados):
    print('Dados de temperatura recebidos e processados:', dados)

def verificar_sinal_desligamento(dados_temperatura):
    if dados_temperatura > 90:
        print("Temperatura muito alta. O programa será encerrado.")
        return True
    else:
        return False

sinal_desligamento = False

while not sinal_desligamento:
    dados_temperatura = receber_dados_temperatura()
    processar_dados(dados_temperatura)
    sinal_desligamento = verificar_sinal_desligamento(dados_temperatura)
