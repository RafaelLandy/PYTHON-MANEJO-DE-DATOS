# EXCEL SEPARAR  EL CONTENIDO QUE ESTA EN UNA SOLA CELDA PERO EN VARIAS LÍNEAS, EN CELDAS DIFERENTE
En este documento se explica cómo resolver un problema real, un problema ya de trabajo, a continuación en la primera imagen se explica que cual es el problema, que información se dispone y en la segunda imagen a donde se desea llegar u obtener

Imagen 01 de partida
![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2001.png)

Lo que se desea

![](https://github.com/RafaelLandy/IMAGENES-DE-SOPORTE/blob/main/imagen%20excel%2002.png)

## SOLUCION A ESTE “GRAN PROBLEMA”
Sería posible resolver en el mismo Excel, de forma casi manual, copiando el contenido de cada celda en otra hoja, este proceso si separa cada línea por celdas diferentes, pero tomaría mucho tiempo hacer de una gran cantidad de datos, en este caso de 222 celdas, y que hablar de más de 1000 celdas. Para esto PYTHON es una herramienta poderosa.
Como se puede apreciar


```python
# ingreso_datos.py

def defdatos():
    global a
    global b
    a=int(input("ingresa el 1 numero"))
    b=int(input("ingresa el 2 numero"))
    print("Para verificar",a,b)

```
