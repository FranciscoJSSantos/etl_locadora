from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, MetaData, Table, asc
import sqlalchemy as sa

def connect_db():
  DIALECT = 'oracle'
  SQL_DRIVER = 'cx_oracle'
  USERNAME = 'locadora' #enter your username
  PASSWORD = 'Oracle18' #enter your password
  HOST = 'oracle-74472-0.cloudclusters.net' #enter the oracle db host url
  PORT = 12498 # enter the oracle port number
  SERVICE = 'XE' # enter the oracle db service name
  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

  engine = create_engine(ENGINE_PATH_WIN_AUTH)
  return engine
