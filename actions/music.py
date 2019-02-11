import subprocess


class Music:
    @staticmethod
    def run():
        subprocess.run(['sh', '/home/pi/pi-voice/actions/music.sh'])
