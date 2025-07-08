# Função para exibir o menu e capturar a opção do usuário
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu).lower()


# Função para realizar depósito
def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
    return saldo, extrato


# Função para realizar saque
def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")

        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite por operação.")

        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

    return saldo, extrato, numero_saques


# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==========================================")


# Função principal
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


# Executa o programa principal
if __name__ == "__main__":
    main()
