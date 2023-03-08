import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# opciones de voz
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Escuchar microfono y devolver audio como texto
def transformar_audio_en_texto():


    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, lenguaje="as-mx")

            # prueba de que se pudo transformar el audio a texto
            print('Dijiste: ' + pedido)

            # devolver pedido
            return pedido
        
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print('ups, no entendi')

            # devolver error
            return "sigo esperando"

        # En caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print('ups, algo ha salido mal')

            # devolver error
            return "sigo esperando"


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Ejecutar prueba de voz
# hablar('Hello world')

# Informar el dia de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.datetime.today()
    print(dia)

    # Crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con los nombres de los dias
    calendario = {0: 'Lunes',
                1: 'Martes',
                2: 'Miércoles',
                3: 'Jueves',
                4: 'Viernes',
                5: 'Sábado',
                6: 'Domingo'}

    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar hora
def pedir_hora():

    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir hora
    hablar(hora)


# Funcion saludo incial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'buen día'
    else:
        momento = 'Buenas tardes'

    # decir saludo
    hablar(f'{momento}, soy Hugo, tu asistente personal. Por favor dime en que te puedo ayudar')


# Funcion central del asistente
def pedir_cosas():

    # Activar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:
        
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('Buscando en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Buscando')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, reproduciendo')
            pywhatkit.playonyt(pedido)
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                    'amazon':'AMZN',
                    'google':'GOOGL'}
            try:
                accion_buscar = cartera[accion]
                accion_buscar = yf.Ticker(accion_buscar)
                precio_actual = accion_buscar.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('perdon, no la he encontrado')
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


pedir_cosas()


# Codigo para saber que voces tiene el ordenador y poder utilizarlas
'''engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)'''