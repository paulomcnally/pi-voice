import speech_recognition as sr
import logging
from libs.audio import Audio

recognizer = sr.Recognizer()
microphone = sr.Microphone()


class Listen:
    @staticmethod
    def start():
        try:
            with microphone as source:
                logging.info('Listen.start - Adjusting microphone')
                recognizer.adjust_for_ambient_noise(source)
            while True:
                with microphone as source:
                    logging.info('Listen.start -Microphone listening')
                    audio = recognizer.listen(source)
                    Audio.play('success')
                try:
                    value = recognizer.recognize_google(audio, None, "es-NI")
                    print('Text: %s' % value)
                except sr.UnknownValueError:
                    logging.info('Listen.start - UnknownValueError')
                    Audio.play('unknown_value_error')
                except sr.RequestError:
                    logging.info('Listen.start - RequestError')
                    Audio.play('request_error')

        except KeyboardInterrupt:
            pass
