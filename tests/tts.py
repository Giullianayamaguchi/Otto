import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-3].id)

engine.say("olá, boa tarde, me chamo Otto")
engine.runAndWait()

