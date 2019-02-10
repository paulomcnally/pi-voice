#!/usr/env/python3
import speech_recognition as sr
import RPi.GPIO as GPIO
import time
from libs.greeting import Greeting
from libs.listen import Listen

recognizer = sr.Recognizer()
microphone = sr.Microphone()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# When the script starts, it executes the greeting
Greeting.run()

while True:
    input_state = GPIO.input(18)
    if not input_state:
        # We start listening with the microphone
        Listen.start()
        time.sleep(0.2)
