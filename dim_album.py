###            LIBRERÍAS                         ###
import pandas as pd
import sqlalchemy

###             Conexion                         ###
def conectar_db_chinook(ruta):
    motorChinook = sqlalchemy.create_engine(ruta)
    conectar = motorChinook.connect()
    return motorChinook, conectar
def conectar_db_dwsalemusic(ruta):    
    motorDwSaleMusic = sqlalchemy.create_engine(ruta)
    conectar = motorDwSaleMusic.connect()
    return motorDwSaleMusic, conectar

###     Extracción de datos de la tabla album    ###
def extraer_df(conectar):
    query = """SELECT Title AS TitleAlbum FROM albums;"""
    result = conectar.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    return df

###                 CARGA DE DATOS            ###
def cargar(datos, connectar, tabla):
    # Procesamiento de completar los valores faltantes
    datos.to_sql(tabla, connectar, if_exists='append', index=False)
    connectar.close()
    fin = print("Carga Terminada!!!")
    return fin

###             EJECUCIÓN           ###
if __name__ == '__main__':
    rutaDB = "sqlite:///chinook.db"
    rutaDW = "sqlite:///DW_Sale_Music.db"

    # Extracción
    extraerDB = conectar_db_chinook(rutaDB)
    engine = extraerDB[0]
    extraer = extraer_df(engine)

    # Carga de los datos
    extraerDW = conectar_db_dwsalemusic(rutaDW)
    datos = extraer
    conectarNuevo = extraerDW[1]
    tabla = "dim_album"
    cargar(datos, conectarNuevo, tabla)
    print(extraer)
