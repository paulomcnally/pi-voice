#!/usr/env/python3
import importlib

import speech_recognition as sr
import re
import os

from actions.play import Play
from actions.video import Video

recognizer = sr.Recognizer()
microphone = sr.Microphone()

play = ['reproduce música', 'reproducir música']
video = ['reproduce video', 'reproducir video']
keyword = 'auto'
exitWord = ['quit', 'exit']

commands = [
    dict(class_name='Play', re='reproduce música de (.*)'),
    dict(class_name='Video', re='reproduce video de (.*)')
]

try:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        os.system("omxplayer /home/pi/pi-voice/locales/es/goodnight.mp3")
    while True:
        with microphone as source:
            audio = recognizer.listen(source)
            os.system("omxplayer /home/pi/pi-voice/locales/es/success.mp3")
        try:
            value = recognizer.recognize_google(audio, None, "es-LA")

            for command in commands:
                regexp = re.compile(command['re'])
                match = regexp.match(value.lower())

                if match:
                    os.system("omxplayer /home/pi/pi-voice/locales/es/ok.mp3")
                    Action = getattr(importlib.import_module('actions.%s' % command['class_name'].lower()), command['class_name'])
                    Action.run(match.group())
                    break
                else:
                    print('No match')

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
