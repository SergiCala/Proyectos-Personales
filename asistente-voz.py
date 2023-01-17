import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

# Escuchar nuestro microfono y devolver el audio

def trans_audio_texto():

    # almacenar el recognicer en una variable

    r = sr.Recognizer()

    #configurar entrada del audio

    with sr.Microphone() as origen:

        # tiempo de espera

        r.pause_threshold = 0.8

        # informar que nos esta escuchando

        print("Adelante, te escucho")

        #guardar lo que escuche como audio

        audio = r.listen(origen)

        try:

            # buscar en google lo que escucho

            pedido = r.recognize_google(audio, language="es-es")

            # Enseñar el texto que capto

            print("Dijiste: " + pedido)

            # Devolver pedido

            return pedido

            # En caso de que no entienda que se dijo

        except sr.UnknownValueError:

            print("Perdona, no te entendi")

            return "Sigo esperando"


# Funcion para que el asistente tenga voz

def hablar_asistente(mensaje):

    # Encender el motor de pyttsx3

    engine = pyttsx3.init()

    # Pronunciar el mensaje

    engine.say(mensaje)
    engine.runAndWait()


# Informar del dia del a semana

def pedir_dia():

    # Crear variable con datos de hoy

    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el dia de la semana

    dia_semana = dia.weekday()

    print(dia_semana)

    # Diccionario para cambiar los numeros por nombre de los dias

    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves',
                  4: 'Viernes', 5: 'Sabado', 6: 'Domingo'}

    hablar_asistente(f'hoy es {calendario[dia_semana]}')


# Pedir hora

def pedir_hora():

    # Crear variable con los datos de la hora

    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} con {hora.minute} minutos'
    print(hora)


    # Decir la hora

    hablar_asistente(hora)


# Saludo inicial

def saludo_inicial():

    # Crear variable con datos de hora

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'


    # Decir el saludo

    hablar_asistente(f'{momento}, soy tu asistente personal, en que puedo ayudarte')


# Funcion central del asistente

def pedir_cosas():

    # Activar el saludo inicial

    saludo_inicial()

    # Variable de corte

    comenzar = True

    # Loop central

    while comenzar:

        # Activar el microfono y guardar el audio en texto

        pedido = trans_audio_texto().lower()

        if 'abre youtube' in pedido:
            hablar_asistente('Ahora mismo lo busco')
            webbrowser.open('https://www.youtube.com')
            continue
        elif ' abre el navegador' in pedido:
            hablar_asistente('Claro, no tardo')
            webbrowser('https://www.google.com')
            continue

        elif ' qué dia es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar_asistente('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=2)
            hablar_asistente('Esto es lo que he encontrado: ')
            hablar_asistente(resultado)
            continue

        elif 'busca en internet' in pedido:
            hablar_asistente('Buscando')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar_asistente('Esto es lo que he encontrado')
            continue

        elif 'reproduce' in pedido:
            pywhatkit.playonyt(pedido)
            continue

        elif 'adios' in pedido:
            hablar_asistente('Cualquier cosa me avisas')
            break


pedir_cosas()



