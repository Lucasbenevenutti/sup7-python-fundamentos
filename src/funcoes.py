def funcao_sem_retorno():
    print("Olá mundo")

def funcao_com_retorno() -> str:
    produto : str = "iPhone 17 Pro Max"
    return produto

def funcao_executar():
    funcao_sem_retorno()

    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)

def solicitar_nome_jogo() -> str:
    nome : str = input("Digite o nome do jogo: ").strip()
    return nome

def solicitar_preco_jogo() -> float:
    preco : float = float(input("Digite o preço: "))
    return preco

def solicitar_quantidade_jogo() -> int:
    quantidade : int = int(input("Digite a quantidade: "))
    return quantidade

def solicitar_pedido_fechado() -> bool:
    pedido_fechado : str = input("Pedido fechado (s/n): ").strip().lower()
    if pedido_fechado == "s":
        return True
    else:
        return False

def solicitar_valor_pagamento():
    valor_pagamento : float = float(input("Digite o valor pago: "))
    return valor_pagamento

def processar_pedido():
    nome : str = solicitar_nome_jogo()
    preco : float = solicitar_preco_jogo()
    quantidade : int = solicitar_quantidade_jogo()
    pedido_fechado: bool = solicitar_pedido_fechado()

    valor_pedido : float = quantidade * preco
    print("\n\nValor pedido: " + str(valor_pedido))

    if pedido_fechado == True:
        valor_pagamento = solicitar_valor_pagamento()
        if valor_pagamento > valor_pedido:
            valor_troco = valor_pagamento - valor_pedido
            print("Troco: " + str(valor_troco))
            print("Status: Pedido realizado")
        elif valor_pagamento == valor_pedido:
            print("Pedido sem troco")
            print("Status: Pedido realizado")
        else:
            valor_faltante = valor_pedido - valor_pagamento
            print("Valor faltante: " + str(valor_faltante))
            print("Status: Pedido cancelado")

# ------------------------------------ Exemplo de cálculo de compra no Paraguai ---------------------------------------------------------------


def solicitar_cotacao_dolar() -> float:
    cotacao: float = float(input("Digite o valor da cotação do dolar hoje: ").replace(",", "."))
    return cotacao

def solicitar_nome_produto() -> str:
    nome = input("Digite o nome do produto: ")
    return nome

def solicitar_valor_produto_dolar() -> float:
    valor_produto_em_dolar: float = float(input("Digite o valor do produto em Dolar: ").replace(",", "."))
    return valor_produto_em_dolar

def solicitar_se_pagara_imposto() -> bool:
    pagar_imposto: str = input("Pagara o imposto? (s/n): ").strip().lower()
    if pagar_imposto == "s":
        return True
    else:
        return False

def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    deseja_utilizar: str = input("Deseja utilizar a cota de dolar mensal? (s/n): ").strip().lower()
    if deseja_utilizar == "s":
        return True
    else:
        return False

def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float
):
    cotacao_mensal = 500.00
    # Calcular o valor que será utilizado para descobrir quanto a mais será pago de imposto
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""
    Valor total do produto: $ {valor_produto_dolar}
    Valor total do produto: R$ {valor_produto_reais}
    Valor imposto: R$ {valor_imposto_reais}

    Valor total do produto com imposto: R$ {valor_total_produto_reais} """)

def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float,
):
    valor_imposto_dolar = valor_produto_dolar / 2 # 50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("Valor total do produto com imposto: " + str(valor_total_produto_reais))


def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar()
    nome_produto: str = solicitar_nome_produto()
    valor_produto_dolar: float = solicitar_valor_produto_dolar()
    pagara_imposto: bool = solicitar_se_pagara_imposto()

    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    if pagara_imposto == True:
        utilizar_cota_dolar_mensal = solicitar_deseja_utilizar_cota_dolar_mensal()

        # Descobrir o valor do produto para calcular o imposto
        if utilizar_cota_dolar_mensal ==  True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
    else:
        print("Valor do produto sem pagar imposto: " + str(valor_produto_reais))


# ------------------------------------------------------ Atividade  ------------------------------------------------------------------------

# Ex.1 : Criar uma função chamada exercicio_aluno
# Solicitar o nome (criar função)
# Solicitar nota 1 (criar função)
# Solicitar nota 2 (criar função)
# Solicitar nota 3 (criar função)
# Calcular a média e apresentar
# Criar um if que verifique se o aluno está ou não aprovado e apresentar
# Solicitar a idade (criar função)
# Solicitar o peso (criar função)
# Solicitar a altura (criar função)
# Calcular o imc do aluno e apresentar a classificação
# Apresentar a ageração de acordo com a idade
# Solicitar o cargo (criar função)
# Apresentar salário de acordo com cargo
#   Estagiário R$ 850,00
#   Junion R$ 1800,00
#   Pleno R$ 4000,00
#   Senior R$ 6000,00


def solicitar_nome_aluno() -> str:
    nome_aluno: str = input("Digite o nome do aluno: ")
    return nome_aluno

def solicitar_nota_1() -> float:
    nota_1: float = float(input("Digite a nota 1: "))
    return nota_1

def solicitar_nota_2() -> float:
    nota_2: float = float(input("Digite a nota 2: "))
    return nota_2

def solicitar_nota_3() -> float:
    nota_3: float = float(input("Digite a nota 3: "))
    return nota_3

def solicitar_idade() -> int:
    idade_aluno: int = int(input("Digite a idade do aluno: "))
    return idade_aluno

def solicitar_peso() -> float:
    peso_aluno: float = float(input("Digite o peso do aluno: "))
    return peso_aluno

def solicitar_altura() -> float:
    altura_aluno: float = float(input("Digite a altura do aluno: "))
    return altura_aluno


def dados_aluno():
    nome: str = solicitar_nome_aluno()
    nota1: float = solicitar_nota_1()
    nota2: float = solicitar_nota_2()
    nota3: float = solicitar_nota_3()

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print("Aluno aprovado com a média: " + str(media))
    else:
        print("Aluno reprovado com a média: " +str(media))
    
    idade: int = solicitar_idade()
    peso: float = solicitar_peso()
    altura: float = solicitar_altura()

    imc: float = peso / (altura * altura)

    if imc <= 18.5:
        print("Classificação: Abaixo do peso, IMC: " + str(imc))
    elif imc >= 18.6 and imc <= 24.9:
        print("Classificação: Peso normal, IMC: " + str(imc))
    elif imc >= 25 and imc <= 29.9:
        print("Classificação: Sobrepeso, IMC: " + str(imc))
    elif imc >= 30 and imc <= 34.9:
        print("Classificação: Obesidade Grau I, IMC: " + str(imc))
    elif imc >= 35 and imc <= 39.9:
        print("Classificação: Obesidade Grau II, IMC: " + str(imc))
    else:
        print("Classificação: Obesidade Grau III, IMC: " + str(imc))


    
