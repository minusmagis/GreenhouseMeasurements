import serial
import time
import sys
import glob


class classHardware_():
    def __init__(self, port):
        self.port = port
        self.status = "close"
        self.door = self.assign_port()

    def assign_port(self):
        try:
            door = serial.Serial(self.port, 115200, timeout=5)
            door.close()
            return door
        except serial.serialutil.SerialException:
            Warning("No COM port defined for load" + str(self.port))
            return None

    def open_door(self):
        if self.status == "close":
            self.door.open()
            self.status = "open"

    def close_door(self):
        if self.status == "open":
            self.door.close()
            self.status = "close"

class Load(classHardware_):
    def __init__(self, port):
        super().__init__(port)

    def init_smu(self, channel_nb, current_lim, oversamplerate):
        self.open_door()
        channel_name = 'CH' + str(channel_nb)
        self.door.write(bytes(channel_name +':ENA\r\n', encoding='utf8'))
        time.sleep(0.05)
        self.door.write(bytes(channel_name +':CUR '+ str(current_lim) + '\r\n', encoding='utf8'))
        time.sleep(0.05)
        self.door.write(bytes(channel_name +':OSR '+ str(oversamplerate) + '\r\n', encoding='utf8'))
        time.sleep(0.05)
        self.close_door()

class Main():
    def __init__(self):
        self.list_port = self.serial_ports()
        self.smu_dist = self.get_smu_dict()

    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def get_smu_dict(self):
        smu_dict = {}
        for port in self.list_port:
            smu_dict[port] = Load(port)





# class String:
#     def __init__(self,string_num):
#         self.string_num = string_num



#     # Load Class, stores basic Load data for communication
#     class Load:
#         def __init__(self,load_number):
#             self.load_number = load_number
#             self.com = None

#         #Create a serial object to connect to the load
#         def link_com(self):
#             if self.com != None:
#                 self.serial = USBComs.create_serial_instance(self.com)
#             else:
#                 raise Warning("No COM port defined for load" + str(self.load_number))

#         def open_com(self):
#             self.serial.open()

#         def close_com(self):
#             self.serial.close()

#         # Add function that helps identify the loads and associates the right load with the right load number (maybe use SN)


if __name__ == '__main__':
    f = Main()
    print(f.list_port)

# -------------------Load test---------------------------------

    # print('---------------------------Load test------------------------')

    # load1 = Load(1)
    # load1.com = 'COM5'
    # load1.link_com()

    # print(load1.load_number)
    # print(load1.com)

    # load1.open_com()
    # print('is serial com open? ' + str(load1.serial.is_open))

    # load1.close_com()
    # print('is serial com open? ' + str(load1.serial.is_open))

    # print('---------------------------Load test end------------------------')

# -------------------Electrical Test ---------------------------------