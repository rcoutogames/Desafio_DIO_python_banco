menu = """

[d] depositar
[s] sacar 
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0: # verificando se o valor informado e maior que zero n pode ser negativo
            saldo += valor # ele sendo maior q zero e adicionado ao saldo
            extrato += f"Deposito: R$ {valor:.2f}\n" # concatenamos e adicionamos ao extrato

        else:
            print("Operação Falhou ! O valor informado é invalido. ")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        # aqui são 3 verificações 
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("operação falhou! Voce não tem saldo suficiente. ")


        elif excedeu_limite:
            print("operação falhou! Voce excedeu o limite.")    

        elif excedeu_saques:
            print("operação falhou! Voce excedeu numero de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operação falho! O valor não é valido. ")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("não foram realizada movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========")

    elif opcao == "q":
        break

    else:
        print("operação invalida, por gentileza selecione a opção desejada. ")
