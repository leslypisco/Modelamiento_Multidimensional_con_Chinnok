import pandas as pd
import sqlalchemy

#################### PROCESO ETL ################################

def conectar_db_chinook(path):
    motorChinook = sqlalchemy.create_engine(path)
    conectar = motorChinook.connect()
    return motorChinook, conectar

def conectar_db_dwsalemusic(path):    
    motorDwSaleMusic = sqlalchemy.create_engine(path)
    conectar = motorDwSaleMusic.connect()
    return motorDwSaleMusic, conectar

###     Extracción de datos de la tabla customers    ###
def extraer_df(conectar):
    query = """SELECT FirstName,LastName,Phone,Fax,Email 
                FROM customers;"""
    result = conectar.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    return df

################### TRANFORMACIÓN DE DATOS NULOS #####################
def transformar_nulls(datos):    
    # Procesamiento de completar los valores faltantes
    datos = datos.fillna({"FirstName": "NA","LastName": "NA","Phone":"NA","Fax":"NA","Email":"NA"})
    return datos

################### CARGA DE DATOS  #####################
def cargar(datos, connectar, tabla):
    # Procesamiento de completar los valores faltantes
    datos.to_sql(tabla, connectar, if_exists='append', index=False)
    connectar.close()
    fin = print("Carga Terminada!!!")
    return fin

################# EJECUCIÓN ############################
if __name__ == '__main__':
    rutaDB = "sqlite:///chinook.db"
    rutaDW = "sqlite:///DW_Sale_Music.db"

    # Extracción
    extraerDB = conectar_db_chinook(rutaDB)
    engine = extraerDB[0]
    extraer = extraer_df(engine)
    
    # Transformación
    transformar = transformar_nulls(extraer)

    # carga de los datos
    extraerDW = conectar_db_dwsalemusic(rutaDW)
    datos = transformar
    conectarNuevo = extraerDW[1]
    tabla = "dim_customer"
    cargar(datos, conectarNuevo, tabla)
    print(extraer)