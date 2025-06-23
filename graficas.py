import seaborn as sns
import matplotlib.pyplot as plt
from datos_clima import *
from analisis_datos import *
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def grafico_temperatura(año):
    sns.set(style="darkgrid")
    fig, ax = plt.subplots(figsize=(12, 7))
    
    date = pd.date_range(start=ext_columna('date', año)[0], 
                         end=ext_columna('date', año)[-1], 
                         freq="D")
    df = pd.DataFrame({
        'Fecha': date,
        'Temp_Promedio': ext_columna('temp.prom', año),
        'Temp_Max': ext_columna('temp.max', año),
        'Temp_Min': ext_columna('temp.min', año),
        'Std_Promedio': bandas_error(3, año),
        'Std_Max': bandas_error(1, año),
        'Std_Min': bandas_error(2, año)
    })
    df.set_index('Fecha', inplace=True)
    sns.lineplot(data=df, x=df.index, y='Temp_Promedio', color='green', 
                 label='Temperatura Promedio', ax=ax)
    ax.fill_between(df.index, 
                    df['Temp_Promedio'] - df['Std_Promedio'], 
                    df['Temp_Promedio'] + df['Std_Promedio'], 
                    color='green', alpha=0.2)
    
    sns.lineplot(data=df, x=df.index, y='Temp_Max', color='red', 
                 label='Temperatura Máxima', ax=ax)
    ax.fill_between(df.index, 
                    df['Temp_Max'] - df['Std_Max'], 
                    df['Temp_Max'] + df['Std_Max'], 
                    color='red', alpha=0.2)
    
    sns.lineplot(data=df, x=df.index, y='Temp_Min', color='blue', 
                 label='Temperatura Mínima', ax=ax)
    ax.fill_between(df.index, 
                    df['Temp_Min'] - df['Std_Min'], 
                    df['Temp_Min'] + df['Std_Min'], 
                    color='blue', alpha=0.2)
    ax.set_title('Serie Temporal de Temperaturas con Bandas de Error', fontsize=16)
    ax.set_xlabel(range(0,len('Fecha'),30), fontsize=12)
    ax.set_ylabel('Temperatura (°C)', fontsize=12)
    ax.legend(title='Leyenda', title_fontsize=12)
    plt.setp(ax.get_xticklabels(), rotation=45)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


def velocidad(año):
    # Obtener datos
    velocidad = ext_columna('veloc.viento',año)  
    date=ext_columna('date',año)
    dates = pd.date_range(start=date[0], end=date[-1], freq='D')
    df = pd.DataFrame({'Fecha': dates, 'Velocidad_viento': velocidad})
    fig = px.line(df, x='Fecha', y='Velocidad_viento', title='Velocidad del Viento durante un Año',
                 labels={'Velocidad_viento': 'Velocidad (km/h)', 'Fecha': 'Fecha'},template='plotly_dark')
    fig.update_traces(line_color='#1f77b4', line_width=2)
    fig.update_layout(hovermode='x unified',xaxis_title='Fecha',yaxis_title='Velocidad del Viento (km/h)',
        xaxis_rangeslider_visible=True)
    st.plotly_chart(fig, use_container_width=True)
    

def direccion(año):
    sns.set_style("whitegrid", {'grid.linestyle': ':', 'axes.edgecolor': '0.8'})
    plt.rcParams['font.family'] = 'DejaVu Sans'
    fechas = pd.date_range(start=ext_columna('date', año)[0], 
                         end=ext_columna('date', año)[-1], 
                         freq="D")
    direcciones = ext_columna('direcc.viento', año)
    df = pd.DataFrame({'Fecha': fechas,'Dirección': [float(d) for d in direcciones]})
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': 'polar'})
    sns.kdeplot(x=np.deg2rad(df['Dirección']),color='#1f77b4',fill=True,alpha=0.25,
        bw_adjust=0.5,ax=ax)
    ax.set_theta_zero_location('N') 
    ax.set_theta_direction(-1)       
    ax.set_xticks(np.deg2rad(np.arange(0, 360, 45)))
    ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    ax.set_title(f'Distribución de Direcciones del Viento - Año {año}',pad=20, fontsize=14, fontweight='bold')
    st.pyplot(fig) 
    plt.close(fig)

def presion(año):
    # Configuración de estilo profesional
    sns.set_style("whitegrid", {'grid.color': '0.9', 'axes.edgecolor': '0.4'})
    plt.rcParams['font.family'] = 'DejaVu Sans'
    fechas = pd.date_range(start=ext_columna('date', año)[0], 
                        end=ext_columna('date', año)[-1], 
                        freq="D")
    presiones = [float(p) for p in ext_columna('presion.atm', año)]
    df = pd.DataFrame({
        'Fecha': fechas,
        'Presión (hPa)': presiones
    })
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=df,
        x='Fecha',
        y='Presión (hPa)',
        color='#4e79a7',
        linewidth=1.5,
        alpha=0.6,
        label='Diario',
        ax=ax
    )
    df['Media_7d'] = df['Presión (hPa)'].rolling(7).mean()
    sns.lineplot(
        data=df,
        x='Fecha',
        y='Media_7d',
        color='#e15759',
        linewidth=2.5,
        label='Media 7 días',
        ax=ax
    )
    ax.set_title(f'Presión Atmosférica - Año {año}', 
                pad=20, fontsize=14, fontweight='bold')
    ax.set_xlabel('Fecha', fontsize=10)
    ax.set_ylabel('Presión (hPa)', fontsize=10)
    ax.axhline(1013.25, color='#59a14f', linestyle='--', 
              alpha=0.7, label='Presión estándar')
    ax.legend(loc='upper right', frameon=True, framealpha=0.9)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


def presion_temperatura(año):
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=ext_columna('date',año)[0],end=ext_columna('date',año)[-1], freq="D")
    
    def adaptacion(temperatura_prom):
        return [float(i)+994.6 for i in temperatura_prom]
    
    datos = {
        "Fecha": fechas,
        "Presión Atmosférica (hPa)": ext_columna('presion.atm',año),
        "Temperatura (°C)": adaptacion(ext_columna('temp.prom',año))
    }
    df = pd.DataFrame(datos)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="Fecha", y="Presión Atmosférica (hPa)", 
                color="blue", label="Presión Atmosférica", linewidth=2, ax=ax)
    sns.lineplot(data=df, x="Fecha", y="Temperatura (°C)", 
                color="red", label="Temperatura", linewidth=2, ax=ax)
    
    ax.set_title("Variación de Presión Atmosférica y Temperatura", fontsize=16, pad=20)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Valores", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title="Variables", loc="upper left")
    
    st.pyplot(fig)
    plt.close(fig)

def presion_viento(año):
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=ext_columna('date',año)[0],end=ext_columna('date',año)[-1], freq="D")
    
    def adaptacion(velocidad_viento):
        return [float(i)+1014.6 for i in velocidad_viento]
    
    datos = {
        "Fecha": fechas,
        "Presión Atmosférica (hPa)": ext_columna('presion.atm',año),
        "Velocidad (km/h)": adaptacion(ext_columna('veloc.viento',año))
    }
    df = pd.DataFrame(datos)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="Fecha", y="Presión Atmosférica (hPa)", 
                color="blue", label="Presión Atmosférica", linewidth=2, ax=ax)
    sns.lineplot(data=df, x="Fecha", y="Velocidad (km/h)", 
                color="red", label="Velocidad viento", linewidth=2, ax=ax)
    
    ax.set_title("Variación de Presión Atmosférica y Velocidad del viento", fontsize=16, pad=20)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Valores", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title="Variables", loc="upper left")
    
    st.pyplot(fig)
    plt.close(fig)

def comp_temporada_ciclonica(año):
    sns.set(style="whitegrid")
    fechas = pd.date_range(start=ext_columna('date',año)[151],end=ext_columna('date',año)[333], freq="D")
    
    def adaptacion(velocidad_viento_ciclon):
        return [float(i)+994.6 for i in velocidad_viento_ciclon]
    
    datos = {
        "Fecha": fechas,
        "Presión Atmosférica (hPa)": ciclones('presion.atm',año),
        "Velocidad (km/h)": adaptacion(ciclones('veloc.viento',año))
    }
    df = pd.DataFrame(datos)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="Fecha", y="Presión Atmosférica (hPa)", 
                color="blue", label="Presión Atmosférica", linewidth=2, ax=ax)
    sns.lineplot(data=df, x="Fecha", y="Velocidad (km/h)", 
                color="red", label="Velocidad viento", linewidth=2, ax=ax)
    
    ax.set_title("Temporada Ciclonica", fontsize=16, pad=20)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Valores", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title="Variables", loc="upper left")
    
    st.pyplot(fig)
    plt.close(fig)

def comp_temporada_invernal(n, año):
    sns.set(style="whitegrid")
    
    if n == 1:
        num = "Inicio de Año"
        fechas = pd.date_range(start=ext_columna('date',año)[0],end=ext_columna('date',año)[150], freq="D")
        presion_atm_invierno = frentes('presion.atm',1,año)
        velocidad_viento_invierno = frentes('veloc.viento',1,año)
        temperatura_min_invierno = frentes('temp.min',1,año)
    elif n == 2:
        num = "Final de Año"
        fechas = pd.date_range(start=ext_columna('date',año)[273],end=ext_columna('date',año)[-1], freq="D")
        presion_atm_invierno = frentes('presion.atm',2,año)
        velocidad_viento_invierno = frentes('veloc.viento',2,año)
        temperatura_min_invierno = frentes('temp.min',2,año)
    else:
        st.error("Error: los valores válidos son 1 o 2")
        return
    
    def adaptacion(datos):
        return [float(i)+998 for i in datos]
    
    datos = {
        "Fecha": fechas,
        "Presión Atmosférica (hPa)": presion_atm_invierno,
        "Velocidad (km/h)": adaptacion(velocidad_viento_invierno), 
        "Temperatura": adaptacion(temperatura_min_invierno)
    }
    df = pd.DataFrame(datos)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="Fecha", y="Presión Atmosférica (hPa)", 
                color="green", label="Presión Atmosférica", linewidth=2, ax=ax)
    sns.lineplot(data=df, x="Fecha", y="Velocidad (km/h)", 
                color="red", label="Velocidad viento", linewidth=2, ax=ax)
    sns.lineplot(data=df, x="Fecha", y="Temperatura", 
                color="blue", label="Temperatura Minima", linewidth=2, ax=ax)
    
    ax.set_title(f"Temporada Invernal {num}", fontsize=16, pad=20)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Valores", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title="Variables", loc="upper left")
    
    st.pyplot(fig)
    plt.close(fig)



