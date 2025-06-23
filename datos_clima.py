import pandas as pd
from pathlib import Path
import os



def data(año):
     ruta_datos = Path(r"C:\Users\Cristian\Desktop\Estudio_Clima") / f"export_HVIEJ_HAV_{año}.xlsx"
     df=pd.read_excel(ruta_datos)
     return df

def gen_tabla(año):
     df=data(año)
     tabla_entera=pd.DataFrame(df)
     tabla=tabla_entera.drop(['prcp','snow','wpgt','tsun'],axis=1)
     tabla.columns=['date','temp.prom','temp.min','temp.max','direcc.viento','veloc.viento','presion.atm']
     return tabla

def ext_columna(columna,año):
     tabla=gen_tabla(año)
     columna_ext=tabla[columna].tolist()
     return columna_ext

    
def ciclones(columna,año):
     tabla=gen_tabla(año)
     tabla_2=tabla.drop(['temp.prom','temp.min','temp.max','direcc.viento'],axis=1)
     temporada_ciclonica=tabla_2.iloc[151:334]
     dato_ciclon=temporada_ciclonica[columna].tolist()
     return dato_ciclon

def frentes(columna,n,año):
     df=data(año)
     tabla=gen_tabla(año)
     temporada_invernal_entera=tabla.drop(['temp.prom','temp.max','direcc.viento'],axis=1)
     if n==1:
        temporada_invernal=temporada_invernal_entera.iloc[:151]
     elif n==2:
        temporada_invernal=temporada_invernal_entera.iloc[273:]
     else:
        temporada_invernal=temporada_invernal_entera.iloc[273:]
     dato_invierno=temporada_invernal[columna].tolist()
     return dato_invierno

def rosa(año):
    df=gen_tabla(año)
    df_2=df.drop(['temp.prom','temp.min','temp.max','presion.atm'],axis=1)
    return df_2