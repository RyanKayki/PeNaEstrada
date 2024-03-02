import os


poltronas = {}

def reservar_poltrona():
    try:
        poltronas_livres = [
            poltrona
            for poltrona in range(1, 51)
            if poltrona not in poltronas
        ]
        print(f"Assentos livres: {poltronas_livres}")
        numero_poltrona = int(input("Escolha o lugar desejado (ímpar para Janela, par para Corredor): "))
        if numero_poltrona in poltronas:
            ocupada = poltronas[numero_poltrona]
            print(f"A poltrona {numero_poltrona} está ocupada por {ocupada}.")
        else:
            nome_passageiro = input("Informe o nome do estudante: ")
            if numero_poltrona % 2 == 1:
                print(f"Reserva realizada com sucesso para {nome_passageiro} na poltrona {numero_poltrona} (Janela).")
            else:
                print(f"Reserva realizada com sucesso para {nome_passageiro} na poltrona {numero_poltrona} (Corredor).")
            poltronas[numero_poltrona] = nome_passageiro
    except ValueError:
        print("Número de poltrona inválido.")

def liberar_poltrona():
    try:
        numero_poltrona = int(input("Informe o número da poltrona a ser liberada: "))
        if numero_poltrona in poltronas:
            nome_passageiro = poltronas.pop(numero_poltrona)
            print(f"Poltrona {numero_poltrona} liberada com sucesso. Passageiro {nome_passageiro}.")
        else:
            print("Poltrona não ocupada ou número inválido.")
    except ValueError:
        print("Número de poltrona inválido.")
 
def mostrar_poltronas():
    print("Estado das poltronas:")
    print("Janelas: \t\tCorredor:")
    for i in range(1, 51):
        if i in poltronas:
            print(f"Poltrona {i}: {poltronas[i]}", end='\t')
        else:
            print(f"Poltrona {i} está livre.", end='\t')
        if i % 2 == 0:
            print()

# Menu principal
while True:
    os.system('cls')
    print("PÉ NA ESTRADA - SISTEMA DE RESERVAS")
    print("----MENU----")
    print("Código [1] - Reservar poltrona")
    print("Código [2] - Liberar poltrona (desistência)")
    print("Código [3] - Mostrar estado das poltronas e passageiros")
    print("Código [4] - Sair do sistema")

    # Validação do MENU
    try:
        op_menu = int(input("Informe o código da opção desejada: "))
        if op_menu == 1:
            reservar_poltrona()
        elif op_menu == 2:
            liberar_poltrona()
        elif op_menu == 3:
            mostrar_poltronas()
        elif op_menu == 4:
            print("Saindo do sistema....")
            break
        else:
            print("Código inválido!")
    except ValueError:
        print("Valor inválido!")

    input("Pressione Enter para continuar...")
