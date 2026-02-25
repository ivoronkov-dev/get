import r2r_dac as r2r
import math
import time
import RPi.GPIO as GPIO

start = float(time.time())

def get_sin_wave_amplitude(freq, t):
    znach = math.sin(freq * 2 * math.pi * (float(time.time()) - start)) + 1
    return znach

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000



GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0.0)
        
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за (0.00 - {self.dynamic_range:.f2} B")
            print("Устанавливаем 0.0 В")
            self.pwm.ChangeDutyCycle(0)

        value = int(voltage / self.dynamic_range * 100)

        self.pwm.ChangeDutyCycle(value)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:

                dac.set_voltage((get_sin_wave_amplitude(signal_frequency, 4)/2) * amplitude)
                time.sleep(1/sampling_frequency)

            except ValueError as msg:
                print(f"{msg}\nВы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()