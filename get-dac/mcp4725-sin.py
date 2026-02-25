import r2r_dac as r2r
import math
import time
import RPi.GPIO as GPIO
import smbus

start = float(time.time())

def get_sin_wave_amplitude(freq, t):
    znach = math.sin(freq * 2 * math.pi * (float(time.time()) - start)) + 1
    return znach

amplitude = 3.2
signal_frequency = 50
sampling_frequency = 500

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
    
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()


    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        self.set_number(int(voltage / self.dynamic_range * 4095))

if __name__ == "__main__":
    try:
        dac = MCP4725(5.0)
        
        while True:
            try:
                dac.set_voltage((get_sin_wave_amplitude(signal_frequency, 4)/2) * amplitude)
                time.sleep(1/sampling_frequency)

            except ValueError as msg:
                print(f"{msg}\nВы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()