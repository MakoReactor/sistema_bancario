from abc import ABC, abstractmethod, abstractproperty


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # falta implementar a classe transacao que tem
        # o metodo registrar
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()   # falta implementar a classe

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f'\n *** Você não tem saldo ***')
        elif valor > 0:
            self._saldo -= valor
            print('\n Saque realizado com sucesso')
            return True
        else:
            print('\n *** Valor Inválido *** ')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\nValor depositado com sucesso')
        else:
            print('O valor informado é inválido')
            return False

        return True


class Historico:
    pass
