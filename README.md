# etl_locadora

- Membro: Francisco José dos Santos Santana

---
## Atividades do Projeto:

- Processo ETL para realizar as ações de Extract, Transform e Load para a tabela dimensional

## Intruções para rodar

- Observações:
  - precisar ter o python instalado na máquina
  - instalar bibliotecas:
    - sqlalchemy
    - cx_Oracle    
    - pandas
    - datetime
  - qualquer dúvida enviar um email para: francisco.jsantana3@gmail.com

- clonar o projeto no seu computador 
- dentro do arquivo 'conexao.py' na função 'connect.db' você deve alterar os dados conforme o seu banco de dados, ex:

```

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
  
```
  
- Depois disso pode entrar no arquivo 'geral.py' e executar
- Nele contém 2 opções: a primeira é para limpar o modelo dimensional e a segunda é para realizar o processo etl
- Pronto, pode olhar a seu banco no modelo dimensional e conferir
