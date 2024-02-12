class Conta:
    def __init__(self, titular, numero, saldo):

        self._saldo = 0
        self.numero = numero
        self._titular = titular

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        if (saldo < 0):
            print("O Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if(self, valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo Insuficiente")

    def deposita(self, valor):
        self.saldo += valor
