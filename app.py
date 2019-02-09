#!/usr/env/python3
import speech_recognition as sr
import os


keyword = 'auto'


r = sr.Recognizer()
m = sr.Microphone()

exitWord = ['quit', 'exit']

try:
    print("One moment...")
    with m as source: r.adjust_for_ambient_noise(source)
    # The above line takes an ambient sample of noise to set threshhold levels.
    # This may not work on all microphones and should be tweaked as needed
    while True:
        print("Now Ready, talk to me. (Press Ctrl+c to or say exit or quit to quit)")
        with m as source: audio = r.listen(source)
        print(".")
        try:
            value = r.recognize_sphinx(audio)
            if keyword.lower() in value.lower():
                if str is bytes:
                    reply = "{}".format(value).encode("utf-8")
                else:
                    reply = "{}".format(value)
                if reply in exitWord:
                    quit()
                else:
                    print("You said: %s" % reply)
                    os.system("flite -t  %s " % reply)
        except sr.UnknownValueError as e:
            print(e)
            print("The Google API could not understand the audio...")
        except sr.RequestError as e:
            print(e)
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass
