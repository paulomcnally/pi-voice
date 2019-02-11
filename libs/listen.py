import importlib

import speech_recognition as sr
import logging
import re
from libs.audio import Audio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of commands to execute
commands = [
    dict(class_name='Music', regular_expresion='reproduce música'),
    dict(class_name='Video', regular_expresion='reproduce videos')
]


class Listen:
    @staticmethod
    def start():
        listen = True
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        try:
            with microphone as source:
                logging.info('Listen.start - Adjusting microphone')
                recognizer.adjust_for_ambient_noise(source)
            while listen:
                with microphone as source:
                    logging.info('Listen.start -Microphone listening')
                    Audio.play('i_hear_you')
                    audio = recognizer.listen(source)
                    Audio.play('success')
                try:
                    text = recognizer.recognize_google(audio, None, "es-NI")
                    logging.info('Listen.start - Text: %s' % text)

                    for command in commands:
                        match = re.match(command['regular_expresion'], text.lower())
                        if match:
                            logging.info('Listen.start - %s' % command['class_name'])
                            library = importlib.import_module('actions.%s' % command['class_name'].lower())
                            Action = getattr(library, command['class_name'])
                            Action.run()
                            Audio.play('ok')
                            break
                    logging.info('Listen.start - No match')
                    Audio.play('unsuccess')
                    listen = False
                except sr.UnknownValueError:
                    logging.info('Listen.start - UnknownValueError')
                    Audio.play('unknown_value_error')
                    listen = False
                except sr.RequestError:
                    logging.info('Listen.start - RequestError')
                    Audio.play('request_error')
                    listen = False

        except KeyboardInterrupt:
            pass
