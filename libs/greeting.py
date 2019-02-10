import datetime
import logging
from libs.audio import Audio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Greeting:
    @staticmethod
    def run():
        logging.info('Greeting.run')

        hour = datetime.datetime.now().hour
        logging.info('Greeting.run - Hour: %d' % hour)

        if hour < 12:
            file = 'good_morning'
        elif 12 <= hour < 18:
            file = 'good_afternoon'
        else:
            file = 'goodnight'

        Audio.play(file)
