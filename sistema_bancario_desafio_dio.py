menu = """

| [1] Depositar |
| [2] Sacar     |
| [3] Extrato   |
| [4] Sair      |

=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES_DIARIOS = 3

while True: 

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"| Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite_diario

        excedeu_saques = numero_saque >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Falha na operação! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Falha na operação! O valor do saque excedeu o limite diário.")

        elif excedeu_saques:
            print("Falha na operação! O número máximo de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"| Saque: R$ {valor:.2f}"
            numero_saque += 1

        else:
            print("Falha na operação! Valor informado inválido.")

    elif opcao == "3":
        print("===============Extrato================")
        print("| Não foram realizadas movimentações |" if not extrato else extrato)
        print("--------------------------------------")
        print(f"| Saldo: {saldo:.2f}")
        print("======================================")
    
    elif opcao == "4":
        break

    else:
        print("Falha na operação! Por favor selecione novamente a operação desejada.")

