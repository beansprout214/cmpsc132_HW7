class Inventory():
    def __init__(self,
                 serial_number,
                 manufacture_date,
                 lot_number,
                 ):
        self.__serial_number = serial_number
        self.__manufacture_date = manufacture_date
        self.__lot_number = lot_number

    def get_serial_number(self):
        return self.__serial_number

    def get_manufacture_date(self):
        return self.__manufacture_date

    def get_lot_number(self):
        return self.__lot_number

    def set_serial_number(self,
                          serial_number
                          ):
        self.__serial_number = serial_number

    def set_manufacture_date(self,
                             manufacture_date
                             ):
        self.__manufacture_date = manufacture_date

    def set_lot_number(self,
                       lot_number
                       ):
        self.__lot_number = lot_number