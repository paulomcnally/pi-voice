import subprocess


class Video:
    @staticmethod
    def run():
        subprocess.run(['sh', '/home/pi/pi-voice/actions/video.sh'])


