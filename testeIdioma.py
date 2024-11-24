import speech_recognition as sr
import threading
from googletrans import Translator
import time
import requests

# URL do servidor Flask
url = 'http://localhost:5000/atualizar_textos'
idioma = 'ru'  # Idioma para reconhecimento de fala
capturando = False  # Variável booleana para controlar a captura

texto_Traducao = ""
texto_Transcricao = ""

# Inicializa o reconhecedor de fala e o tradutor
recognizer = sr.Recognizer()
translator = Translator()

# Variáveis globais para armazenar o áudio capturado
captura_audio = True
audio_buffer = []

# Função para capturar áudio continuamente
def capturar_audio_continuamente():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while captura_audio:
            try:
                audio = recognizer.listen(source, timeout=1)
                audio_buffer.append(audio)
            except sr.WaitTimeoutError:
                continue

# Função para processar áudio em trechos
def processar_audio():
    global texto_Traducao, texto_Transcricao
    while captura_audio:
        if audio_buffer:
            audio = audio_buffer.pop(0)
            try:
                text = recognizer.recognize_google(audio, language=idioma)
                if text.strip():  # Verifica se o texto não está vazio
                    print("Você disse: " + text)
                    texto_Transcricao = texto_Transcricao + " " +text
                    traducao = translator.translate(texto_Transcricao, dest='pt')  # Alterar o destino conforme necessário
                    print("Tradução: " + traducao.text)
                    texto_Traducao = traducao.text
                else:
                    print("Texto vazio recebido")
            except sr.UnknownValueError:
                print("Não consegui entender o que você disse")  # Log de depuração
            except sr.RequestError as e:
                print("Erro ao acessar o serviço de reconhecimento de voz; {0}".format(e))
        else:
            time.sleep(0.1)

# Função para iniciar a captura e processamento de áudio em threads separadas
def iniciar_captura_e_processamento():
    global captura_audio, capturando
    captura_audio = True
    capturando = True
    thread_captura = threading.Thread(target=capturar_audio_continuamente)
    thread_processamento = threading.Thread(target=processar_audio)
    thread_envio = threading.Thread(target=enviar)
    thread_captura.start()
    thread_processamento.start()
    thread_envio.start()
    return thread_captura, thread_processamento, thread_envio

# Função para interromper as threads
def interromper_captura_e_processamento(thread_captura, thread_processamento, thread_envio):
    global captura_audio, capturando, texto_Transcricao, texto_Traducao
    texto_Traducao = ""
    texto_Transcricao = ""
    captura_audio = False
    capturando = False
    thread_captura.join()
    thread_envio.join()
    thread_processamento.join()
    print("Captura e processamento de áudio interrompidos")

# Função para alternar entre iniciar e interromper a captura e processamento de áudio
def alternar_captura_processamento(lingua):
    global capturando, thread_captura, thread_processamento, idioma, thread_envio
    idioma = lingua
    if capturando:
        interromper_captura_e_processamento(thread_captura, thread_processamento,thread_envio)
    else:
        thread_captura, thread_processamento, thread_envio = iniciar_captura_e_processamento()


def enviar():
    while captura_audio:
        # Dados a serem enviados no formato JSON
        dados = {
        'translation': texto_Traducao,
        'transcricao': texto_Transcricao
        }
        print("texto enviado",texto_Transcricao, texto_Traducao)
        response = requests.post(url, json=dados)



# Inicializar as threads como None
thread_captura = None
thread_processamento = None
thread_envio = None 