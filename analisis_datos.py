from datos_clima import *
import estadistica
import numpy as np

def gen_estadisticas_basicas(año):
    tabla_entera=gen_tabla(año)
    tabla=tabla_entera.drop(['date'],axis=1)
    estaditicas_basicas=tabla.agg(['mean','median','var','std',estadistica.Estadistica.moda_serie])
    estaditicas_basicas.index=['promedio','mediana','varianza','desviacion estandar','moda']
    estaditicas_basicas.columns=['temp.prom','temp.min','temp.max','direcc.viento','veloc.viento','presion.atm']
    return estaditicas_basicas

def pearson(columna_1,columna_2,año):
    pearson=estadistica.Estadistica.correlacion_pearson(ext_columna(columna_1,año),ext_columna(columna_2,año))
    return pearson

def cov(columna_1,columna_2,año):
    covarianza=estadistica.Estadistica.covarianza(ext_columna(columna_1,año),ext_columna(columna_2,año))
    return covarianza

def gen_banda(columna,año):
    tabla=gen_tabla
    banda=estadistica.Estadistica.bandas_error(tabla,año)
    desv_estandar=banda[columna].tolist()
    return desv_estandar

def detectar_tormentas(año):
    fecha = pd.date_range(start=ext_columna('date',año)[151],end=ext_columna('date',año)[333])
    datos={'Fecha' : fecha, 'Veloc.Viento' : ciclones('veloc.viento',año),'Presion.Atm' : ciclones('presion.atm',año)}
    df=pd.DataFrame(datos)
    condiciones = [(df['Veloc.Viento'] >= 25) & (df['Veloc.Viento']<63),
        (df['Veloc.Viento'] >= 63) & (df['Veloc.Viento'] < 118),
        (df['Veloc.Viento'] >= 118)]
    categorias = ['Posible Tormenta Cercana','Tormenta Tropical o Banda Ciclonica', 'Ciclón']
    df['Evento'] = np.select(condiciones, categorias, default=None)
    df_eventos = df[df['Evento'].notna()].copy()
    if df_eventos.empty:
        return "No hubo ningun evento meteorologico"
    resultado = df_eventos.groupby(['Fecha', 'Evento'])['Veloc.Viento'].max().reset_index()
    resultado = resultado.rename(columns={'Fecha': 'Fecha','Evento': 'Evento','Veloc.Viento': 'Velocidad Maxima (km/h)'})
    resultado = resultado.sort_values('Fecha')
    
    return resultado

def detectar_frentes_frios(n,año):
    if n ==1:
        num="Inicio de Año"
        fechas = pd.date_range(ext_columna('date',año)[0],end=ext_columna('date',año)[150])
        velocidad_viento_invierno=frentes('veloc.viento',1,año)
        temperatura_min_invierno=frentes('temp.min',1,año)
    elif n==2:
        num="Final de Año"
        fechas = pd.date_range(start=ext_columna('date',año)[273],end=ext_columna('date',año)[-1])
        velocidad_viento_invierno=frentes('veloc.viento',2,año)
        temperatura_min_invierno=frentes('temp.min',2,año)
       
    datos={'Fecha' : fechas, 'Veloc.Viento' : velocidad_viento_invierno,'Temperatura' : temperatura_min_invierno}
    df=pd.DataFrame(datos)
    condiciones = [(df['Veloc.Viento'] >= 15) & (df['Veloc.Viento']<40) & (df['Temperatura']<18)]
    categorias = ['Posible Frente Frio']
    df['Evento'] = np.select(condiciones, categorias, default=None)
    df_eventos = df[df['Evento'].notna()].copy()
    if df_eventos.empty:
        return "No hubo ningun frente frio"
    resultado = df_eventos.groupby(['Fecha', 'Evento'])['Temperatura'].min().reset_index()
    resultado = resultado.rename(columns={'Fecha': 'Fecha','Evento': 'Evento','Temperatura': 'Temperatura minima °C'})
    resultado = resultado.sort_values('Fecha')
    
    return resultado

def bandas_error(n,año):
    df=gen_tabla(año)
    if n==1:
        resultados = df['temp.max'] - df['temp.prom']
    elif n==2:
        resultados = df['temp.prom'] - df['temp.min']
    else:
        resultados = df['temp.max']-df['temp.min']

    return resultados
