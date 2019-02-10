import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Audio:
    @staticmethod
    def play(file):
        logging.info('Audio.play')

        logging.info('Audio.play - File: %s' % file)
        subprocess.run('/usr/bin/omxplayer ./locales/es/%s.mp3 > /dev/null 2>&1' % file)
