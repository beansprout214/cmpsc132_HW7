# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Date.py
# Date: 12/5/24
#
# Description: Contains the Date class


class Date():
    def __init__(self, month, day, year):
        self.__month = month
        self.__day = day
        self.__year = year

    def __str__(self):
        return f"{self.__month}/{self.__day}/{self.__year}"

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def get_year(self):
        return self.__year

    def set_month(self, month):
        self.__month = month

    def set_day(self, day):
        self.__day = day

    def set_year(self, year):
        self.__year = year
