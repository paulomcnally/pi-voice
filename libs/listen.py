import speech_recognition as sr
import logging
from libs.audio import Audio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
                    Audio.play('ok')
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
