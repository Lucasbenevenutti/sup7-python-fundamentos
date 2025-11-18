from enum import Enum
from typing import List


# region Console
class MarcaEnum(Enum):
    SONY = "Sony"
    MICROSOFT = "Microsoft"


class Console:
    def __init__(self):
        self.marca: MarcaEnum
        self.modelo: str = ""


def exemplo_consoles():
    # Instaciar um objeto
    play_station = Console()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "PS1"

    play_station_2 = Console()
    play_station_2.marca = MarcaEnum.SONY
    play_station_2.modelo = "PS2"

    xbox = Console()
    xbox.marca = MarcaEnum.MICROSOFT
    xbox.modelo = "Xbox"
# endregion


class PessoaTipo(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"


class Pessoa:
    def __init__(self):
        self.nome: str
        self.cpf_cnpj: str
        self.tipo: PessoaTipo


def exemplo_pessoas():
    creber = Pessoa()
    creber.nome = "Cleiton"
    creber.cpf_cnpj = "82.654.088/0001-20"
    creber.tipo = PessoaTipo.JURIDICA

    print(
        "PESSOA:",
        creber.nome,
        "CPF/CNPJ:",
        creber.cpf_cnpj,
        "TIPO:",
        creber.tipo.value,
    )


if __name__ == "__main__":
    exemplo_pessoas()



# Criar um enum de Personagem com os seguintes valores
# Batman
# Superman
# Buzz lightyear
# Homen Formiga
# Bob Esponja
# CatDog

# Criar um enum de StatusEnum com os seguintes valores
# Pendente
# Em Andamento
# Cancelado
# Finalizado

# Criar uma classe chamada Job com os seguintes atributos
# - Personagem enum
# - valor 2301.20
# - local atuação "Blumenau"
# status enum

# Instanciar dois objetos de jobs com personagens e status diferentes
# Apresentar os dados

class PersonagemEnum(Enum):
    BATMAN = "Batman"
    SUPERMAN = "Superman"
    BUZZ_LIGHTYEAR = "Buzz Lightyear"
    HOMEM_FORMIGA = "Homem Formiga"
    BOB_ESPONJA = "Bom Esponja"
    CATDOG = "CatDog"


class StatusEnum(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"


class Job:
    def __init__(self):
        self.personagem: PersonagemEnum
        self.valor: float = None
        self.local_atuacao: str = None
        self.status: StatusEnum


def exercicio_Job():

    jobs = List[Job] = []

    job1 = Job()
    job1.personagem = PersonagemEnum.BATMAN
    job1.valor = 2301.20
    job1.local_atuacao = "Blumenau"
    job1.status = StatusEnum.EM_ANDAMENTO

    job2 = Job()
    job2.personagem = PersonagemEnum.SUPERMAN
    job2.valor = 2301.20
    job2.local_atuacao = "Blumenau"
    job2.status = StatusEnum.FINALIZADO

