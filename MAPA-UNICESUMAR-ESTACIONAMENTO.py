from datetime import datetime

print('Bem vindo ao Unicesumar Parking')
n = str(input('Digite o seu nome completo: ')).capitalize()
nome = n.split()
print('Seja bem vindo {}. \n Com qual das opções você deseja prosseguir?↧↧'.format(nome[0]))
# Armazena os veículos com horário de entrada
veiculos = {}

# Total arrecadado no dia
total_arrecadado = 0.0

# Horário de funcionamento
HORARIO_ABERTURA = datetime.strptime("08:00", "%H:%M").time()
HORARIO_FECHAMENTO = datetime.strptime("18:00", "%H:%M").time()

def registrar_entrada():
    placa = input("Digite a placa do veículo: ").upper()
    horario_str = input("Digite o horário de entrada (HH:MM): ")
    horario = datetime.strptime(horario_str, "%H:%M").time()

    if horario < HORARIO_ABERTURA or horario >= HORARIO_FECHAMENTO:
        print("Estacionamento fechado. Funciona das 08:00 às 18:00.")
        return

    veiculos[placa] = horario_str
    print(f"Entrada registrada para {placa} às {horario_str}.")

def registrar_saida():
    global total_arrecadado

    placa = input("Digite a placa do veículo para saída: ").upper()

    if placa not in veiculos:
        print("Veículo não encontrado.")
        return

    entrada_str = veiculos[placa]
    entrada = datetime.strptime(entrada_str, "%H:%M")
    saida_str = input("Digite o horário de saída (HH:MM): ")
    saida = datetime.strptime(saida_str, "%H:%M")

    tempo_minutos = (saida - entrada).total_seconds() / 60

    if tempo_minutos <= 15:
        valor = 0.0
    elif tempo_minutos <= 60:
        valor = 1.50
    else:
        horas_extras = ((tempo_minutos - 60) / 60)
        valor = 1.50 + (int(horas_extras) + (1 if horas_extras % 1 > 0 else 0)) * 1.00

    total_arrecadado += valor
    print(f"Tempo de permanência: {int(tempo_minutos)} minutos")
    print(f"Valor a pagar: R$ {valor:.2f}")
    del veiculos[placa]

def fechar_estacionamento():
    global total_arrecadado

    print("\nFechando o estacionamento...")
    for placa in list(veiculos.keys()):
        entrada_str = veiculos[placa]
        entrada = datetime.strptime(entrada_str, "%H:%M")
        saida = datetime.strptime("18:00", "%H:%M")
        tempo_minutos = (saida - entrada).total_seconds() / 60

        if tempo_minutos <= 15:
            valor = 0.0
        elif tempo_minutos <= 60:
            valor = 1.50
        else:
            horas_extras = ((tempo_minutos - 60) / 60)
            valor = 1.50 + (int(horas_extras) + (1 if horas_extras % 1 > 0 else 0)) * 1.00

        total_arrecadado += valor
        print(f"{placa} foi retirado automaticamente às 18:00. Valor cobrado: R$ {valor:.2f}")

    veiculos.clear()
    print(f"\nTotal arrecadado no dia: R$ {total_arrecadado:.2f}")

# Menu simples
def menu():
    while True:
        print("\n=== SISTEMA DE ESTACIONAMENTO ===")
        print("1. Registrar entrada")
        print("2. Registrar saída")
        print("3. Fechar estacionamento")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            fechar_estacionamento()
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

menu()