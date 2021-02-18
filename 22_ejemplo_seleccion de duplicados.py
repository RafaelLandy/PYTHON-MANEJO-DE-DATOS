#DE UN ARCHIVO BUSCA VALORES DUPLICADOS EN ESTE CASO DE LA COLUMNA CODIGO
import numpy as np
import pandas as pd

#Lee el archivo y mantiene el tipo texto de la columna codigo para que no se borre el cero adelante
df=pd.read_csv(r'C:/visual_studio/datos_csv/duplicados.csv',converters={'codigo': lambda x: str(x)}) 

#imprime los valores dupliados con valores identicos para cada columna
#print(df.duplicated())

print(df.duplicated(df.columns[df.columns.isin(['codigo'])]))
df['duplicado']=(df.duplicated(df.columns[df.columns.isin(['codigo'])]))
print(df)
df.to_csv('C:/visual_studio/salidas/datos_duplicados.csv',index=True)