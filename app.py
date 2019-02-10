#!/usr/env/python3
import importlib
import speech_recognition as sr
import re
import os

recognizer = sr.Recognizer()
microphone = sr.Microphone()

# List of commands to execute
commands = [
    dict(class_name='Music', regular_expresion='reproduce música de (.*)'),
    dict(class_name='Video', regular_expresion='reproduce video de (.*)')
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
            print('Text: %s' % value)

            # We are looking for a valid action
            for command in commands:
                regexp = re.compile(command['regular_expresion'])
                match = regexp.match(value.lower())

                # A valid action was found
                if match:
                    print('Command: %s' % command['class_name'])
                    os.system("omxplayer /home/pi/pi-voice/locales/es/ok.mp3")
                    Action = getattr(importlib.import_module('actions.%s' % command['class_name'].lower()), command['class_name'])
                    Action.run(match.group())
                    break

            # No valid action found
            os.system("omxplayer /home/pi/pi-voice/locales/es/unsuccess.mp3")
        except sr.UnknownValueError as e:
            print(e)
            print("The Google API could not understand the audio...")
        except sr.RequestError as e:
            print(e)
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass
