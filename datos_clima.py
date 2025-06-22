import pandas as pd
from pathlib import Path
import os
 

años=[2023,2024]
print(f"Estan disponibeles las bases de datos de los años: {años} ")
año=str(input("Por favor introduzca el año: ")).strip()
nombre_archivo=f"export_HVIEJ_HAV_{año}.xlsx"
ruta_datos = Path(r"C:\Users\Cristian\Desktop\Estudio_Clima") / f"export_HVIEJ_HAV_{año}.xlsx"
df=pd.read_excel(ruta_datos)

#Datos clima
    #Temperatura:
        #Temperatura promedio:
temperatura_prom=df['tavg'].tolist()
        #Temperatura maxima:
temperatura_max=df['tmax'].tolist()
        #Temperatura minima:
temperatura_min=df['tmin'].tolist()
    #Condiciones del viento:
        #Direccion:
direccion_viento=df['wdir'].tolist()
        #Velocidad:
velocidad_viento=df['wspd'].tolist()
    #Presion atmosferica:
presion_atm=df['pres'].tolist()
 
#Fecha
date=df['date'].tolist()
 
#Tabla para estudio estadistico 
tabla_entera=pd.DataFrame(df)
tabla=tabla_entera.drop(['date','prcp','snow','wpgt','tsun'],axis=1)
tabla.columns=['temp.prom','temp.min','temp.max','direcc.viento','veloc.viento','presion.atm']

#Temporada ciclonica en Cuba
temporada_ciclonica_entera=tabla.drop(['temp.prom','temp.min','temp.max','direcc.viento'],axis=1)
temporada_ciclonica=temporada_ciclonica_entera.iloc[151:334]
velocidad_viento_ciclon=temporada_ciclonica['veloc.viento'].tolist()
presion_atm_ciclon=temporada_ciclonica['presion.atm'].tolist()

#Primera y segunda temporada invernal en cuba
temporada_invernal_entera=tabla.drop(['temp.prom','temp.max','direcc.viento'],axis=1)
temporada_invernal_1=temporada_invernal_entera.iloc[:151]
temporada_invernal_2=temporada_invernal_entera.iloc[273:]
temperatura_min_invierno_1=temporada_invernal_1['temp.min'].tolist()
temperatura_min_invierno_2=temporada_invernal_2['temp.min'].tolist()
velocidad_viento_invierno_1=temporada_invernal_1['veloc.viento'].tolist()
velocidad_viento_invierno_2=temporada_invernal_2['veloc.viento'].tolist()
presion_atm_invierno_1=temporada_invernal_1['presion.atm'].tolist()
presion_atm_invierno_2=temporada_invernal_2['presion.atm'].tolist()

