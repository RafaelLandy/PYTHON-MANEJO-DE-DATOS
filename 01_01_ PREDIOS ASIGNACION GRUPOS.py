# CREA UN CAMPO Y CLASIFICA A CADA PREDIO A GRUPO EN FUNCIÓN DEL TAMAÑO DE SUPERFICIE
import os

import pandas as pd
import numpy as np
#os.system ("cls") # borra la pantalla
datos_df=pd.read_csv("C:/visual_studio/datos_csv/predios.csv") #importa datos usando pandas, el archivo csv cada dato debe estar separado por comas, 
#sino sale errordatos_df es una variable tipo matriz o frame work  , datos.csv es el archivo
datos_df['predios_n']=1 # Crea una columna de nombre predios_n y asigna el valor 1, sirve para contar y sumar cantidad de predios
#LISTADO DE CONDICIONES
conditionlist = [
    (datos_df['area'] <= 500) ,#G1
    (datos_df['area'] > 500) & (datos_df['area'] <=1000),#G2
    (datos_df['area'] > 1000) & (datos_df['area'] <=2000),#G3
    (datos_df['area'] > 2000) & (datos_df['area'] <=3000),#G4
    (datos_df['area'] > 3000) & (datos_df['area'] <=4000),#G5
    (datos_df['area'] > 4000) & (datos_df['area'] <=5000),#G6
    (datos_df['area'] > 5000) & (datos_df['area'] <=6000),#G7
    (datos_df['area'] > 6000) & (datos_df['area'] <=7000),#G8
    (datos_df['area'] > 7000) & (datos_df['area'] <=10000),#G9
    (datos_df['area'] > 10000) & (datos_df['area'] <=20000),#G10
    (datos_df['area'] > 20000) & (datos_df['area'] <=30000),#G11
    (datos_df['area'] > 30000) & (datos_df['area'] <=50000),#G12
    (datos_df['area'] > 50000) & (datos_df['area'] <=100000),#G13
    (datos_df['area'] >=100000)]#G14

choicelist = ['G01','G02', 'G03', 'G04','G05','G06', 'G07', 'G08','G09','G10',
 'G11', 'G12','G13','G14']
choicelist2 = ['<=500','500-1000', '1000-2000', '2000-3000','3000-4000','4000-5000', '5000-6000', '6000-7000','7000-10000','1-2 ha',
 '2-3 ha', '3-5 ha','5-10 ha','>10 ha']
datos_df['GRUPO'] = np.select(conditionlist, choicelist, default='Not Specified')
datos_df['RANGO'] = np.select(conditionlist, choicelist2, default='Not Specified')
#print(datos_df)
#rango1=(datos_df[(datos_df.area > 0) & (datos_df.area <= 1000)])
#print(rango1)
#grupo1 = rango1.groupby(['PIT','PARROQUIA'])
#print (grupo1)
#valor_media= (grupo1.mean(['COD_PARR']))# calcula la media de cada campo numerico, esto es solo una forma de para poder sacar la agrupacion
#os.system ("cls") 
#print(valor_media)
datos_df.to_csv('C:/visual_studio/salidas/predios_rangos.csv',index=True)# el directorio siempre se debe poner con este tipo


# de barra / con \ da error  - True se debe poner para que el archivo ponga una etiqueta, en este caso la PARROQUIA , con FALSE
#solo pone los campos numericos