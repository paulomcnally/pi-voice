import os
import logging


class Audio:
    @staticmethod
    def play(file):
        logging.info('Audio.play')

        logging.info('Audio.play - File: %s' % file)
        os.system('omxplayer ./locales/es/%s.mp3' % file)
