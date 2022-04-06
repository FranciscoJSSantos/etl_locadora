import collections
from doctest import testfile
from itertools import count
import re
import string
from traceback import print_tb
from turtle import home
import turtle
from unittest import result
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import delete
from sqlalchemy import text
import sqlalchemy as sa
from time import perf_counter
import time
from datetime import date, datetime, timedelta
import timeit
from Entities import artista,copias,tempo,dmArtistas,dmGravadora,dmSocio,dmTempo,dmTitulo,ftLocacoes,gravadoras,itensLocacao,locacoes,socios,tipoSocio,titulos


BASE = declarative_base()

def connect_db():
  DIALECT = 'oracle'
  SQL_DRIVER = 'cx_oracle'
  USERNAME = 'locadora' #enter your username
  PASSWORD = 'Oracle18' #enter your password
  HOST = 'oracle-74472-0.cloudclusters.net' #enter the oracle db host url
  PORT = 12498 # enter the oracle port number
  SERVICE = 'XE' # enter the oracle db service name
  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

  engine = sa.create_engine(ENGINE_PATH_WIN_AUTH)
  print("Abrindo Conexao Relacional")
  return engine
  
engine = connect_db()


def connect_db_dimensional():
  DIALECT = 'oracle'
  SQL_DRIVER = 'cx_oracle'
  USERNAME = 'dw_locadora' #enter your username
  PASSWORD = 'Oracle18' #enter your password
  HOST = 'oracle-74472-0.cloudclusters.net' #enter the oracle db host url
  PORT = 12498 # enter the oracle port number
  SERVICE = 'XE' # enter the oracle db service name
  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

  dw_engine = sa.create_engine(ENGINE_PATH_WIN_AUTH)
  print("Abrindo Conexao Dimensional")
  return dw_engine
  
dw_engine = connect_db_dimensional()
metadata = sa.MetaData(bind=None)

##Tabelas relacionais

table_artistas = sa.Table('ARTISTAS', metadata, autoload=True, autoload_with=engine)
table_gravadoras = sa.Table('GRAVADORAS', metadata, autoload=True, autoload_with=engine)
table_copias = sa.Table('COPIAS', metadata, autoload=True, autoload_with=engine)
table_itensLocacoes = sa.Table('ITENS_LOCACOES', metadata, autoload=True, autoload_with=engine)
table_locacoes = sa.Table('LOCACOES', metadata, autoload=True, autoload_with=engine)
table_socios = sa.Table('SOCIOS', metadata, autoload=True, autoload_with=engine)
table_tipoSocios = sa.Table('TIPOS_SOCIOS', metadata, autoload=True, autoload_with=engine)
table_titulos = sa.Table('TITULOS', metadata, autoload=True, autoload_with=engine)

##Tabelas dimensionais

dm_artista = sa.Table('dm_artista', metadata, autoload=True, autoload_with=engine)
dm_gravadora = sa.Table('DM_GRAVADORA', metadata, autoload=True, autoload_with=engine)
dm_socio = sa.Table('DM_SOCIO', metadata, autoload=True, autoload_with=engine)
dm_tempo = sa.Table('DM_TEMPO', metadata, autoload=True, autoload_with=engine)
dm_titulo = sa.Table('DM_TITULO', metadata, autoload=True, autoload_with=engine)
ft_locacoes = sa.Table('FT_LOCACOES', metadata, autoload=True, autoload_with=engine)



###Extraction

def ExtractArtista():
    art1 = []
    count = 0
    print("Iniciando extração de Artista")
    start = timeit.default_timer()

    stmt = sa.select([table_artistas])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        art1.append(artista.Artistas(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        count += 1
    
    # for i in art1:
    #    print(i.cod_art)

    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Artistas")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return art1
        

###TRANSFORM
def TransformarArtistas():
    artisdw = []
    print("Iniciando processa de transformação de Artistas")
    start = timeit.default_timer()
    artista = ExtractArtista()
        
    for i in artista:
       artisdw.append(dmArtistas.DM_artistas(i.cod_art,i.nac_bras,i.nom_art,i.tpo_art))
    
    # for a in artisdw: 
    #     print(a.nom_art)
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação dos artista. "
          f"- Tempo de transformação: {r} segundos")
    
    return artisdw


###LOAD

def CarregarDmArtistas():
    print("Iniciando processa de Carregamento dos Artistas")
    start = timeit.default_timer()
    arts = TransformarArtistas()
        
    for item in arts :
        ins = dm_artista.insert().values(id_art = item.id_art, tpo_art = item.tpo_art, nac_bras = item.nac_bras, nom_art = item.nom_art)
        result = engine.execute(ins)
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento dos Artistas. "
          f"- Tempo de transformação: {r} segundos")



def ETL():
    print("Iniciando rotina ETL")
    start = timeit.default_timer()
    #CarregarDmArtistas()
    #CarregarDmGravadora()
    #CarregarDmSocio()
    #CarregarDmTempo()
    #CarregarDmTitulo()
    CarregarDmArtistas()
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado a rotina ETL. "
          f"- Tempo de transformação: {r} segundos")
    

teste = ETL()