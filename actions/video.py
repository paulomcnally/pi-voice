import os


class Video:
    @staticmethod
    def run(value):
        print(value)
        os.system("omxplayer /home/pi/pi-voice/locales/es/ok.mp3")
