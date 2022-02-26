##################### LIBRERÍAS ################################
import pandas as pd
import sqlalchemy

#################### PROCESO ETL ################################
def conectar_db_chinook(ruta):
    motorChinook = sqlalchemy.create_engine(ruta)
    conectar = motorChinook.connect()
    return motorChinook, conectar

def conectar_db_dwsalemusic(ruta):    
    motorDwSaleMusic = sqlalchemy.create_engine(ruta)
    conectar = motorDwSaleMusic.connect()
    return motorDwSaleMusic, conectar

###     Extructura de la tabla de hechos            ###
def extraer_df(conectar):
    query = """SELECT   invoices.InvoiceId as InvoiceId,
                        customers.CustomerId,
                        dim_time.Time_id as TimeId,
                        invoices.InvoiceId AS LocationId,
                        tracks.TrackId,
                        artists.ArtistId,
                        albums.AlbumId,
                        invoices.Total
                FROM invoices INNER JOIN customers
                ON invoices.CustomerId= customers.CustomerId
                INNER JOIN invoice_items
                ON invoice_items.InvoiceId= invoices.InvoiceId
                INNER JOIN tracks
                ON tracks.TrackId=  invoice_items.TrackId
                INNER JOIN albums
                ON tracks.AlbumId= albums.AlbumId
                INNER JOIN artists 
                ON albums.ArtistId= artists.ArtistId 
                INNER JOIN dim_time
                ON invoices.InvoiceDate= substr(dim_time.date,0,20);"""
    result = conectar.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    return df

###           CARGA DE DATOS      ###
def cargar(datos, connectar, tabla):
    # Procesamiento de completar los valores faltantes
    datos.to_sql(tabla, connectar, 
    if_exists='append', index=False)
    connectar.close()
    fin = print("Carga Terminada!!!")
    return fin

###              EJECUCIÓN          ###
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
    tabla = "Fact_sales"
    cargar(datos, conectarNuevo, tabla)
    print(extraer)
    

