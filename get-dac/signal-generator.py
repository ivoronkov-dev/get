import numpy
import time
import math

start = float(time.time())

def get_sin_wave_amplitude(freq, t):
    znach = math.sin(freq * 2 * math.pi * (float(time.time()) - start)) + 1
    return znach
