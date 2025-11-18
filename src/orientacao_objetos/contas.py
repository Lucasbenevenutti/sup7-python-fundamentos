from typing import List


class Conta:
    def __init__(self, titular: str, saldo_inicial: float):
        """"Construtor da classe. Inicializa o titular e o saldo"""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor_deposito: float):
        """Adiciona um valor ao saldo da conta."""
        if valor_deposito <= 0:
            print(f"DEPÓSITO: Valor de depósito inválido R${valor_deposito:.2f}")
            return
        
        self.saldo = self.saldo + valor_deposito
        print(f"DEPÓSITO: Depósito de R${valor_deposito:.2f} realizado com sucesso")

    def sacar(self, valor_saque: float):
        """Remove um valor do saldo da conta, se houver dinheiro suficiente."""
        if valor_saque > self.saldo:
            print(f"SAQUE: Saldo insuficiente para realizar o saque de R${valor_saque:.2f}")
        else:
            self.saldo = self.saldo - valor_saque
            print(f"SAQUE: Saque de R${valor_saque:.2f} realizado com sucesso")

    def exibir_saldo(self):
        """Mostra o status atual da conta"""
        print(f"EXTRATO: Saldo atual de R${self.saldo:.2f}")



def exemplo_conta():
    """Método para testar a funcionalidade da conta"""
    conta_bradesco = Conta("Vitor", 3900.22)

    conta_bradesco.exibir_saldo()
    conta_bradesco.sacar(800)

    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78)
    conta_bradesco.depositar(-10)

    conta_bradesco.sacar(4000)

    conta_bradesco.sacar(3500)
    conta_bradesco.sacar(3201)
    conta_bradesco.exibir_saldo()


#exemplo_conta()


# Criar uma classe Aluno com um construtor que receba o nome do aluno
# Dentro do construtor deve criar uma lista vazia de notas

# Criar um método adicionar que recebe como parâmetro a nota e adiciona na lista de notas
# Criar um método que apresenta as notas
# Criar um método calcularMedia que percorre cada uma das notas e apresenta a média para o usuário

class Aluno:
    def __init__(self, aluno: str):
        self.aluno = aluno
        self.notas = []
        self.media = 0

    def adiconar_nota(self, nota: float):
        self.notas.append(nota)
    
    def apresentar_notas(self):
        print(f"notas {self.notas}")
    
    def calcularMedia(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        
        self.media = soma / len(self.notas)

def exercicio_notas():
    aluno = Aluno("Lucas")
    aluno.adiconar_nota(8.5)
    aluno.adiconar_nota(9)
    aluno.adiconar_nota(7)

    aluno.apresentar_notas()

    aluno.calcularMedia()
    print(f"A media do aluno {aluno.aluno}: {aluno.media:.2f}")

exercicio_notas()        