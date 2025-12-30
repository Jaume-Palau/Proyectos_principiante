'''
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.
'''

#Por el momento usando esta url hace algunos espacios extraños y junta algunas palabras.
#https://www.rtve.es/noticias/20251128/reacciones-gobierno-socios-entrada-prision-abalos/16835828.shtml

import newspaper as nwp #Extrae texto de articulos web
import nltk #Herramienta de procesamiento de texto
import gtts #Combierte texto a mp3
import re

def extraer_articulo(url):
    #Crear objeto articulo:
    articulo = nwp.Article(url, language = 'es')
    articulo.download() #Descargar el articulo
    articulo.parse() #Parsear el texto

    titulo = articulo.title
    texto = articulo.text

    return titulo, texto


def limpiar_texto(texto):
    
    texto = texto.replace('-\n', '')
    texto = texto.replace('\n', ' ')
    texto = texto.replace('\r', ' ')

    texto = re.sub(r'\s+', ' ', texto)

    texto = texto.replace(' .', '.')
    texto = texto.replace(' ,', ',')
    texto = texto.strip()

    return texto


#Pruebas de uso:

url = input('Introduzca la url del articulo: ')

#Extraer y limpiar el texto:
titulo,texto = extraer_articulo(url)
texto_limpio = limpiar_texto(texto)

#Combertir el texto en archivo mp3:
tts = gtts.gTTS(text=texto_limpio,lang='es')
tts.save('articulo.mp3')
print('Mp3 generado con extito!')










