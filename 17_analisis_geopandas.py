#ESTE CODIGO LEE EL ARCHIVO PREDIOS_SHP , CREA COLUMNAS DE RANGO Y GRUPO Y LOS LLENA DE ACUERDO A LA 
#LISTA DE CONDICIONES PARA EL CAMPO area. Funciona super bien , puede salir error sin causa, pero es por los campos del shp original
#Importa las librerias necesaria
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Lee el archivo shp
mapa=gp.read_file('E:/pugs_ultimo suspiro/LAYERS_VALIDACION/pits_predios.shp')

#print(mapa.head())
#print(mapa)
#mapa.plot()
#plt.show()


#LISTADO DE CONDICIONES
conditionlist = [
    (mapa['area'] <= 500) ,#G1
    (mapa['area'] > 500) & (mapa['area'] <=1000),#G2
    (mapa['area'] > 1000) & (mapa['area'] <=2000),#G3
    (mapa['area'] > 2000) & (mapa['area'] <=3000),#G4
    (mapa['area'] > 3000) & (mapa['area'] <=4000),#G5
    (mapa['area'] > 4000) & (mapa['area'] <=5000),#G6
    (mapa['area'] > 5000) & (mapa['area'] <=6000),#G7
    (mapa['area'] > 6000) & (mapa['area'] <=7000),#G8
    (mapa['area'] > 7000) & (mapa['area'] <=10000),#G9
    (mapa['area'] > 10000) & (mapa['area'] <=20000),#G10
    (mapa['area'] > 20000) & (mapa['area'] <=30000),#G11
    (mapa['area'] > 30000) & (mapa['area'] <=50000),#G12
    (mapa['area'] > 50000) & (mapa['area'] <=100000),#G13
    (mapa['area'] >=100000)]#G14
#Lista de valores a asiganar para cada condicion
choicelist = ['G01','G02', 'G03', 'G04','G05','G06', 'G07', 'G08','G09','G10',
 'G11', 'G12','G13','G14']
choicelist2 = ['<=500','500-1000', '1000-2000', '2000-3000','3000-4000','4000-5000', '5000-6000', '6000-7000','7000-10000','1-2 ha',
 '2-3 ha', '3-5 ha','5-10 ha','>10 ha']
#Crea los campos Grupo y Rango y asigna los valores de acuerdo a la condición  y a la lista de valores

mapa['GRUPO'] = np.select(conditionlist, choicelist, default='Not Specified')
mapa['RANGO'] = np.select(conditionlist, choicelist2, default='Not Specified')

#Graba el archivo en formato shp
mapa.to_file('C:/visual_studio/salidas_geo/predios_grupos.shp')
