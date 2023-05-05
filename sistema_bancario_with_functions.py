def depositar(valor, saldo, depositos):
    
    if valor > 0.0:
        saldo += valor
        depositos.append(valor)
        return saldo
        
    else:
        return False 

def extrato(saldo, depositos):
    deposito_extrato = f""
    for deposito in depositos:
        deposito_extrato = f"Deposito(s): {deposito:10.2f}\n"

    extrato =f"""
    ####################
    ##### EXTRATO ######
    {deposito_extrato}

    SALDO: {saldo:10.2f}
    ####################

    """
    return extrato

def main():
    menu = (
          f"""
            #### MENU ####
            Escolha umas das opções:
            (d) Depositar
            (e) Extrato
            (q) Sair
            => """
            )

    saldo = 150
    depositos = []

    while True:

        op = input(menu).lower()
        if op == "d":
            valor = float(input("Digite o valor do depósito: "))
            if depositar(valor, saldo, depositos):
                print(f"R$ {valor:.2} Depositado")
            else:
                print("Não depositamos valores negativos.")
        
        else:
            print("Opção Inválida!!")
    

main()
