import serial
import USBComs
from time import sleep
import matplotlib.pyplot as plt
from numpy import arange
from datetime import datetime
import csv

# Important: Please ensure electronic load is configured for constant resistance (CR) before running this program.

# Configure device settings
device = USBComs.serial_ports()[0]

# COnfigure sweep settings
start_res = 25
end_res = 0
step = 0.5

current = []
voltage = []

def set_resistance(ser, res):
    set_res_str = f':RES {res}OHM\n'
    ser.write(set_res_str.encode('utf-8'))

def set_input(ser, state):
    set_input_str = f':INPut {state}\n'
    ser.write(set_input_str.encode('utf-8'))

def trigger_measurement(ser, res):
    set_resistance(ser, res)
    sleep(0.100)
    ser.write(b':MEASure:CURRent?\n')
    sleep(0.05)
    current.append(float(ser.readline().decode('utf-8').rstrip('A\n')))
    ser.write(b':MEASure:VOLTage?\n')
    sleep(0.05)
    voltage.append(float(ser.readline().decode('utf-8').rstrip('V\n')))

# Generate list of resistance used for sweep
res_list = arange(start_res, end_res - step, step * -1)

# Perform the sweep
with serial.Serial(device, timeout=5) as ser:
    # switch off the electronic load input
    set_input(ser, 'OFF')
    sleep(0.5)
    # start with start value of resistor
    set_resistance(ser, start_res)
    sleep(0.5)
    # switch on the electronic load input
    set_input(ser, 'ON')
    sleep(2) # settling time (I noticed anomalous results for start value of resistance without settling time)
    # Trigger sweep for all values of resistance
    for res in res_list:
        trigger_measurement(ser, res)
    sleep(0.5)
    # switch off the electronic load input
    set_input(ser, 'OFF')

# Plot graph of Voltage against Current
plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.plot(voltage, current, '-o')

# Save graph as PNG
now = datetime.now()
timestampStr = now.strftime("%Y%m%d%H%M%S")
plt.savefig(f'{timestampStr}.png')

# Save sweep data as csv
i = 0
with open(f'{timestampStr}.csv', mode='w') as sweep_data:
    sweep_writer = csv.writer(sweep_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sweep_writer.writerow(['resistance', 'voltage', 'current'])
    while i < len(voltage):
        sweep_writer.writerow([res_list[i], voltage[i], current[i]])
        i+=1