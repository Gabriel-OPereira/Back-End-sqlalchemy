# %%
# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from classes import (
    UNIDADE_PRODUCAO,
    REGISTRO_FALHA,
    PECA,
    SOPRADORA,
    FRESADORA,
    TORNO_CNC,
    IMPRESSORA_3D,
)
import os
from dotenv import load_dotenv

load_dotenv()

# %%
# Criar uma conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

engine = create_engine(f"mssql+pymssql://{usuario}:{senha}@{host}/{banco_de_dados}")
# %%
# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# %%
# Inserir registros de departamentos
Unidade01 = UNIDADE_PRODUCAO(
    numero = 1,
    peca_hora_nominal = 23
)
session.add(Unidade01)
session.commit()

Unidade02 = UNIDADE_PRODUCAO(
    numero = 2,
    peca_hora_nominal = 24
)
session.add(Unidade02)
session.commit()

Registro01 = REGISTRO_FALHA(
    id = 1,
    severidade = True,
    inicio = date(2024,4,1),
    fim = date(2024,4,2),
    numero_unidade_producao = 1
)
session.add(Registro01)
session.commit()

Registro02 = REGISTRO_FALHA(
    id = 2,
    severidade = False,
    inicio = date(2024,4,1),
    fim = date(2024,4,2),
    numero_unidade_producao = 2
)
session.add(Registro02)
session.commit()

Peca01 = PECA(
    numero = 1,
    status = 'Aprovada',
    inicio_fabricacao = date(2024,4,1),
    fim_fabricacao = date(2024,4,2),
    numero_unidade_producao = 1 
)
session.add(Peca01)
session.commit()

Peca02 = PECA(
    numero = 2,
    status = 'Reprovada',
    inicio_fabricacao = date(2024,4,1),
    fim_fabricacao = date(2024,4,2),
    numero_unidade_producao = 2 
)
session.add(Peca02)
session.commit()

Sopradora01 = SOPRADORA(
    numero = 1,
    vazao_sopro = 2.0,
    pressao_sopro = 1.5

)

session.add(Sopradora01)
session.commit()

Sopradora02 = SOPRADORA(
    numero = 2,
    vazao_sopro = 3.0,
    pressao_sopro = 1.5

)

session.add(Sopradora02)
session.commit()


Torno01 = TORNO_CNC(
    numero = 1,
    velocidade_rotacao = 2.1,
    tolerancia = 2.3

)

session.add(Torno01)
session.commit()

Torno02 = TORNO_CNC(
    numero = 2,
    velocidade_rotacao = 2.3,
    tolerancia = 2.5

)

session.add(Torno02)
session.commit()

Impressora01 = IMPRESSORA_3D(
    numero = 1,
    espessura_camada = 0.3 ,
    tipo_material = 'Pla Premium'

)

session.add(Impressora01)
session.commit()

Impressora02 = IMPRESSORA_3D(
    numero = 2,
    espessura_camada = 0.3 ,
    tipo_material = 'Pla Ultra Premium'

)

session.add(Impressora02)
session.commit()

Fresadora01 = FRESADORA(
    numero = 1,
    velocidade_rotacao = 1.0,
    profundidade_corte = 1.2
)

session.add(Fresadora01)
session.commit()

Fresadora02 = FRESADORA(
    numero = 2,
    velocidade_rotacao = 1.2,
    profundidade_corte = 1.4
)

session.add(Fresadora02)
session.commit()
