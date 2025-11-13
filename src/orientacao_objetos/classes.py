from datetime import date
from typing import List
from rich.table import Table
from rich.console import Console

class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []


# Classe é uma representação de objeto do mundo real
class Jogo:
    def __init__(self):
        # atributos de classe
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: Desenvolvedora = None


def exemplo_01():
    # titulo = "GTA VI"
    # data_lancamento = date(2077, 2, 28)
    # preco = 650.00
    # genero = "Ação"
    # classificacao = "M"

    # gta_vi_dict = {
    #     "titulo": "GTA VI",
    #     "data_lancamento": date(2077, 2, 28),
    #     "preco": 650,
    #     "genero": "Ação",
    #     "classificacao": "M"
    # }

    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "Nova York"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    # Instaciando um objeto chamado gta_vi da classe Jogo
    gta_vi = Jogo() # nome_objeto = NomeClasse()
    # Definido valor para as atributos do objeto
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 650
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    gta_vi.preco = 669.99

    the_witcher = Jogo()
    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()
    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10, 27)
    league_of_legends.preco = 0
    league_of_legends.genero = "Moba"
    league_of_legends.classificacao = "12"

    # Adicionar os jogos na desenvolvedora
    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)


    colunas = ["Desenvolvedora",  "Título", "Data Lançamento", "Preço", "Gênero", "Classificação"]
    # Instancinado um objeto chamado tabela de classe Table
    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao
    )
    tabela.add_row(
        "N/A", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao
    )
    tabela.add_row(
        "N/A", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificacao
    )

    # Instanciando um objeto chamado console da Classe Console
    console = Console()
    console.print(tabela)


# ------------------------------------------------------------ Exerício 01 ----------------------------------------------------------------------------------------
class Marca:
    def __init__(self):
        self.nome: str = None
        self.id: int = None
        self.fundador: str = None
        self.data_fundacao: date = None
        self.faturamento: float = None

def exercicio_marca():
    adidas = Marca()
    adidas.nome = "Adidas"
    adidas.id = 1001
    adidas.fundador = "Adolf Dassler"
    adidas.data_fundacao = date(1924, 7, 10)
    adidas.faturamento = 129677275.00

    nike = Marca()
    nike.nome = "Nike"
    nike.id = 1002
    nike.fundador = "Bill Bowerman"
    nike.data_fundacao = date(1964, 1, 25)
    nike.faturamento = 272057630.00

    colunas = ["Nome", "ID", "Fundador", "Data da fundação", "Faturamento 2024"]
    tabela = Table(*colunas)

    tabela.add_row(
        adidas.nome, str(adidas.id), adidas.fundador, str(adidas.data_fundacao), str(adidas.faturamento)
    )
    tabela.add_row(
        nike.nome, str(nike.id), nike.fundador, str(nike.data_fundacao), str(nike.faturamento)
    )

    console = Console()
    console.print(tabela)


# ------------------------------------------------------------- Exercício 02 ---------------------------------------------------------------------------------------
class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.login: str = None
        self.data_nascimento: date = None


class Ticket:
    def __init__(self):
        self.numero: int = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao: str = None


def exercicio_ticket():
    usuario01 = Usuario()
    usuario01.id = 1005
    usuario01.nome_completo = "Lucas Vinícius Benevenutti"
    usuario01.login = "l.benevenutti"
    usuario01.data_nascimento = date(2000, 11, 5)

    usuario02 = Usuario()
    usuario02.id = 1006
    usuario02.nome_completo = "Felipe Fernando Correa"
    usuario02.login = "ff.correa"
    usuario02.data_nascimento = date(1999, 2, 13)

    ticket01 = Ticket()
    ticket01.numero = 4561
    ticket01.usuario = usuario01
    ticket01.data_abertura = date(2025, 11, 12)
    ticket01.status = "Em análise"
    ticket01.descricao = "Sistema não está permitindo impressão do relatório do giro de estoque"

    ticket02 = Ticket()
    ticket02.numero = 4552
    ticket02.usuario = usuario01
    ticket02.data_abertura = date(2025, 11, 2)
    ticket02.status = "Finalizado"
    ticket02.descricao = "Está dando erro no envio automático de cotação"
    ticket02.data_fechamento = date(2025, 11, 12)

    colunas = ["Ticket", "Usúario", "Data de abertura", "Status", "Descrição", "Data de fechamento"]
    tabela = Table(*colunas)

    tabela.add_row(
        str(ticket01.numero), ticket01.usuario.nome_completo, str(ticket01.data_abertura), ticket01.status, ticket01.descricao, "Ticket aberto"
    )
    tabela.add_row(
        str(ticket02.numero), ticket02.usuario.nome_completo, str(ticket02.data_abertura), ticket02.status, ticket02.descricao, str(ticket02.data_fechamento)
    )
    
    console = Console()
    console.print(tabela)


