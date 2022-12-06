# Our main file.

'''
                Reconhecimento pelo Google 

import speech_recognition as sr

# Criar um recochecedor
r = sr.Recognizer()

# Abrir o microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define microfone como fonte de audio

        print(r.recognize_google(audio, language='pt'))
    
'''
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

# Síntaxe de fala 

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-2].id)

def speak(text):

    engine.say(text)
    engine.runAndWait()


# Loop do reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
        if result is not None:
            text = result['text']
           
            print(text)
       
            if text == 'horário' or text == ' me diga as horas':
                speak(core.SystemInfo.get_time())

            if text == 'data de hoje' or text =='data atual':
                speak(core.SystemInfo.get_data()) 
            
            if text == 'se apresente' or text =='como se chama':
                speak(core.Pessoa.get_nome()) 