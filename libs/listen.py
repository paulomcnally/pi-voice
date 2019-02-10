import speech_recognition as sr
import logging
from libs.audio import Audio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Listen:
    @staticmethod
    def start():
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

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
                    pass
                except sr.UnknownValueError:
                    logging.info('Listen.start - UnknownValueError')
                    Audio.play('unknown_value_error')
                    pass
                except sr.RequestError:
                    logging.info('Listen.start - RequestError')
                    Audio.play('request_error')
                    pass

        except KeyboardInterrupt:
            pass
