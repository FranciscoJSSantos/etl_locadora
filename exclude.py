from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, MetaData, Table, asc
import sqlalchemy as sa
from teste import connect_db_dimensional

def Exclude():
    dw_engine = connect_db_dimensional()

    metadata = MetaData(bind=None)

    dm_artista = sa.Table('dm_artista', metadata, autoload=True, autoload_with=dw_engine)
    dm_gravadora = sa.Table('dm_gravadora', metadata, autoload=True, autoload_with=dw_engine)
    dm_socio = sa.Table('dm_socio', metadata, autoload=True, autoload_with=dw_engine)
    dm_tempo = sa.Table('dm_tempo', metadata, autoload=True, autoload_with=dw_engine)
    dm_titulo = sa.Table('dm_titulo', metadata, autoload=True, autoload_with=dw_engine)
    ft_locacoes = sa.Table('ft_locacoes', metadata, autoload=True, autoload_with=dw_engine)

    dw_engine.execute(ft_locacoes.delete()) 
    dw_engine.execute(dm_artista.delete()) 
    dw_engine.execute(dm_gravadora.delete()) 
    dw_engine.execute(dm_socio.delete())
    dw_engine.execute(dm_tempo.delete()) 
    dw_engine.execute(dm_titulo.delete()) 
 