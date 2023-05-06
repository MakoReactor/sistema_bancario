def depositar(valor, saldo, depositos):
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"R$ {valor:.2f} depositado")
    else:
        print("Valor informado fora do padrão.")
    
    return saldo

def sacar(*, valor, saldo, saques, limite):
    if len(saques) >= 3:
        print("Numero de saque exedidos no dia.")
    elif valor <= 0:
        print("Valor menor igual a zero")
    elif valor > limite:
        print("Valor acima do limite.")
    elif valor > saldo:
        print("Saque não permite saldo negativo")
    else:
        saldo -= valor
        saques.append(valor)
        print("Saque realizado com sucesso!")
    
    return saldo
    


def extrato(saldo, depositos, saques):
    ext_dep = ""
    ext_saq = ""
    
    for deposito in depositos:
        ext_dep = ext_dep + f"Depósito(s) (+) R$ {deposito:.2f}\n    "
    
    for saque in saques:
        ext_saq = ext_saq + f"Saque(s) (-) R$ {saque:.2f}\n    "

    extrato = (
    f"""
    ######### Extrato ###########
    {ext_dep}
    {ext_saq}
    Saldo: R$ {saldo:.2f}
    #############################
    """
           )
    print(extrato)



def menu():
    menu = (
    f"""
    ########## MENU ##########
    Escoha uma opção:
    (d)    Depositar
    (s)    Sacar
    (e)    Extrato
    (q)    Sair
    ###########################
     => """)
    escolha = input(menu)
    return escolha.lower()

def main():
    saldo = 0.0
    depositos = []
    saques = []
    limite = 500.0
    
    
    while True:
        op = menu()
        if op == 'd':
            valor = float(input("Informe o valor do depósito: "))
            saldo = depositar(valor, saldo, depositos)
        elif op == 'e':
            extrato(saldo, depositos, saques)
        elif op == "s":
            valor = float(input("Digita o valor a sacar: "))
            saldo = sacar(valor=valor, saldo=saldo,saques=saques, limite=limite)

        else:
            break

            

            

main()
