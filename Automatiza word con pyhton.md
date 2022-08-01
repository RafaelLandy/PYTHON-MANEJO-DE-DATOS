# PYHTON: AUTOMATIZA WORD - GENERA INFORMES A PARTIR DE UNA TABLA EXCEL
### Nota: este código esta dirigido a personas que tienen conocimientos básicos e intermedios de PYTHON.

En este documento se explica cómo resolver un problema real, generar informes a partir de datos de una tabla en excel, a continuación se comparte el código


```python
# Importamos las ibrerias a utilizar
import pandas as pd
import docx

#leemos la hoja de datos 

archivo=pd.read_excel('C:/visual_studio/datos_excel/inventario areas protegidas2.xlsx',
                        sheet_name="Indicador")
lista= archivo['Nombre'].unique() # Creamos una lista con valores unicos de los nombres


# EN ESTE BUCLE POR CADA NOMBRE AGREGAMOS LA INFORMACION Y GRABAMOS EL ARCHIVO

for humedal in lista:
    doc = docx.Document('C:/Users/Rafael/Documents/Plantilla_humedales.docx') #Archivo planttilla
    
    fila= (archivo[archivo.Nombre== humedal]) # ACCEDEMOS A LA INFORMACION DE CADA FILA      
    nombre=humedal
    
    # ACCEDEMOS A LA INFORMACION DE CADA CELDA
    anio= fila ['Anio'].to_list()
    anio=str(anio[0])
    
    tipo= fila ['Tipo'].tolist()
    tipo=str(tipo[0])
    
    ubicacion= fila ['Ubicacion'].tolist()
    ubicacion=str(ubicacion[0])
    
    superficie= fila ['Superficie'].tolist()
    superficie= str(superficie[0])
    
    descripcion= fila ['Descripcion'].tolist()
    descripcion= str(descripcion[0])
    
    foto= fila ['Fotografia'].tolist()
    foto=str(foto[0])
    
    # AÑADIMOS LA INFORMACION AL DOCUMENTO PLANTILLA
    
    doc.add_heading((("INFORME DEL HUMEDAL: ")+nombre),1)
    doc.add_picture(foto)
    
    doc.add_heading(("AÑO DE INSCRIPCION: "),2)
    doc.add_paragraph(anio)
    
    doc.add_heading(("UBICACION: "),2)
    doc.add_paragraph(ubicacion)
    
    doc.add_heading(("SUPERFICIE: "),2)
    doc.add_paragraph(superficie + " ha")    
    
    doc.add_heading("DESCRIPCIÓN: ",2)
    doc.add_paragraph(descripcion)
    doc.save('C:/visual_studio/salidas/informe_word/%s.docx'% nombre) # Grabamos un archivo docx por cada nombre
    
print('LISTO')
```
