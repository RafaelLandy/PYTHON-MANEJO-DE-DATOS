# GENERA UN ARCHIVO POR CADA PIT CON SUMA Y PROCENTAJE ACUMULADO DEL AREA Y CANTIDAD DE PREDIOS
import os
import openpyxl as xl
#importa datos usando pandas, el archivo csv cada dato debe estar separado por comas, sino sale error
import pandas as pd
import numpy as np

os.system ("cls") # borra la pantalla
datos_df=pd.read_csv("C:/visual_studio/salidas/viern_agrupacion.csv") # datos_df es una variable tipo matriz o frame work  , datos.csv es el archivo
lista=pd.read_csv("C:/visual_studio/datos_csv/lista_pits.csv")# Lee el archivo lista tiene los nombres de cada pit
for name in lista:
    PIT01= (datos_df[datos_df.PIT == name])# Extrae de la matriz los valores de la lista
    #Suma y porcentaje acumulado de area
    PIT01['area_sum'] = PIT01["area"].cumsum()
    PIT01['area_%_acum'] = round(100*PIT01.area_sum/PIT01["area"].sum(),2) #2 Es el numero de decimales
   #Suma y porcentaje acumulado de la cantidad de predios
    PIT01['pred_sum'] = PIT01["predios_n"].cumsum()
    PIT01['pred_%_acum'] = round(100*PIT01.pred_sum/PIT01["predios_n"].sum(),2)

    PIT01.to_excel('C:/visual_studio/salidas/pit_rango/%s.xlsx'%name, sheet_name='Resultado') #GUARDA LOS ARCHIVOS EN FORMATO DE EXCEL
    #PIT01.to_csv('C:/visual_studio/salidas/pit_rango/%s.csv' % name,index=True)# %s.csv' % name  el nombre es una variable

print('listo')

