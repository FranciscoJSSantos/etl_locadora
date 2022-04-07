from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, MetaData, Table, asc
import sqlalchemy as sa


BASE = declarative_base()


  
def connect_db_dimensional():
  DIALECT = 'oracle'
  SQL_DRIVER = 'cx_oracle'
  USERNAME = 'DW_LOCADORA' #enter your username
  PASSWORD = 'Oracle18' #enter your password
  HOST = 'oracle-74472-0.cloudclusters.net' #enter the oracle db host url
  PORT = 12498 # enter the oracle port number
  SERVICE = 'XE' # enter the oracle db service name
  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

  dw_engine = create_engine(ENGINE_PATH_WIN_AUTH)
  return dw_engine
  
engine = connect_db()
dw_engine = connect_db_dimensional()

#print tabelas conectadas 
# print("\n -- Tabelas do banco relacional -- ") 
# print (engine.table_names())


# print("\n -- Tabelas do banco dimensional -- ") 
# print (dw_engine.table_names())


#SELECT
metadata = MetaData(bind=None)
artistas = Table('DM_ARTISTA', metadata, autoload=True, autoload_with= dw_engine)

#printa coluna da tabela

# print("\n -- Tabelas na coluna 'artistas' --") 
# for columns in artistas.columns: 
#   print(columns.name)


#select simples 
# print("\n -- select simples --") 
# stmt = select([artistas])
# print(stmt)
# print(engine.execute(stmt).fetchall())

# #percorrer os resultados
# results = engine.execute(stmt).fetchall()
# for result in results:
#   print(result)

# print("\n -- SIMPLE SELECT, USING ORDER BY") 
# stmt = select([artistas]).order_by(asc(artistas.columns.cod_art))
# print(stmt)
# print(engine.execute(stmt).fetchall())

# selecione com WHERE 
# print("\n -- SELECIONE COM WHERE --") 
# stmt = select([artistas]).where(artistas.columns.tpo_art == 'D')
# print(stmt)
# print(engine.execute(stmt).fetchall())

# # selecione com JOIN 
# print("\n -- SELECT WITH JOIN --")
# table_socios = sa.Table('socios', metadata, autoload=True, autoload_with=engine)
# table_tipos_socios = sa.Table('tipos_socios', metadata, autoload = True, autoload_with=engine)
# stmt = sa.select([table_socios.columns.cod_tps, table_tipos_socios.columns.cod_tps]).select_from(table_socios.join(table_tipos_socios))
# print(stmt)
# print(engine.execute(stmt).fetchall())

#DELETE TABELA DE FATOS
