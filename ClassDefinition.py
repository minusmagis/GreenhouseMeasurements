import USBComs


class String:
    def __init__(self,string_num):
        self.string_num = string_num



    # Load Class, stores basic Load data for communication
    class Load:
        def __init__(self,load_number):
            self.load_number = load_number
            self.com = None

        #Create a serial object to connect to the load
        def link_com(self):
            if self.com != None:
                self.serial = USBComs.create_serial_instance(self.com)
            else:
                raise Warning("No COM port defined for load" + str(self.load_number))

        def open_com(self):
            self.serial.open()

        def close_com(self):
            self.serial.close()

        # Add function that helps identify the loads and associates the right load with the right load number (maybe use SN)


class

if __name__ == '__main__':

# -------------------Load test---------------------------------

    print('---------------------------Load test------------------------')

    load1 = Load(1)
    load1.com = 'COM5'
    load1.link_com()

    print(load1.load_number)
    print(load1.com)

    load1.open_com()
    print('is serial com open? ' + str(load1.serial.is_open))

    load1.close_com()
    print('is serial com open? ' + str(load1.serial.is_open))

    print('---------------------------Load test end------------------------')

# -------------------Electrical Test ---------------------------------