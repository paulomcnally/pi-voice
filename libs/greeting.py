import datetime
import logging
import pyttsx3
import i18n

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = pyttsx3.init()
i18n.add_translation('greeting')


class Greeting:
    @staticmethod
    def run():
        logging.info('Greeting.run')

        hour = datetime.datetime.now().hour
        logging.info('Greeting.run - Hour: %d' % hour)

        if hour < 12:
            engine.say(i18n.t('greeting.good_morning'))
        elif 12 <= hour < 18:
            engine.say(i18n.t('greeting.good_afternoon'))
        else:
            engine.say(i18n.t('greeting.goodnight'))

        engine.runAndWait()
