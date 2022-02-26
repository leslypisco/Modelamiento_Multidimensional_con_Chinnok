##################### LIBRERÍAS ################################
import pandas as pd
import sqlalchemy
import calendar
#################### PROCESO ETL ################################


def db(ruta):    
    motorDwSaleMusic = sqlalchemy.create_engine(ruta)
    conectar = motorDwSaleMusic.connect()
    return motorDwSaleMusic, conectar


###      Creacion de datos para la dimension   dim   ###
def create_date_table(start='2009-01-01', end='2030-12-31'):
    df = pd.DataFrame({'date': pd.date_range(start, end)})
    df['Time_id'] = df.index + 1
    df['Year'] = df.date.dt.year
    df['Quarter'] = df.date.dt.quarter
    df['Month'] = df.date.dt.month
    df['Week'] = df.date.dt.isocalendar().week
    df['Day'] = df.date.dt.day
    df['Day_Week'] = df.date.dt.dayofweek
    df['Day_Name'] = df.date.dt.day_name()
    df = df[['Time_id', 'date', 'Year', 'Quarter', 'Month', 
    'Week', 'Day', 'Day_Week', 'Day_Name']] 
    df = pd.DataFrame(df)
    return df


##

################### CARGA DE DATOS  #####################

date_dim = create_date_table()

date_dim.head()

#Mostrar datos en consola
print(date_dim)


#####################3
def cargar(datos, connectar, tabla):
    # Procesamiento de completar los valores faltantes
    datos.to_sql(tabla, connectar, if_exists='append', index=False)
    connectar.close()
    fin = print("Carga Terminada!!!")
    return fin

################# EJECUCIÓN ############################
if __name__ == '__main__':
    #rutaDB = "sqlite:///chinook.db"
    rutaDW = "sqlite:///DW_Sale_Music.db"


    # Carga de los datos
    extraerDW = db(rutaDW)
    #datos = extraer
    conectarNuevo = extraerDW[1]
    tabla = "dim_time"
    cargar(date_dim, conectarNuevo, tabla)
    #print(extraer)
