#!/usr/env/python3
import RPi.GPIO as GPIO
import logging
import time
from libs.greeting import Greeting
from libs.listen import Listen

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
