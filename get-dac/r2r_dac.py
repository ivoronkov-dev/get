import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



# GPIO.output(leds, 0)

dynamic_range = 3.14

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        
    def set_number(self, number):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за (0.00 - {dynamic-range:.f2} B")
            print("Устанавливаем 0.0 В")
            return 0

        value = int(voltage / dynamic_range * 255)

        return [int(element) for element in bin(value)[2:].zfill(8)]

    def set_voltage(self, number):
        number = self.set_number(voltage)
        GPIO.output(self.gpio_bits, number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.143, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
