import sys
import time
import msvcrt
import serial
import glob
import SmallFunctions as sf
import DataHandling as DH
import warnings


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

# identify loads by their serial number
def self_id_load(port):
    try:
        door = serial.Serial(port, 115200, timeout=5)
        time.sleep(0.2)
        door.write(b'*IDN?\n')
        time.sleep(0.2)
        foo, serial_number = door.readline().decode('utf-8').rstrip('\n').split('SN:')
        sf.debugging('Data Readout: '+str(serial_number), D_COMS)

        door.close()
        return serial_number

    except serial.serialutil.SerialException as error:
        sf.debugging(error, D_COMS)
        return None


# Run identification procedure to identify the active load for its correct cell string association
def load_lights_identification(port, signaling_time = 30):
    try:
        door = serial.Serial(port, 115200, timeout=5)

        # Id Routine with lights

        for i in range(signaling_time):
            time_delay = 0.2
            set_V = f':VOLT 0V\n'
            door.write(set_V.encode('utf-8'))
            time.sleep(time_delay)
            set_A = f':CURR 0A\n'
            door.write(set_A.encode('utf-8'))
            time.sleep(time_delay)
            set_R = f':RES 1OHM\n'
            door.write(set_R.encode('utf-8'))
            time.sleep(time_delay)
            set_P = f':POW 0W\n'
            door.write(set_P.encode('utf-8'))
            time.sleep(time_delay)
            sf.debugging(str(i)+' Please Identify load to string relation', D_COMS)

        door.close()

    except serial.serialutil.SerialException as error:
        sf.debugging(error, D_COMS)


def load_string_assign_check(port):
    serial_number = self_id_load(port)
    if DH.load_SN_to_string_num(serial_number) is None:
        warnings.warn('This load has not been asigned to a string yet. Please proceed to assign it when prompted \n')
        load_lights_identification(port)
        string_number = input('Please input the string number connected to the current load: ')
        DH.string_num_to_load_SN(string_number, serial_number)
    else:
        string_number = DH.load_SN_to_string_num(serial_number)
        sf.debugging('String Number: ' + str(string_number), D_COMS)

    return serial_number, string_number


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

    print('---------------------------Load Detection and Assigning------------------------')

    port_list = serial_ports()
    print(port_list)
    for port in port_list:
        detect_load(port)
        load_SN, load_string_number = load_string_assign_check(port)


    print('---------------------------Load Detection and Assigning end------------------------')