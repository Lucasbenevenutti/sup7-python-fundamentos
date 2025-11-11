from typing import Dict, List
from src.arquivos import ler_json, escrever_json
from rich.console import Console
from rich.table import Table

def resolver():
    # Ler o arquivo e convertendo para uma lista de dicionário
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta")
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")
        email = dados_pessoais.get("email")

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano
        }

        if status == "ativo":
            ativos.append(dados)
        elif status == "suspenso":
            suspensos.append(dados)
        else:
            inativos.append(dados)

    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")

    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(inativos, "Contas Inativas")
    apresentar_tabela(suspensos, "Contas Suspenas")

def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("E-mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")

    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome"),
            dado.get("email"),
            dado.get("tipo"),
            str(dado.get("pontos")),
            dado.get("plano"),
        )

    console = Console()
    console.print(table)


# Exercício 01: 

def exercicio_01():
    
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    free = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano")

        dado = {
            "nome": nome,
            "plano": plano
        }

        if plano == "Free":
            free.append(dado)
        
    
    escrever_json(free, "data/free.json")


def exercicio_02():

    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    lista_tags = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")

        tags = usuario.get("tags")

        dado = {
             "tags": nome
        }
        


        if tags != []:
            lista_tags.append(tags)

        escrever_json(lista_tags, "data/tags.json")


def exercicio_03():
    
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    lista_enderecos = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        dados_pessoais = usuario.get("dados_pessoais")
        endereco = dados_pessoais.get("endereco")
        rua = endereco.get("rua")
        numero = endereco.get("numero")
        bairro = endereco.get("bairro")
        cep = endereco.get("cep")
        uf = endereco.get("uf")

        dado = [
            {
                "rua": rua,
                "numero": numero,
                "bairro": bairro,
                "cep": cep,
                "uf": uf
            }
        ]

        lista_enderecos.append(dado)

    escrever_json(lista_enderecos, "data/enderecos.json")
        