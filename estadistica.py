import math
from collections import Counter
import numpy as np
import pandas as pd

class Estadistica:

    @staticmethod
    def media(datos):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
        return sum(datos) / len(datos)
    
    @staticmethod
    def mediana(datos):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
            
        datos_ordenados = sorted(datos)
        n = len(datos_ordenados)
        mitad = n // 2
        
        if n % 2 == 1:
            return datos_ordenados[mitad]
        else:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
    
    @staticmethod
    def moda(datos):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
            
        contador = Counter(datos)
        max_frecuencia = max(contador.values())
        modas = [dato for dato, freq in contador.items() if freq == max_frecuencia]
        
        return modas[0] if len(modas) == 1 else modas
    
    @staticmethod
    def moda_serie(serie):
        frecuencia=serie.value_counts()
        modas=frecuencia[frecuencia==frecuencia.max()].index.tolist()
        return modas[0] 
    
    @staticmethod
    def varianza(datos, poblacional=True):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
            
        n = len(datos)
        media_val = Estadistica.media(datos)
        suma_cuadrados = sum((x - media_val) ** 2 for x in datos)
        
        divisor = n if poblacional else (n - 1)
        return suma_cuadrados / divisor
    
    @staticmethod
    def desviacion_estandar(datos, poblacional=True):
        return math.sqrt(Estadistica.varianza(datos, poblacional))
    
    @staticmethod
    def rango(datos):
        #Rango de un conjunto de datos
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
        return max(datos) - min(datos)
    
    @staticmethod
    def cuartiles(datos):
        #Calcula los cuartiles Q1, Q2 (mediana) y Q3 de un conjunto de datos
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
            
        datos_ordenados = sorted(datos)
        n = len(datos_ordenados)
        
        def calcular_percentil(p):
            pos = (n - 1) * p
            entero = int(pos)
            decimal = pos - entero
            
            if entero + 1 >= n:
                return datos_ordenados[-1]
            
            return datos_ordenados[entero] + decimal * (datos_ordenados[entero + 1] - datos_ordenados[entero])
        
        q1 = calcular_percentil(0.25)
        q2 = calcular_percentil(0.5)
        q3 = calcular_percentil(0.75)
        
        return q1, q2, q3
    
    @staticmethod
    def rango_intercuartil(datos):
        #Calcula el rango intercuartílico (Q3 - Q1)
        q1, _, q3 = Estadistica.cuartiles(datos)
        return q3 - q1
    
    @staticmethod
    def covarianza(x, y):
        if len(x) != len(y):
            raise ValueError("Las listas deben tener la misma longitud")
            
        n = len(x)
        media_x = Estadistica.media(x)
        media_y = Estadistica.media(y)
        
        suma = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
        return suma / (n - 1)
    @staticmethod
    def correlacion_pearson(x, y):
        #Calcula el coeficiente de correlación de Pearson entre dos variables
        if len(x) != len(y):
            raise ValueError("Las listas deben tener la misma longitud")
            
        cov = Estadistica.covarianza(x, y)
        desv_x = Estadistica.desviacion_estandar(x, poblacional=False)
        desv_y = Estadistica.desviacion_estandar(y, poblacional=False)
        
        return cov / (desv_x * desv_y)
    