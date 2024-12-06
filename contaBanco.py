menu = """
***********ESCOLHA UMA OPÇÃO***********
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
-------------------------------------

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Saldo excede o limite.")

        elif excedeu_saques:
            print("Quantidade de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido.")

    elif opcao == "3":
        print("\n***********EXTRATO***********")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, selecione uma operação.")

      
