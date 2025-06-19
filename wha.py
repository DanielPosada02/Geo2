import pywhatkit
import time
import random

# Lista de números
numeros = ["+573205345189","+573213131687", "+573227318375", "+573108818445","+573197787228"]

# Lista de mensajes con pequeñas variaciones
mensajes = [
    "Hola, ¿cómo estás? Solo quería enviarte este mensaje de prueba.",
    "¡Buenas! Este es un mensaje automático, solo de prueba 😊.",
    "Saludos, estoy probando el sistema de mensajes automáticos.",
    "Hola 👋, mensaje de prueba. Disculpa las molestias.",
    "¡Hola! Solo estoy probando un sistema, gracias por tu paciencia."
]

# Espera entre mensajes (en segundos)
espera_entre_mensajes = 20

for numero in numeros:
    mensaje = random.choice(mensajes)
    print(f"Enviando a {numero}: {mensaje}")
    pywhatkit.sendwhatmsg_instantly(numero, mensaje, wait_time=10, tab_close=True)
    print("Mensaje enviado. Esperando para el siguiente...")
    time.sleep(espera_entre_mensajes)