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

# Criar Usuário
def criar_usuario(usuarios):
    
    cpf = input("Digite o CPF: ")
    
    if verifica_usuario(usuarios, cpf):
        print("usuário já existe!")
        return False



    nome = input("Digite o nome: ")
    endereco = input("Digite o endereco: ")
    data_nascimento = input("Data de Nascimento: ")

    dicionario = {
            'cpf': cpf,
            'nome': nome,
            'endereco': endereco,
            'data_nascimento': data_nascimento,
            }
    return dicionario

def criar_conta(usuarios, agencia, numero_contas):
    cpf = input("Digite o CPF para a conta: ")
    if not verifica_usuario(usuarios, cpf):
        print("Cliente não existe, tente outro cpf!")
        return False

    conta = {
            'cpf': cpf,
            'agencia':agencia,
            'conta_corrente': numero_contas
            }
    return conta




def verifica_usuario(usuarios, cpf):

    for i in usuarios:
        if i['cpf'] == cpf:
            return True

    return False

def lista_contas(contas):
    lista_contas=''
    for i in contas:
        lista_contas += f"\n\tAgência: {i['agencia']} Nº Conta: {i['conta_corrente']} CPF: {i['cpf']}    "
    
    listar = (
    f"""
    ##############################################
               * Contas Corrente *
    {lista_contas}
    ##############################################
    """
    )
    print(listar)


def menu():
    menu = (
    f"""
    ########## MENU ##########
    Escoha uma opção:
    (d)    Depositar
    (s)    Sacar
    (e)    Extrato
    (c)    Criar Conta
    (u)    Criar Usuário
    (l)    Listar Contas
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
    clientes = []
    contas = []
    numero_contas = 1 
    AGENCIA = '0001'


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
        elif op == 'u':
            cliente = criar_usuario(clientes)
            if cliente:
                clientes.append(cliente)

        elif op == 'c':
            conta = criar_conta(clientes, AGENCIA , numero_contas)
            if conta:
                contas.append(conta)
                numero_contas += 1
        elif op == 'l':
            lista_contas(contas)
        
        else:
            break

            

            

main()
