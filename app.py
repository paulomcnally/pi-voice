#!/usr/env/python3
import speech_recognition as sr
import os

from actions.play import Play
from actions.video import Video

recognizer = sr.Recognizer()
microphone = sr.Microphone()

play = ['reproduce música', 'reproducir música']
video = ['reproduce video', 'reproducir video']
keyword = 'auto'
exitWord = ['quit', 'exit']

try:
    print("Loading...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
    while True:
        print("Ready")
        os.system("omxplayer /home/pi/pi-voice/locales/es/goodnight.mp3")
        with microphone as source:
            audio = recognizer.listen(source)
        print(".")
        try:
            value = recognizer.recognize_google(audio, None, "es-LA")
            print(value)

            if value.lower() in play:
                os.system("omxplayer /home/pi/pi-voice/locales/es/ok.mp3")
                Play.listen()
            if value.lower() in video:
                os.system("omxplayer /home/pi/pi-voice/locales/es/ok.mp3")
                Video.listen()

            if keyword.lower() in value.lower():
                if str is bytes:
                    reply = "{}".format(value).encode("utf-8")
                else:
                    reply = "{}".format(value)
                if reply in exitWord:
                    quit()
                else:
                    print("You said: %s" % reply)
                    os.system("flite -t  %s " % reply)
        except sr.UnknownValueError as e:
            print(e)
            print("The Google API could not understand the audio...")
        except sr.RequestError as e:
            print(e)
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass
