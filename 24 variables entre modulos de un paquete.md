# USO DE VARIABLES ENTRE MÓDULOS DE UN PAQUETE
Este tutorial esta dirigido a documentar como se puede usar variables entre módulos de un paquete. Mediante el primer modulo creamos y asignamos valores a 2 variables para usar en un segundo modulo llamado adición, las funciones de cada modulo se ejecuta a traves del modulo principal.py"

La clave del uso de las variables entre modulos de un paquete es el uso de la palabra reservada  \"global\" para definir variables globales.
En primer lugar debemos crear el paquete, que es un directorio o carpeta con varios archivos .py que se denominan módulos y dentro de ellos estarán las funciones entoces creamos dentro de una carpeta los siguientes archivos __init__.py ; ingreso_datos.py; adicion.py; principal.py.

![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/Directorio.jpg)


En el archivo __init__.py no se escribe ningún código, solo se crea ese archivo para que python reconozca a la carpeta como un paquete.

"Los otros archivos deberán tener el siguiente código (usado como ejemplo)"

## CONTENIDO DE CADA ARCHIVO


```python
# ingreso_datos.py

def defdatos():
    global a
    global b
    a=int(input("ingresa el 1 numero"))
    b=int(input("ingresa el 2 numero"))
    print("Para verificar",a,b)

```
 
```python
# adicion.py
def suma():
    from ingreso_datos import a, b #Del modulo igreso_datos importamos las variables a y be 
    suma=a+b
    print ("la suma es",suma)
```
##Finalmente en el archivo o modulo principal escribimos el códgio que nos permite ejecutar o interar entre los modulos y usar las variables

```python
#principal.py
def main():
    import ingreso_datos #importamos el modulo
    import adicion #importamos el modulo
    ingreso_datos.defdatos() # ejecutamos la función
    adicion.suma()# ejecutamos la función

    
"""Ejecuto el programa principal"""   
main()
```

