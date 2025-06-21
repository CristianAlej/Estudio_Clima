import seaborn as sns
import matplotlib.pyplot as plt
from datos_clima import *
from analisis_datos import *
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


def grafico_temperatura(date, temp_promedio, temp_max, temp_min, std_promedio, std_max, std_min):
    sns.set(style="darkgrid")
    plt.figure(figsize=(12, 7)) 
    df = pd.DataFrame({
        'Fecha': date,
        'Temp_Promedio': temp_promedio,
        'Temp_Max': temp_max,
        'Temp_Min': temp_min,
        'Std_Promedio': std_promedio,
        'Std_Max': std_max,
        'Std_Min': std_min
    })
    df.set_index('Fecha', inplace=True)
    
    sns.lineplot(data=df, x=df.index, y='Temp_Promedio', color='green', label='Temperatura Promedio')
    plt.fill_between(df.index, 
                     df['Temp_Promedio'] - df['Std_Promedio'], 
                     df['Temp_Promedio'] + df['Std_Promedio'], 
                     color='green', alpha=0.2)
    
    sns.lineplot(data=df, x=df.index, y='Temp_Max', color='red', label='Temperatura Máxima')
    plt.fill_between(df.index, 
                     df['Temp_Max'] - df['Std_Max'], 
                     df['Temp_Max'] + df['Std_Max'], 
                     color='red', alpha=0.2)
    
    sns.lineplot(data=df, x=df.index, y='Temp_Min', color='blue', label='Temperatura Mínima')
    plt.fill_between(df.index, 
                    df['Temp_Min'] - df['Std_Min'], 
                    df['Temp_Min'] + df['Std_Min'], 
                    color='blue', alpha=0.2)
    
    plt.title('Serie Temporal de Temperaturas con Bandas de Error', fontsize=16)
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    plt.legend(title='Leyenda', title_fontsize=12)
    plt.xticks(range(0, len(date), 30), rotation=45)
    plt.tight_layout()
    plt.show()


grafico_temperatura(date, temperatura_prom, temperatura_max,temperatura_min,
                     desv_estandar_prom, desv_estandar_sup, desv_estandar_inf)


def rosa_polar(direccion,velocidad):
    fig = go.Figure(go.Barpolar(r=velocidad,theta=direccion,marker_color=velocidad,marker_line_color="black",
                                marker_line_width=1,opacity=0.8,name="Velocidad del viento (km/h)"))

    fig.update_layout(
        title='Rosa de los Vientos Interactiva',
        polar=dict(radialaxis=dict(visible=True),angularaxis=dict(direction="clockwise")),showlegend=True)

    fig.show()

rosa_polar(direccion_viento,velocidad_viento)
def direccion(direccion):
    sns.set_theme()
    df = pd.DataFrame({'direccion': direccion, 'r':direccion})
    df = pd.melt(df, id_vars=['direccion'], value_name='theta')
    g = sns.FacetGrid(df,
                  subplot_kws=dict(projection='polar'), height=4.5,
                  sharex=False, sharey=False, despine=False)
    g.map(sns.scatterplot,"theta","direccion")
    plt.show()  

direccion(direccion_viento)

def velocidad(date,velocidad):
    dates = pd.date_range(start=date[0], end=date[-1], freq='D')
    df = pd.DataFrame({'Fecha': dates, 'Velocidad_viento': velocidad})
    fig = px.line(df, x='Fecha', y='Velocidad_viento', title='Velocidad del Viento durante un Año',
              labels={'Velocidad_viento': 'Velocidad (km/h)', 'Fecha': 'Fecha'},template='plotly_dark')
    fig.update_traces(line_color='#1f77b4', line_width=2)
    fig.update_layout(hovermode='x unified', 
                  xaxis_title='Fecha',
                  yaxis_title='Velocidad del Viento (km/h)',
                  xaxis_rangeslider_visible=True)
    fig.show()

velocidad(date,velocidad_viento)

def presion_temperatura():
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=date[0],end=date[-1] , freq="D")
    def adaptacion(temperatura_prom):
        temperatura_adaptada=[]
        for i in temperatura_prom:
            j=float(i)+994.6
            temperatura_adaptada.append(j)
        return temperatura_adaptada
    datos = {"Fecha": fechas,"Presión Atmosférica (hPa)": presion_atm,"Temperatura (°C)": adaptacion(temperatura_prom)}
    df = pd.DataFrame(datos)
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df,x="Fecha",y="Presión Atmosférica (hPa)",color="blue",label="Presión Atmosférica",linewidth=2)
    sns.lineplot(data=df,x="Fecha",y="Temperatura (°C)",color="red",label="Temperatura",linewidth=2)
    plt.title("Variación de Presión Atmosférica y Temperatura", fontsize=16, pad=20)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Valores", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Variables", loc="upper left")
    plt.tight_layout()
    plt.show()

presion_temperatura()

def presion_viento():
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=date[0],end=date[-1] , freq="D")
    def adaptacion(velocidad_viento):
        velocidad_viento_adaptada=[]
        for i in velocidad_viento:
            j=float(i)+1014.6
            velocidad_viento_adaptada.append(j)
        return velocidad_viento_adaptada
    datos = {"Fecha": fechas,"Presión Atmosférica (hPa)": presion_atm,"Velocidad (km/h)": adaptacion(velocidad_viento)}
    df = pd.DataFrame(datos)
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df,x="Fecha",y="Presión Atmosférica (hPa)",color="blue",label="Presión Atmosférica",linewidth=2)
    sns.lineplot(data=df,x="Fecha",y="Velocidad (km/h)",color="red",label="Velocidad viento",linewidth=2)
    plt.title("Variación de Presión Atmosférica y Velocidad del viento", fontsize=16, pad=20)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Valores", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Variables", loc="upper left")
    plt.tight_layout()
    plt.show()

presion_viento()


def comp_temporada_ciclonica():
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=date[151],end=date[333] , freq="D")
    def adaptacion(velocidad_viento_ciclon):
        velocidad_viento_adaptada=[]
        for i in velocidad_viento_ciclon:
            j=float(i)+994.6
            velocidad_viento_adaptada.append(j)
        return velocidad_viento_adaptada
    datos = {"Fecha": fechas,"Presión Atmosférica (hPa)": presion_atm_ciclon,
             "Velocidad (km/h)": adaptacion(velocidad_viento_ciclon)}
    df = pd.DataFrame(datos)
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df,x="Fecha",y="Presión Atmosférica (hPa)",color="blue",label="Presión Atmosférica",linewidth=2)
    sns.lineplot(data=df,x="Fecha",y="Velocidad (km/h)",color="red",label="Velocidad viento",linewidth=2)
    plt.title("Temporada Ciclonica", fontsize=16, pad=20)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Valores", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Variables", loc="upper left")
    plt.tight_layout()
    plt.show()

comp_temporada_ciclonica()

def comp_temporada_invernal(n):
    sns.set(style="whitegrid")
    if n ==1:
        num="Inicio de Año"
        fechas = pd.date_range(start=date[0],end=date[150] , freq="D")
        presion_atm_invierno=presion_atm_invierno_1
        velocidad_viento_invierno=velocidad_viento_invierno_1
        temperatura_min_invierno=temperatura_min_invierno_1
    elif n==2:
        num="Final de Año"
        fechas = pd.date_range(start=date[273],end=date[-1] , freq="D")
        presion_atm_invierno=presion_atm_invierno_2
        velocidad_viento_invierno=velocidad_viento_invierno_2
        temperatura_min_invierno=temperatura_min_invierno_2
    else: 
        print("Error los valores son 1 o 2")
        return False
    def adaptacion(datos):
        datos_adaptados=[]
        for i in datos:
            j=float(i)+998
            datos_adaptados.append(j)
        return datos_adaptados
    datos = {"Fecha": fechas,"Presión Atmosférica (hPa)": presion_atm_invierno,
             "Velocidad (km/h)": adaptacion(velocidad_viento_invierno), 
             "Temperatura": adaptacion(temperatura_min_invierno)}
    df = pd.DataFrame(datos)
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df,x="Fecha",y="Presión Atmosférica (hPa)",color="green",label="Presión Atmosférica",linewidth=2)
    sns.lineplot(data=df,x="Fecha",y="Velocidad (km/h)",color="red",label="Velocidad viento",linewidth=2)
    sns.lineplot(data=df,x="Fecha",y="Temperatura",color="blue",label="Temperatura Minima",linewidth=2)
    plt.title(f"Temporada Invernal {num}", fontsize=16, pad=20)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Valores", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Variables", loc="upper left")
    plt.tight_layout()
    plt.show()

comp_temporada_invernal(1)
comp_temporada_invernal(2)
  

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


eventos = detectar_tormentas()
print(eventos)