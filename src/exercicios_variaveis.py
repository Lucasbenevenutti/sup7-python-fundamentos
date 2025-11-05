def exercicios_dados_produtos():
    nome: str = input("Digite o nome do produto: ")
    quantidade: float = float(input("Digite a quantidade do produto: "))
    preco: float = float(input("Digite o valor unitário do produto: "))
    categoria: str = input("Digite a categoria do produto")

    valor_total: float = quantidade * preco

    print("Nome do produto: " + str(nome) + ", valor total da compra: " + str(valor_total))