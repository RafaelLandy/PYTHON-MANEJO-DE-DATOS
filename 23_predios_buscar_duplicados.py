#ESTE CODIGO LEE EL ARCHIVO PREDIOS_SHP , BUSCA DUPLICADOS POR CLAVE , Y LOS MUESTRA EN UNA COLUMNA


#Importa las librerias necesaria
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Lee el archivo shp
mapa=gp.read_file('E:/pugs_ultimo suspiro/LAYERS_VALIDACION/pits_predios.shp')

#DUPLICADOS 


mapa['duplicado']=mapa.duplicated(subset=['codigo'],keep=False)


#Graba el archivo en formato shp
mapa.to_file('C:/visual_studio/salidas_geo/predios_duplicados.shp')