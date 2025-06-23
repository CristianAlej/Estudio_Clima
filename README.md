# Análisis de Bases de Datos Climáticas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-ff4b4b?logo=streamlit)

Este proyecto realiza análisis estadísticos avanzados sobre bases de datos climáticas, permitiendo visualizar el comportamiento de variables meteorológicas y establecer relaciones entre ellas además de detectar eventos climaticos.

## Características principales

- 📊 Análisis estadístico descriptivo (medias, percentiles, extremos)
- 📈 Visualización temporal interactiva 
- ⚡️ Detección automática de eventos meteorológicos extremos
- 🔍 Correlación entre variables climáticas
- 🌡️ Procesamiento de temperatura, presión atmosférica, velocidad del veinto, etc.
- 🖥️ Interfaz interactiva con Streamlit

## Requisitos

- Python 3.8+
- Bibliotecas principales:
```  
plaintext
  streamlit
  pandas
  numpy
  matplotlib
  seaborn
  plotly
 ```

## Instalación

1. Clona el repositorio:
   
```bash
   git clone https://github.com/CristianAlej/Estudio_Clima.git
   cd Estudio_Clima
``` 

2. Crea y activa un entorno virtual (recomendado):
   
```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
```
  

3. Instala dependencias:
   
```bash
   pip install -r requirements.txt
``` 

## Uso

### Interfaz interactiva (Streamlit)
```bash
streamlit run streamlit_app.py
```
## Estructura del proyecto

```plaintext
/Estudio_Clima
|
|   Bases de datos:
├── export_HVIEJ_2023
├── export_HVIEJ_2024
|
|   Funciones para extraer datos
├── datos_clima.py
|
|   Funciones para procesar datos:        
├── analisis_datos.py
|
|   Funciones para graficar
├── graficas.py
|
|   Biblioteca propia:    
├── estadistica.py
|
|   Aplicacion Principal 
├── streamlit_app.py 
|
|   Dependencias:
├── requirements.txt
|
|   Dependencias:
└── README.md             
```
## Créditos
Desarrollado por Cristian Alejandro Perdomo Bruzon - 
🌦️ Proyecto para análisis de patrones climáticos
