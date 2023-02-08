
#importamos las librerias
import googletrans
from googletrans import Translator

#print(googletrans.LANGUAGES)  #imprime abreviatura de lenguajes

#abrimos el archivo y leemos 
string=open('D:/Datos/rlandy/Documentos/guia.txt', 'r',encoding="utf_8")
text=string.read()

#activamos el motor traductor de google
translator = Translator() 

#traducimos
translated = translator.translate(text, dest='en') 
print (translated)
#Grabamos lo traducido en un archivo de texto
salida = open('D:/Datos/rlandy/Documentos/texto_esp2.txt',"a")#append mode
salida.write(translated.text)
salida.close()
print('****listo****')
