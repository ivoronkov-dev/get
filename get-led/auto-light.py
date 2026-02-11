import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0

button = 6
GPIO.setup(button, GPIO.IN)


while True:
    if GPIO.input(button):
        GPIO.output(led, 0)
        time.sleep(0.1)
    else:
        GPIO.output(led, 1)
        time.sleep(0.1)