import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0

leds = [24, 22, 23, 27, 17, 25, 12, 16]
leds1 = [24, 22, 23, 27, 17, 25, 12]
leds2 = [22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

light_time = 0.2

while True:
    for led in leds1:

        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)
    for led in reversed(leds2):
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)
