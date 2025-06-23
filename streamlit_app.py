import streamlit as st
from datos_clima import *
from analisis_datos import *
from graficas import *
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from estadistica import *


st.title("🌤 Analisis climatico 🌧")
st.header('Analisis de bases de datos climaticas anuales')


st.info('Tenemos diponibles las bases de datos de los años 2023 y 2024.')

año=st.selectbox("Por favor elija uno:", ('2023', '2024'),)

st.header('Tabla de datos')
mostrar=st.checkbox('Mostrar tabla de datos', value=True,)
if mostrar:
    
    st.dataframe(data(año))
    st.caption('Tabla de datos')
else:
    '📜'

st.header('Estadistica basica 📑')
st.dataframe(gen_estadisticas_basicas(año))

st.header('Eventos meteorologicos')
def eventos():
    evento=st.selectbox("Por favor elija un evento:", ('Etapa ciclonica', 'Epoca invernal (comienzo de año)',
                                                       'Epoca invernal (finales de año)'),)
    if evento=='Epoca invernal (comienzo de año)':
        comp_temporada_invernal(1,año)
        st.dataframe(detectar_frentes_frios(1,año))
    elif evento=='Epoca invernal (finales de año)':
        comp_temporada_invernal(2,año)
        st.dataframe(detectar_frentes_frios(2,año))
    else:
        comp_temporada_ciclonica(año)
        st.dataframe(detectar_tormentas(año))

eventos()

st.header('Comportamiento de las magnitudes')
def grafica():
    grafo=st.selectbox("Por favor elija un tema:", ('Temperatura🌡', 'Viento 💨','Presion atmosferica ☁️'),)
    df=gen_tabla(año)
    if grafo=='Temperatura🌡':
        grafico_temperatura(año)
    elif grafo=='Viento 💨':
        velocidad(año)
        direccion(año)
    else:
        presion(año)
 
grafica()

st.header('Relacion entre las magnitudes')
def realacion(año):
    rela=st.selectbox("Por favor diga que relacion le interesa conocer:", ('🌡Temperatura - Presion atmosferica☁️',
                         '☁️Presion atmosferica - Viento💨'),)
    if rela=='🌡Temperatura - Presion atmosferica☁️' :
        presion_temperatura(año)
        x=ext_columna('temp.prom',año)
        y=ext_columna('presion.atm',año)
        st.info(
        f"""
        Relación Temperatura-Presión Atmosférica ({año})
        
        📊 Covarianza: {estadistica.Estadistica.covarianza(x,y)}  
- Indica la dirección de la relación:
    - Positiva → Ambas variables aumentan juntas
    - Negativa → Cuando una aumenta, la otra disminuye
        
        🔍 Coeficiente de Pearson: {estadistica.Estadistica.correlacion_pearson(x,y)})  
- Mide la fuerza y dirección de la relación lineal:
    - ±0.8 a ±1: Fuerte correlación
    - ±0.5 a ±0.8: Moderada
    - ±0 a ±0.5: Débil o nula
        """
    )
        st.success('''Efecto de la Temperatura sobre la Presión  
- Aire caliente:  
  - Las moléculas se mueven más rápido, se expanden y disminuyen su densidad.  
  - Esto genera bajas presiones (por ejemplo, en zonas ecuatoriales o durante el día en superficie).  
- Aire frío:  
  - Las moléculas se mueven más lento, se compactan y aumentan su densidad.  
  - Esto genera altas presiones (como en los polos o durante la noche).''')
    else: 
        presion_viento(año)
        x=ext_columna('veloc.viento',año)
        y=ext_columna('presion.atm',año)
        st.info(
        f"""
        Relación Temperatura-Presión Atmosférica ({año})
        
        📊 Covarianza: {estadistica.Estadistica.covarianza(x,y)}  
- Indica la dirección de la relación:
    - Positiva → Ambas variables aumentan juntas
    - Negativa → Cuando una aumenta, la otra disminuye
        
        🔍 Coeficiente de Pearson: {estadistica.Estadistica.correlacion_pearson(x,y)})  
- Mide la fuerza y dirección de la relación lineal:
    - ±0.8 a ±1: Fuerte correlación
    - ±0.5 a ±0.8: Moderada
    - ±0 a ±0.5: Débil o nula
        """
    )
        st.success('''**Principio Fundamental: El Viento como Consecuencia de Diferencias de Presión**  
El viento es el movimiento del aire desde zonas de alta presión hacia zonas de baja presión, impulsado por el gradiente de presión (diferencia de presión entre dos puntos).  

    - Ley básica: "El aire fluye de donde hay más presión a donde hay menos".
                   ''')
        st.success('''**Tipos de Vientos Según la Presión** 
Vientos Ciclónicos (Baja Presión)  
    - Cómo se forman: El aire asciende (por baja presión en superficie), creando vientos convergentes en espiral (huracanes, borrascas).  
    - Sentido:  
        - H. Norte: Giran en contra de las agujas del reloj.  
        - H. Sur: Giran a favor del reloj.  

Vientos Anticiclónicos (Alta Presión)  
    - Cómo se forman: El aire desciende (alta presión en superficie), generando vientos divergentes.  
    - Sentido:  
        - H. Norte: Giran a favor del reloj.  
        - H. Sur: Giran en contra del reloj.
  ''')
        

        
realacion(año)
