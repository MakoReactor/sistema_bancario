menu = """
    ######### MENU #########

    (d) depositar
    (s) sacar
    (e) extrato
    (q) sair

==> """
limite = 500
numero_de_saques = 3
qnt_saques = []
qnt_depositos = [] 
saldo = 300

while True:
    op = input(menu)
    op = op.lower()

    if op == 'd':

        valor = int(input("Valor do Depósito: "))
        if valor > 0:
            saldo += valor
            print(f"Novo Saldo: R$ {saldo:.2f}")
            qnt_depositos.append(valor)
        else:
            print("Operação falhou: Valor informado fora do padrão.") 


    elif op == 's':
        saque = int(input("Quanto quer sacar? "))
        if len(qnt_saques) >= 3:
            print("Quantidade de saques diárias excedida.")
        elif saque < 0 or saque > limite:
            print("Valor fora do esptipulado no limite diário.")
        elif saque > saldo:
            print("Operação não realizada")
            print("Saldo Insuficiente.")
        else:
            saldo -= saque 
            qnt_saques.append(saque)
            print("Saque efetuado!")

    elif op == 'e':
        depositos = """"""
        saques = """"""

        if len(qnt_depositos) > 0:
            for i in qnt_depositos:
                depositos = depositos + f"Deposito: R$+ {i:9.2f}\n    " 
        else:
            depositos = f"Sem mov. de deósitos."

        if len(qnt_saques) > 0:
            for s in qnt_saques:
                saques = saques + f"Saque: R$- {s:12.2f}\n    "
        else:
            saques = f"Sem mov. de Saques"


        extrato = f"""
    ########################    
    ####### EXTRATO ########

    {depositos}
    {saques}

    SALDO: RS {saldo:13.2f}
    ########################
    """
        print(extrato)
    elif op == 'q':
        print('Sair')
        break
    else:
        print("Opção inválida por favor tente outra vez!")
