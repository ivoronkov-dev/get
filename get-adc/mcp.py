import mcp3021_driver
import adc_plot
import time

adc = mcp3021_driver.MCP3021(3.143)

voltage_values = []
time_values = []
duration = 10.0

try:
    start = time.time()
    while time.time() - start < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.2)
    adc_plot.plot_sampling_period_hist(time_values)
finally:
    adc.deinit()