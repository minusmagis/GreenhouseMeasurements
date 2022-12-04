import sys
import time

import serial
import glob
import SmallFunctions as sf

D_COMS = True


# Serial port lister that returns a list of ports or an error when in an unsupported platform
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    port_list = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            if port != 'COM5':
                port_list.append(port)
        except (OSError, serial.SerialException):
            pass
    return port_list


# Identify loads and differentiate them from other devices
def detect_load(port):
    try:
        door = serial.Serial(port, 115200, timeout=5)
        time.sleep(0.2)
        door.write(b'*IDN?\n')
        time.sleep(0.2)
        readout = door.readline().decode('utf-8').rstrip('A\n')
        sf.debugging('Data Readout: '+str(readout), D_COMS)
        door.close()
        if 'KORAD' in readout: return True
        else: return False
    except serial.serialutil.SerialException as error:
        sf.debugging(error, D_COMS)
        sf.debugging('No KORAD load found at port ' + str(port), D_COMS)
        return False


# Read the data from a port and decide if it is an arduino or not
def detect_arduino(port):
    try:
        door = serial.Serial(port, 9600, timeout=5)
        readout = door.readline().decode('utf-8').rstrip('A\n')
        sf.debugging('Data Readout: '+str(readout), D_COMS)
        door.close()
        if 'Arduino' in readout: return True
        else: return False
    except serial.serialutil.SerialException:
        sf.debugging('No arduino found at port ' + str(port), D_COMS)
        return False


if __name__ == '__main__':

    print('---------------------------Coms test------------------------')

    port_list = serial_ports()
    print(port_list)
    for port in port_list:
        detect_load(port)


    print('---------------------------Coms test end------------------------')