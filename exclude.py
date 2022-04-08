from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, MetaData, Table, asc
import sqlalchemy as sa
from conexao import connect_db

def Exclude():
    engine = connect_db()

    metadata = MetaData(bind=None)

    dm_artista = sa.Table('dm_artista', metadata, autoload=True, autoload_with=engine)
    dm_gravadora = sa.Table('dm_gravadora', metadata, autoload=True, autoload_with=engine)
    dm_socio = sa.Table('dm_socio', metadata, autoload=True, autoload_with=engine)
    dm_tempo = sa.Table('dm_tempo', metadata, autoload=True, autoload_with=engine)
    dm_titulo = sa.Table('dm_titulo', metadata, autoload=True, autoload_with=engine)
    ft_locacoes = sa.Table('ft_locacoes', metadata, autoload=True, autoload_with=engine)
    
    print("Excluindo dados do modelo dimensional")
    
    engine.execute(ft_locacoes.delete()) 
    engine.execute(dm_artista.delete()) 
    engine.execute(dm_gravadora.delete()) 
    engine.execute(dm_socio.delete())
    engine.execute(dm_tempo.delete()) 
    engine.execute(dm_titulo.delete()) 
    
    print("Dados excluídos com sucesso")