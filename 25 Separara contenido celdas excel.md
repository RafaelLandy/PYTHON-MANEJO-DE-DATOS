# EXCEL SEPARAR  EL CONTENIDO QUE ESTA EN UNA SOLA CELDA PERO EN VARIAS LÍNEAS, EN CELDAS DIFERENTE
En este documento se explica cómo resolver un problema real, un problema ya de trabajo, a continuación en la primera imagen se explica que cual es el problema, que información se dispone y en la segunda imagen a donde se desea llegar u obtener

Imagen 01 de partida, se tiene información en cada celda, pero separado por salto de linea y se desea separar por celdas o filas de excel
![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2001.png)

Imagen 02 Lo que se desea, separar por celdas

![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2002.png)

## SOLUCION A ESTE “GRAN PROBLEMA”
Sería posible resolver en el mismo Excel, de forma casi manual, copiando el contenido de cada celda en otra hoja, este proceso si separa cada línea por celdas diferentes, pero tomaría mucho tiempo hacer de una gran cantidad de datos, en este caso de 222 celdas, y que hablar de más de 1000 celdas. Para esto PYTHON es una herramienta poderosa.
Como se puede apreciar la información esta en dos columnas "Codigo" y "Determinantes adicionales" , la primera es un identificador para cada fila, este código se realciona con unos sectores territoriales en este caso es de la cidad de Cuenca - Ecuador, no quiero entrar en detalles sobre la información porque lo importante es los datos que se disponen.

Partiendo de esta información se ha escrito un código en Python y para una mejor compresión se comenta en algunas lineas


```python
# SEPARA EL CONTENIDO DE UNA CELDA EXCEL EN VARIAS 
#Importamos esta libreria básica
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import DataFrame
import csv


archivo= pd.read_excel('C:/visual_studio\datos_excel/21_Norma_PIT_Ficha_Adicionales.xlsx') # lee el archivo base con su ruta correspondiente

lista_cod= archivo['Codigo'].unique() #obtiene una lista por cada codigo, se utilza para trabajar en cada linea, por cada código

# Bucle para leer cada fila según codigo y grabara un archivo csv por cada código
for name in lista_cod:
    fila= (archivo[archivo.Codigo== name]) 
    df=pd.DataFrame()
    
    df['det']=fila['Determinantes adicionales']
    deter=df['det'].unique()

    df.to_csv('C:/visual_studio/salidas/determinantes_gina/%s.csv'% name,index = False,encoding='utf-8')# Graba archivo csv, es un archivo de transicion previo al resulatdo final
   
      


 #BLOQUE PARA ABRIR CADA ARCHIVO CSV EMPEZAR A CAMBIAR Y GRABAR LOS CAMBIOS
 # SIRVE PARA ABRIR CADA ARCHIVO CSV Y ELIMINAR LAS COMILLAS, QUE HACE QUE EL CONTENIDO SALGA EN UNA SOLA CELDA, CUANDO SE BORRA ESTO Y AL GRABAR EN FORMATO XLSX LA INFORMACIÓN SE SEPARA POR CELDAS
for name in lista_cod:

     #ABRE EL ARCHIVO EN MODO LECTURA PARA REMPLAZAR O ELIMINAR LAS COMILLAS
     with open('C:/visual_studio/salidas/determinantes_gina/%s.csv'% name, newline='',encoding='utf-8') as File:  
         reader = csv.reader(File)
         Mydata=(File.read().replace('"', ''))
         File.close()
         print(Mydata)

     """MODIFICA EL ARCHIVO Y LO GRABA CON LOS CAMBIOS HECHOS"""
     ObjFichero = open('C:/visual_studio/salidas/determinantes_gina/%s.csv'% name,'w',encoding='utf-8')
     MiNuevoTexto = Mydata
     ObjFichero.write(MiNuevoTexto)
     ObjFichero.close()
     print(ObjFichero)
     print("LISTO")

     #Se abre el archivo modificado csv  , \t se pone como delimitador tab para finalmente grabar en formato xlsx
     import pandas as pd
     archivo= pd.read_csv('C:/visual_studio/salidas/determinantes_gina/%s.csv'% name,delimiter ='\t' ,encoding='utf-8') 
     archivo['COD']=name
    
     archivo.to_excel('C:/visual_studio/salidas/determinantes_gina/%s.xlsx'% name, sheet_name=name) #genera un archivo xlsx por cada código y luego se podran unir estos archivos en una sola hoja de excel usando un script 

print("LISTO ")
```
Finalmente los archivos creados por cada código se unen en una sola hoja de excel mediante un modulo llamado "RBDMerge", complemento que lo decargue de internet y lo instale en EXCEL. Es posible tambien crear un codigo PYTHON para unir los archivos xlsx pero bueno ya no lo hice y podría ser objeto de otra entrada.
