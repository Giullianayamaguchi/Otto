# Our main file.

import speech_recognition as sr

# Criar um recochecedor
r = sr.Recognizer()

# Abrir o microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define microfone como fonte de audio

        print(r.recognize_google(audio, language='pt'))
        