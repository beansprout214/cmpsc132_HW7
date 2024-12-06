# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Stack.py
# Date: 12/5/24
#
# Description: Contains the Stack class
# Intended for use with LIFO practices


class Stack():
        def __init__(self):
            self.__list = []

        def __str__(self):
            concat = ""
            index = 0
            for item in self.__list:
                index += 1
                if concat == "":
                    concat = f"{index}: {item}"
                    continue
                concat = f"{concat}\n\n{index}: {item}"
            return concat

        def push(self,
                 data,
                 ):
            self.__list.append(data)

        def peek(self):
            return self.__list[-1] or None

        def pop(self):
            if not Stack.peek(self):
                return None
            return self.__list.pop(-1)

        def is_empty(self):
            return Stack.size(self) == 0

        def size(self):
            return len(self.__list)