import pandas as pd
df=pd.read_excel('C:/visual_studio/datos_excel/cod_parr.xlsx',sheet_name='Datos') #LEE UN ARCHIVO DE EXCEL CON PANDAS COMO DATA FRAME
grupo1 = df.groupby(['PIT']) 
grupo2 = grupo1['PROMEDIO'].describe()

grupo2.to_excel('C:/visual_studio/salidas/datos_parr.xlsx', sheet_name='Resultado de pit') #GUARDA LOS ARCHIVOS EN FORMATO DE EXCEL
print(df)