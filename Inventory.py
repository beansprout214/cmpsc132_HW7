# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Inventory.py
# Date: 12/5/24
#
# Description: Contains the Inventory class


class Inventory():
    def __init__(self,
                 serial_number,
                 manufacture_date,
                 lot_number,
                 ):
        self.__serial_number = serial_number
        self.__manufacture_date = manufacture_date
        self.__lot_number = lot_number

    def __str__(self):
        return (f"Serial Number: {self.__serial_number}\n"
                f"Manufacture Date: {self.__manufacture_date}\n"
                f"Lot Number: {self.__lot_number}")

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