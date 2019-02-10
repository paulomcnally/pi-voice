import speech_recognition as sr
import os

recognizer = sr.Recognizer()
microphone = sr.Microphone()


class Video:
    @staticmethod
    def listen():
        os.system("omxplayer /home/pi/pi-voice/locales/es/i_did_not_find_the_song_you_requested.mp3")
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
            while True:
                with microphone as source:
                    audio = recognizer.listen(source)
                try:
                    print("Sphinx thinks you said '" + recognizer.recognize_google(audio, None, "es-LA") + "'")
                except sr.UnknownValueError:
                    print("Sphinx could not understand audio")
                except sr.RequestError as e:
                    print("Sphinx error; {0}".format(e))

        except KeyboardInterrupt:
            pass
