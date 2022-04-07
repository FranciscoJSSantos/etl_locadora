from main import ETL
from exclude import Exclude

print("================================")
print("Conexões dos Bancos Realizadas")



while(True):
    print("\n")
    print("================================")
    print("1 - Exclude \n2 - ETL \n3 - Sair")
    teste = input("Escolha a sua operação: ")

    if(teste == '1'):
        exclude = Exclude()
    elif (teste == '2'): 
        etl = ETL()
    else:
        break

