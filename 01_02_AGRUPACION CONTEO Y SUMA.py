# CALCULA LAS MEDIAS POR PIT
import os
#importa datos usando pandas, el archivo csv cada dato debe estar separado por comas, sino sale error
import pandas as pd
import numpy as np

os.system ("cls") # borra la pantalla
datos_df=pd.read_csv("C:/visual_studio/salidas/predios_rangos.csv") # datos_df es una variable tipo matriz o frame work  , datos.csv es el archivo
grupo1 = datos_df.groupby(['PIT','GRUPO','RANGO']) #agrupa los datos por pit, grupo, rango
grupo2= (grupo1.sum(['area']))# suma el area de cada grupo
grupo2=(grupo1.sum(['predios_n']))#suma la cantidad de predios de cada grupo

grupo2.to_csv('C:/visual_studio/salidas/viern_agrupacion.csv',index=True)# grava el arcivo de salida, el directorio siempre se debe poner con este tipo / sino sale error
