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
from conexao import connect_db

BASE = declarative_base()
 
engine = connect_db()
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

def ExtrairArtista():
    art1 = []
    count = 0
    print("Iniciando extração de Artista")
    start = timeit.default_timer()

    stmt = sa.select([table_artistas])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        art1.append(artista.Artistas(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Artistas")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return art1

def ExtrairCopias():
    cop1 = []
    count = 0
    print("Iniciando extração de Copias")
    start = timeit.default_timer()

    stmt = sa.select([table_copias])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        cop1.append(copias.Copias(row[0],row[1],row[2],row[3]))
        count += 1
        
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extracao das Copias")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execucao: {r} segundos")
    
    return cop1


def ExtrairGravadoras():
    grav1 = []
    count = 0
    print("Iniciando extracao de Gravadoras")
    start = timeit.default_timer()

    stmt = sa.select([table_gravadoras])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        grav1.append(gravadoras.Gravadoras(row[0],row[1],row[2],row[3]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extracao das Gravadoras")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execucao: {r} segundos")
    
    return grav1

def ExtrairItensLocacoes():
    il1 = []
    count = 0
    print("Iniciando extracao de Itens locacoes")
    start = timeit.default_timer()

    stmt = sa.select([table_itensLocacoes])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        il1.append(itensLocacao.ItensLocacoes(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extracao dos Itens Locações")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execucao: {r} segundos")
    
    return il1

def ExtrairLocacoes():
    l1 = []
    count = 0
    print("Iniciando extração de Locacoes")
    start = timeit.default_timer()

    stmt = sa.select([table_locacoes])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        l1.append(locacoes.Locacoes(row[0],row[1],row[2],row[3],row[4],row[5]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Locações")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return l1

def ExtrairSocios():
    s1 = []
    count = 0
    print("Iniciando extração de Socios")
    start = timeit.default_timer()

    stmt = sa.select([table_socios])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        s1.append(socios.Socios(row[0],row[1],row[2],row[3],row[4]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Socios")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return s1

def ExtrairTipoSocios():
    ts1 = []
    count = 0
    print("Iniciando extração de Tipo Socios")
    start = timeit.default_timer()

    stmt = sa.select([table_tipoSocios])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        ts1.append(tipoSocio.TipoSocios(row[0],row[1],row[2],row[3]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Tipo de Socios")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return ts1

def ExtrairTitulos():
    t1 = []
    count = 0
    print("Iniciando extração de Titulos")
    start = timeit.default_timer()

    stmt = sa.select([table_titulos])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        t1.append(titulos.Titulos(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Títulos")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return t1

def ExtrairTempo():
    temp1 = []
    count = 0
    print("Iniciando extração do Tempo")
    start = timeit.default_timer()

    stmt = sa.select([table_locacoes])
    result = engine.execute(stmt).fetchall()
            
    for row in result:
        temp1.append(tempo.Tempo(row[1]))
        count += 1
    
    end = timeit.default_timer()
    r = (end - start)
    print("Fim da extrção dos Tipo de Socios")
    print(f'Total de itens exraidos: {count}')
    print(f"Tempo total da execução: {r} segundos")
    
    return temp1 

###TRANSFORM
def TransformarArtistas():
    artisdw = []
    print("Iniciando processa de transformação de Artistas")
    start = timeit.default_timer()
    artista = ExtrairArtista()
        
    for i in artista:
       artisdw.append(dmArtistas.DM_artistas(i.cod_art,i.nac_bras,i.nom_art,i.tpo_art))
      
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação dos artista. "
          f"- Tempo de transformação: {r} segundos")
    
    return artisdw

def TransformarGravadoras():
    gravdw = []
    print("Iniciando processa de transformação de Gravadoras")
    start = timeit.default_timer()
    gravadora = ExtrairGravadoras()
        
    for i in gravadora:
       gravdw.append(dmGravadora.DM_gravadora(i.cod_grav,i.uf_grav,i.nac_bras,i.nom_grav))
       
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação dos artista. "
          f"- Tempo de transformação: {r} segundos") 
    
    return gravdw   
    
def TransformarSocio():
    socdw = []
    print("Iniciando processa de transformação de Socios")
    start = timeit.default_timer()
    gravadora = ExtrairSocios()
        
    for i in gravadora:
       socdw.append(dmSocio.DM_socio(i.cod_soc,i.nom_soc,i.cod_tps))
     
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação dos Socios. "
          f"- Tempo de transformação: {r} segundos")
    
    return socdw

def TransformarTempo():
    count = 0
    tempdw = []
    print("Iniciando processa de transformação do Tempo")
    start = timeit.default_timer()
    temp = ExtrairTempo()
        
    for i in temp:
       count+=1
       tempdw.append(dmTempo.DM_tempo(count,i.tempoLoc.strftime("%Y"),i.tempoLoc.strftime("%m"),i.tempoLoc.strftime("%Y")+i.tempoLoc.strftime("%m"),NomMes(i.tempoLoc.strftime("%m"))[0:3],NomMes(i.tempoLoc.strftime("%m"))[0:3]+"/"+i.tempoLoc.strftime("%Y"),NomMes(i.tempoLoc.strftime("%m")),i.tempoLoc.strftime("%d"),i.tempoLoc,i.tempoLoc.strftime("%H"),Turn(i.tempoLoc.strftime("%H"))))

    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação do tempo. "
          f"- Tempo de transformação: {r} segundos")
    
    return tempdw

def Turn(hora):
    turno = "Teste"
    h = int(hora)
    if(h < 12):
        turno = "MANHA"
    elif(h > 12 and h <= 18):
        turno = "TARDE"
    elif(h > 18):
        turno = "NOITE"
    return turno

def NomMes(num):
    nome = "Teste"
    if(num == "01"):
        nome = "Janeiro"
    elif(num == "02"):
        nome = "Fevereiro"
    elif(num == "03"):
        nome = "Março"
    elif(num == "04"):
        nome = "Abril"
    elif(num == "05"):
        nome = "Maio"
    elif(num == "06"):
        nome = "Junho"
    elif(num == "07"):
        nome = "Julho"
    elif(num == "08"):
        nome = "Agosto"
    elif(num == "09"):
        nome = "Setemebro"
    elif(num == "10"):
        nome = "Outubro"
    elif(num == "11"):
        nome = "Novembro"
    elif(num == "12"):
        nome = "Dezembro"
    
    return nome

def TransformarTitulo():
    titdw = []
    print("Iniciando processa de transformação dos Titulos")
    start = timeit.default_timer()
    tit = ExtrairTitulos()
        
    for i in tit:
       titdw.append(dmTitulo.DM_titulo(i.cod_tit,i.tpo_tit,i.cla_tit,i.dsc_tit))
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação dos Titulos. "
          f"- Tempo de transformação: {r} segundos")

    return titdw

def TransformarFMLocacoes():
    locFT = []
    count = 0
    sum = 0
    
    print("Iniciando processa de transformação das Locações")
    start = timeit.default_timer()
    locs = ExtrairLocacoes()
    itLocs = ExtrairItensLocacoes()
        
    while(count != 300):
        for locacao in locs:
            sum += locacao.val_loc
            for item in itLocs:
                count+=1
                locFT.append(ftLocacoes.FT_locacoes(locacao.cod_soc,item.cod_tit,IdArt(item.cod_tit),IdGrav(item.cod_tit),count,sum,0 if locacao.sta_pgto == "P" else (CalDt(locacao)),0.0 if locacao.sta_pgto == "P" else (CalcularMul(locacao))))
                print("Item adicionado")
                print(count)

    for a in locFT: 
        print(a.id_art)
 
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de transformação das Locações. "
          f"- Tempo de transformação: {r} segundos")
    
    return locFT

def CalDt(locacao):
    tempoAtraso = date.today()-locacao.dat_venc.strftime("%Y", "%m", "%d")
    return tempoAtraso
    

def IdArt(id):
    tit = ExtrairTitulos()
    for i in tit:
        if(id == i.cod_art):
            id = i.cod_art
            
            return id
        
def IdGrav(id):
    tit = ExtrairTitulos()
    for i in tit:
        if(id == i.cod_grav):
            id = i.cod_grav
            
            return id

def CalcularMul(locacao):
    multa = 0
    tempoAtraso = date.today()-locacao.dat_venc.strftime("%Y","%m","%d")
    if(tempoAtraso > 1):
        tempoAtraso -= 1
        multa += tempoAtraso * 0.4
        print(multa)
    return multa
  
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


def CarregarDmGravadora():
    print("Iniciando processa de Carregamento das Gravadoras")
    start = timeit.default_timer()
    gravs = TransformarGravadoras()
        
    for item in gravs :
        ins = dm_gravadora.insert().values(id_grav = item.id_grav, uf_grav = item.uf_grav, nac_bras = item.nac_bras, nom_grav = item.nom_grav)
        result = engine.execute(ins)
        

        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento das Gravadoras. "
          f"- Tempo de transformação: {r} segundos")

def CarregarDmSocio():
    print("Iniciando processa de Carregamento dos Socios")
    start = timeit.default_timer()
    soc = TransformarSocio()
        
    for item in soc :
        ins = dm_socio.insert().values(id_soc = item.id_soc, nom_soc = item.nom_soc, tipo_socio = item.tipo_socio)
        result = engine.execute(ins)
        

        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento das Gravadoras. "
          f"- Tempo de transformação: {r} segundos")

def CarregarDmTempo():
    print("Iniciando processa de Carregamento do Tempo")
    start = timeit.default_timer()
    temp = TransformarTempo()
        
    for item in temp :
        ins = dm_tempo.insert().values(id_tempo = item.id_tempo,nu_ano = item.nu_ano,nu_mes = item.nu_mes,nu_anomes = item.nu_anomes,sg_mes = item.sg_mes,nm_mesano = item.nm_mesano,nm_mes = item.nm_mes,nu_dia = item.nu_dia,dt_tempo = item.dt_tempo,nu_hora = item.nu_hora,turno = item.turno)
        result = engine.execute(ins)
        
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento dos Tempos. "
          f"- Tempo de transformação: {r} segundos")
    
def CarregarDmTitulo():
    print("Iniciando processa de Carregamento dos Títulos")
    start = timeit.default_timer()
    tit = TransformarTitulo()
        
    for item in tit :
        ins = dm_titulo.insert().values(id_titulo = item.id_titulo,tpo_titulo = item.tpo_titulo,cla_titulo = item.cla_titulo, dsc_titulo = item.dsc_titulo)
        result = engine.execute(ins)
        
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento dos Títulos. "
          f"- Tempo de transformação: {r} segundos")
    
    
def CarregarFTlocacoes():
    print("Iniciando processa de Carregamento das Locações na tabela de fatos")
    start = timeit.default_timer()
    locF = TransformarFMLocacoes()
        
    for item in locF :
        ins = ft_locacoes.insert().values(id_socio = item.id_socio,id_titulo = item.id_titulo,id_art = item.id_art,id_grav = item.id_grav,id_tempo = item.id_tempo,valor_arrecadado = item.valor_arrecadado,tempo_devolucao = item.tempo_devolucao,multa_atraso = item.multa_atraso)
        result = engine.execute(ins)
        
        
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado processo de Carregamento dos Títulos. "
          f"- Tempo de transformação: {r} segundos")


def ETL():
    print("Iniciando rotina ETL")
    start = timeit.default_timer()
    
    CarregarDmArtistas()
    CarregarDmGravadora()
    CarregarDmSocio()
    CarregarDmTempo()
    CarregarDmTitulo()
    CarregarFTlocacoes()
    
    end = timeit.default_timer()
    r = (end - start)
    print("Finalizado a rotina ETL. "
          f"- Tempo total: {r} segundos")
