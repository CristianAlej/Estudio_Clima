from datos_clima import *
import estadistica
import numpy as np


estaditicas_basicas=tabla.agg(['mean','median','var','std',estadistic_a.Estadistica.moda_serie])
estaditicas_basicas.index=['promedio','mediana','varianza','desviacion estandar','moda']
estaditicas_basicas.columns=['temp.prom','temp.min','temp.max','direcc.viento','veloc.viento','presion.atm']

#Correlacion de pearson temperatura-presion atmosferica
pearson=estadistica.Estadistica.correlacion_pearson(temperatura_prom,presion_atm)

#Covarianza temperatura-velocidad de viento
covarianza=estadistica.Estadistica.covarianza(temperatura_prom,velocidad_viento)

#Covarianza temperatura-presion atmosferica
covarianza2023=estadistic_a.Estadistica.covarianza(temperatura_prom,presion_atm)

banda=estadistica.Estadistica.bandas_error(tabla)
desv_estandar_prom=banda['cent'].tolist()
desv_estandar_sup=banda['b_sup'].tolist()
desv_estandar_inf=banda['b_inf'].tolist()


def detectar_tormentas():
    fecha = pd.date_range(start=date[151],end=date[333])
    datos={'Fecha' : fecha, 'Veloc.Viento' : velocidad_viento_ciclon,'Presion.Atm' : presion_atm_ciclon}
    df=pd.DataFrame(datos)
    condiciones = [(df['Veloc.Viento'] >= 25) & (df['Veloc.Viento']<63),
        (df['Veloc.Viento'] >= 63) & (df['Veloc.Viento'] < 118),
        (df['Veloc.Viento'] >= 118)]
    categorias = ['Posible Tormenta Cercana','Tormenta Tropical o Banda Ciclonica', 'Ciclón']
    df['Evento'] = np.select(condiciones, categorias, default=None)
    df_eventos = df[df['Evento'].notna()].copy()
    if df_eventos.empty:
        return "No hubo ningun evento meteorologico"
    
    # Agrupar por fecha y evento para encontrar la máxima velocidad
    resultado = df_eventos.groupby(['Fecha', 'Evento'])['Veloc.Viento'].max().reset_index()
    resultado = resultado.rename(columns={'Fecha': 'Fecha','Evento': 'Evento','Veloc.Viento': 'Velocidad Maxima (km/h)'})
    
    # Ordenar por fecha
    resultado = resultado.sort_values('Fecha')
    
    return resultado

eventos_meteorologicos = detectar_tormentas()
print(eventos_meteorologicos)
