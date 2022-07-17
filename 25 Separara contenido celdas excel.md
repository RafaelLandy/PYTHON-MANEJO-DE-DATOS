# PYHTON: SEPARAR  EN VARIAS CELDAS EL CONTENIDO QUE ESTÁ EN UNA SOLA CASILLA DE EXCEL PERO SEPARADOS POR SALTOS DE LINEA
### Nota: este código esta dirigido a personas que tienen conocimientos básicos e intermedios de PYTHON.

En este documento se explica cómo resolver un problema real, un problema ya de trabajo, a continuación en la primera imagen se explica cual es el problema, que información se dispone y en la segunda imagen a donde se desea llegar u obtener

Imagen 01 de partida, se tiene información en cada celda, pero separado por salto de linea y se desea separar por celdas o filas de excel
![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2001.png)

Imagen 02 Lo que se desea, separar por celdas

![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2002.png)

## SOLUCION A ESTE “GRAN PROBLEMA”
Sería posible resolver en el mismo Excel, de forma casi manual, copiando el contenido de cada celda en otra hoja, este proceso si separa cada línea por celdas diferentes, pero tomaría mucho tiempo hacer de una gran cantidad de datos, en este caso de 222 celdas, y que hablar de más de 1000 celdas. Para esto PYTHON es una herramienta poderosa.
Como se puede apreciar la información esta en dos columnas "Codigo" y "Determinantes adicionales" , la primera es un identificador para cada fila, este código se realciona con unos sectores territoriales en este caso es de la cidad de Cuenca - Ecuador, no quiero entrar en detalles sobre la información porque lo importante es los datos que se disponen.

Partiendo de esta información se ha escrito un código en Python y para una mejor compresión se comenta en algunas lineas.
Lo he escrito como una función o programa, es importante desde el inicio aprender a escribir nuestros codigos como funciones porque debemos ir acostumbrandonos a reciclar o reutilizar los códigos y eso se facilita si lo escribimos con la sintaxis de función , en donde se define los parametros o variables que utilizamos, en este caso es ruta_i se refiere a la ruta del archivo de inicio, ruta_s es la ruta de salida de los resultado del proceso, campo1 se refiere al campo o columna de nombre "Codigo" del archivo de inicio, campo 2 se refiere al nombre de la columna del archivo de inicio del cual vamos a extraer la información en este caso se llama 'Determinantes adicionales'.


```python
def separa_celdas(ruta_i, ruta_s_,campo1,campo2): #NOMBRAMOS LA FUNCION Y PONEMOS SUS PARAMETROS O VARIABLES
    #Importamos esta libreria básica
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    from pandas import DataFrame
    import csv


    archivo= pd.read_excel(ruta_i) # lee el archivo base con su ruta correspondiente
    global lista_cod
    lista_cod= archivo[campo1].unique() #obtiene una lista por cada codigo, se utilza para trabajar en cada linea, por cada código

    # Bucle para leer cada fila según codigo y grabara un archivo csv por cada código
    for name in lista_cod:
        fila= (archivo[archivo.Codigo== name])         
        df=pd.DataFrame()
        df['det']=fila[campo2]
        df.to_csv(ruta_s_+'/%s.csv'% name,index = False,encoding='utf-8')# Graba archivo csv, es un archivo de transicion previo al resulatdo final; + se pone para unir string


     #BUCLE PARA ABRIR CADA ARCHIVO CSV EMPEZAR A CAMBIAR Y GRABAR LOS CAMBIOS
    # SIRVE PARA ABRIR CADA ARCHIVO CSV Y ELIMINAR LAS COMILLAS, QUE HACE QUE EL CONTENIDO SALGA EN UNA SOLA CELDA, CUANDO SE BORRA ESTO Y AL GRABAR EN FORMATO XLSX LA INFORMACIÓN SE SEPARA POR CELDAS
    for name in lista_cod:

        #ABRE EL ARCHIVO EN MODO LECTURA PARA REMPLAZAR O ELIMINAR LAS COMILLAS
        with open(ruta_s_+'%s.csv'% name, newline='',encoding='utf-8') as File:  
            reader = csv.reader(File)
            Mydata=(File.read().replace('"', ''))
            File.close()
            print(Mydata)

       #MODIFICA EL ARCHIVO Y LO GRABA CON LOS CAMBIOS HECHOS
        ObjFichero = open(ruta_s_+'%s.csv'% name,'w',encoding='utf-8')
        MiNuevoTexto = Mydata
        ObjFichero.write(MiNuevoTexto)
        ObjFichero.close()
        print(ObjFichero)
        

        #Se abre el archivo modificado csv  , \t se pone como delimitador tab para finalmente grabar en formato xlsx
        
        archivo= pd.read_csv(ruta_s_+'%s.csv'% name,delimiter ='\t' ,encoding='utf-8') 
        archivo['COD']=name
        archivo.to_excel(ruta_s_+'%s.xlsx'% name, sheet_name=name) #genera un archivo xlsx por cada código y luego se podran unir estos archivos en una sola hoja de excel usando un script 

    "Bloque para concatenar o unir los archivos xlsx en un solo archivo"
    df2=pd.DataFrame()
    df2 = df2.assign(det=None,COD=None)   
    
    for name in lista_cod:
        
        df3=pd.read_excel(ruta_s_+'%s.xlsx'%name)
        valores1=df2[['det','COD']]
        valores2=df3[['det','COD']]
        unido=[valores1,valores2]
        sal=pd.concat(unido)
        df2=sal
    sal.to_excel(ruta_s+'RESULTADO.xlsx')
        
    print("LISTO ") 

"""BLOQUE PARA EJECUTAR LA FUNCIÓN - SE DEBE ESCRIBIR BIEN LAS RUTAS Y NOMBRES DE CAMPOS"""

ruta_i='C:/visual_studio\datos_excel/21_Norma_PIT_Ficha_Adicionales.xlsx'
ruta_s='C:/visual_studio/salidas/determinantes_gina/'
campo1='Codigo'
campo2='Determinantes adicionales'
separa_celdas(ruta_i, ruta_s,campo1,campo2)
```
La concatenación de los archivos creados por cada código se unen en una sola hoja de excel mediante  una parte del código pytnon, pero también se puede unir en el mismo excel con un módulo llamado "RBDMerge", complemento que lo descargue de internet y lo instale en EXCEL, que igual permite concatenar de manera masiva varios archivos de xlsx.
