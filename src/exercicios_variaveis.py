from datetime import datetime
from questionary import select, confirm
import os


categorias = [
    "Esportes",
    "Roupas Esportivas",
    "Calças",
    "Acessórios",
    "Equipamentos",
    "Suplementos e Nutrição",
    "Marcas",
    "Ofertas e Categorias Especiais",
]

regioes = [
    "Sul",
    "Sudeste",
    "Centro-Oeste",
    "Norte",
    "Nordeste",
]


def exercicios_dados_produto():
    nome : str = input("Digite o nome do produto: ")
    categoria_escolhida = select("Escolha a categoria: ", choices=categorias).ask()
    quantidade : int = int(input("Digite a quantidade: "))
    preco : float = float(input("Digite o preço: "))
    data_venc_str = input("Digite a data de vencimento (dd/mm/aaaa): ")
    data_vencimento = datetime.strptime(data_venc_str, "%d/%m/%Y").date()
    hoje = datetime.today().date()
    regiao_entrega = select("Escolha a região de entrega: ", choices=regioes).ask()
    solicitar_cupom = input("Digite um cupom promocional: ").strip().upper()
    desconto : float = 0

    if data_vencimento < hoje:
        print("Produto vencido! Compra não permitida.")
        return  
    
    if categoria_escolhida == "Esportes":
        desconto = 10
    elif categoria_escolhida == "Roupas Esportivas":
        desconto = 15
    elif categoria_escolhida == "Calças":
        desconto = 20
    elif categoria_escolhida == "Acessórios":
        desconto = 12
    elif categoria_escolhida == "Equipamentos":
        desconto = 8
    elif categoria_escolhida == "Suplementos e Nutrição":
        desconto = 5
    elif categoria_escolhida == "Marcas":
        desconto = 7
    elif categoria_escolhida == "Ofertas e Categorias Especiais":
        desconto = 25

    subtotal : float = quantidade * preco
    valor_desconto : float = subtotal * (desconto / 100)
    total : float = subtotal - valor_desconto

    desconto_extra = 0

    if data_vencimento == hoje:
        desconto_extra = valor_desconto * 0.7

    elif data_vencimento.month == hoje.month and data_vencimento.year == hoje.year:
        desconto_extra = 20

    total = subtotal - (valor_desconto + desconto_extra)

    valor_frete: float
    if total > 500:
        valor_frete = 0
    else:
        if regiao_entrega == "Sul":
            valor_frete = 25
        elif regiao_entrega == "Sudeste":
            valor_frete = 35
        elif regiao_entrega == "Centro-Oeste":
            valor_frete = 45
        elif regiao_entrega == "Norte":
            valor_frete = 55
        elif regiao_entrega == "Nordeste":
            valor_frete = 50

    desconto_cupom = 0
    if solicitar_cupom == "SUPER10":
        desconto_cupom = 10
    elif solicitar_cupom == "FRETEGRATIS":
        valor_frete = 0
    elif solicitar_cupom == "PRIME20":
        desconto_cupom = 20
    elif solicitar_cupom == "CLIENTEVIP":
        desconto_cupom = 25

    total = total - (desconto_cupom / 100)

    resumo = f"""🧾 RESUMO DO PEDIDO
------------------------------------
Produto: {nome}
Categoria: {categoria_escolhida}
Quantidade: {quantidade}
Preço Unitário: R$ {preco:.2f}
Total Bruto: R$ {(subtotal + valor_frete):.2f}
Desconto Categoria {desconto}%: (R$ {valor_desconto:.2f})
Desconto Cupom: R$ {desconto_cupom:.2f}
Desconto Extra: R$ {desconto_extra:.2f}
Frete: R$ {valor_frete:.2f}
------------------------------------
💰 Total a Pagar: R$ {(total + valor_frete):.2f}
📅 Vencimento: {data_vencimento.strftime("%d/%m/%Y")}
📦 Região: {regiao_entrega}
------------------------------------
Obrigado por comprar conosco! 😄
"""

    print(resumo)
    
    salvar = confirm("Deseja salvar o resumo do pedido em um arquivo .txt na área de trabalho?").ask()

    if salvar:
        caminho_desktop = os.path.expanduser("~/OneDrive/Área de Trabalho")
        caminho_arquivo = os.path.join(caminho_desktop, "resumo_pedido.txt")

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(resumo)

        print(f"\n✅ Arquivo 'resumo_pedido.txt' foi salvo na área de trabalho com sucesso!")
    else:
        print("\nResumo não foi salvo. Obrigado por usar o sistema! 😊")