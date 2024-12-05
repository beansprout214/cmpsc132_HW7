from Inventory import Inventory
from Stack import Stack

my_stack = Stack()

def is_int(user_input):
    if user_input is None or isinstance(user_input,bool):
        return False
    try:
        casted = int(user_input)
        return True
    except ValueError:
        return False

def input_integer():
    user_input = input()
    while not is_int(user_input):
        print(f"Field only accepts integer values.")
        user_input = input()
    return user_input

def input_string():
    user_input = input()
    while is_int(user_input):
        print(f"Field only accepts string values.")
        user_input = input()
    return user_input

def display():
    print(my_stack)
    return

def new_inventory():
    return

def add():
    new = new_inventory()
    if new:

    return False

def remove():
    return

def main():
    print(f"Welcome to the inventory manager!")
    user_input = 0
    while (user_input != 2):
        print(f"Please select any of the following options:"
              f"0 - Add Inventory"
              f"1 - Remove Inventory"
              f"2 - Display Stack"
              f"3 - Exit Program")

        user_input = input_integer()

        if user_input == 1:

        elif user_input == 2:

        elif user_input == 3:


    return