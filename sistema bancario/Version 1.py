menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato ++ f"depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! o valor informado é invalido")

        elif excedeu_limite:
            print("Operação falhou! o valor informado é invalido")

        elif excedeu_saques:
            print("Operação falhou! o valor informado é invalido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é invalido")
        
    elif opcao == "e":
        print("\n================= EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por facor selecione novamente a operação desejada.")