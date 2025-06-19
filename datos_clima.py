import pandas as pd

df_23=pd.read_excel(r"C:\Users\Cristian\Downloads\Telegram Desktop\export_HVIEJ_HAV_2023.xlsx")
df_24=pd.read_excel(r"C:\Users\Cristian\Downloads\Telegram Desktop\export_HVIEJ_HAV_2024.xlsx")

#Clima 2023:
    
    #Temperatura:
        
        #Temperatura promedio:
temperatura_prom_23=df_23['tavg'].tolist()
        #Temperatura maxima:
temperatura_max_23=df_23['tmax'].tolist()
        #Temperatura minima:
temperatura_min_23=df_23['tmin'].tolist()
    
    #Condiciones del viento:
        
        #Direccion:
direccion_viento_23=df_23['wdir'].tolist()
        #Velocidad:
velocidad_viento_23=df_23['wspd'].tolist()

    #Presion atmosferica:
presion_atm_23=df_23['pres'].tolist()



#Clima 2024:
    
    #Temperatura:
        
        #Temperatura promedio:
temperatura_prom_24=df_24['tavg'].tolist()
        #Temperatura maxima:
temperatura_max_24=df_24['tmax'].tolist()
        #Temperat4ra minima:
temperatura_min_24=df_24['tmin'].tolist()
    
    #Condiciones del viento:
        
        #Direccion:
direccion_viento_24=df_24['wdir'].tolist()
        #Velocidad:
velocidad_viento_24=df_24['wspd'].tolist()

    #Presion atmosferica:
presion_atm_24=df_24['pres'].tolist()
