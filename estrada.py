import os

poltronas = {}

def reservar_poltrona():
    try:
        escolha = input("Escolha o lugar desejado (para Janela (J),para Corredor (C)): ").upper()

        try:
            if escolha == 'J':
                poltronas_livres = [
                    poltrona
                    for poltrona in range(1, 51, 2)
                    if poltrona not in poltronas
                ]
            elif escolha == 'C':
                poltronas_livres = [
                    poltrona
                    for poltrona in range(2, 51, 2)
                    if poltrona not in poltronas
                ]
            else:
                print("Lugar invalído...")
                return

            print(f"Assentos livres: {poltronas_livres}")

            if poltronas_livres:
                numero_poltrona = int(input("Escolha o Numero da poltrona que deseja sentar: "))
    
                if escolha == "C":
                    probabilidade = numero_poltrona % 2 == 1
                    if probabilidade == 1:
                        mudar = input("deseja mudar para poltronas na janela? (S/N): ").upper()
                        if mudar == 'S':
                            return
                        else:
                            print("Escolha os assentos disponiveis")
                            return
                    
                elif escolha == "J":
                    probabilidade = numero_poltrona % 2 == 1
                    if probabilidade == 0:
                        mudar = input("deseja mudar para poltronas na corredor? (S/N): ").upper()
                        if mudar == 'S':
                            return
                        else:
                            print("Escolha os assentos disponiveis")
                            return
                
                if numero_poltrona < 1 or numero_poltrona > 50:
                    print("Assento inválido. Por favor, escolha um número entre 1 e 50.")
                    return

                if numero_poltrona in poltronas:
                    ocupada = poltronas[numero_poltrona]
                    print(f"A poltrona {numero_poltrona} está sendo ocupada por {ocupada}.")
                else:
                    nome_passageiro = input("Informe o nome do estudante: ")
                    tipo_poltrona = "Janela" if numero_poltrona % 2 == 1 else "Corredor"
                    print(f"Reserva realizada com sucesso para {nome_passageiro} na poltrona {numero_poltrona} ({tipo_poltrona}).")
                    poltronas[numero_poltrona] = nome_passageiro
            else:
                print("Não há assentos disponíveis para o tipo escolhido.")

        except ValueError:
            print("Número de poltrona inválido.")

    except ValueError:
        print("Escolha inválida para o tipo de assento.")


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

def privacidade_poltronas():
    print("Estado das poltronas:")
    print("Janelas: \t\tCorredor:")  
    assento_escolhido = int(input("Em qual assento você está? "))
    if assento_escolhido < 1 or assento_escolhido > 50:
        print("Assento inválido. Por favor, escolha um número entre 1 e 50.")
        return
    lado = assento_escolhido + 1 

    if assento_escolhido:
        assento_escolhido % 2 == 1
    else: 
        assento_escolhido - 1
    

    if assento_escolhido not in poltronas:
        estado_assento= "livre"
    else:
        estado_assento = poltronas[assento_escolhido]
    

    if lado not in poltronas:
        estado_lado = "livre"
    else:
        estado_lado = poltronas[lado]
    
    print(f"Poltrona {assento_escolhido}: {estado_assento}\tPoltrona {lado}: {estado_lado}")
    resposta = input(f"Deseja comprar a Poltrona {lado}? (S/N): ").upper()
    if resposta == 'S':
        nome_passageiro = input("Informe o seu nome: ")
        poltronas[assento_escolhido] = poltronas[lado] = nome_passageiro
        print(f"Poltrona {lado} também foi reservada para {nome_passageiro}.")


# Menu principal
while True:
    os.system('cls')
    print("PÉ NA ESTRADA - SISTEMA DE RESERVAS")
    print("----MENU----")
    print("Código [1] - Reservar poltrona")
    print("Código [2] - Liberar poltrona (desistência)")
    print("Código [3] - Mostrar estado das poltronas e passageiros")
    print("Código [4] - Mostrar a poltrona ao lado (privacidade)")
    print("Código [5] - Sair do sistema")

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
            privacidade_poltronas()
        elif op_menu == 5:
            print("Saindo do sistema....")
            break
        else:
            print("Código inválido!")
    except ValueError:
        print("Valor inválido!")

    input("Pressione Enter para continuar...")
