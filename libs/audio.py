import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Audio:
    @staticmethod
    def play(file):
        logging.info('Audio.play')

        logging.info('Audio.play - File: %s' % file)
        subprocess.run(['omxplayer', '/home/pi/pi-voice/locales/es/%s.mp3' % file])
