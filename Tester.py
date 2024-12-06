# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Tester.py
# Date: 12/5/24
#
# Description: Tests the Inventory, Date, and Stack classes with an attached menu


from Date import Date
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
    return int(user_input)

def input_string():
    user_input = input()
    while is_int(user_input):
        print(f"Field only accepts string values.")
        user_input = input()
    return user_input

def display():
    if my_stack.is_empty():
        print(f"Stack is empty!\n"
              f"Nothing to display.\n")
        return False
    print(f"{my_stack}\n")
    return

def new_inventory():
    print(f"Creating a new inventory object!\n"
          f"Please enter product Serial Number.")
    new_serial_number = input_integer()
    print(f"Please enter product Manufacture Date.\n")
    print(f"Manufacture Month:")
    new_month = input_integer()
    print(f"Manufacture Day:")
    new_day = input_integer()
    print(f"Manufacture Year:")
    new_year = input_integer()
    new_date = Date(new_month,new_day,new_year)
    print(f"Please enter product Lot Number.")
    new_lot_number = input_integer()
    new_inventory = Inventory(new_serial_number,new_date,new_lot_number)
    print(f"Are you sure you'd like to add the\n"
          f"following inventory object?\n\n"
          f"1 - Yes      2 - No\n\n"
          f"{new_inventory}\n")
    user_input = input_integer()
    print("")
    if user_input == 1:
        return new_inventory
    return False

def add():
    new = new_inventory()
    if new:
        print(f"Added to stack!")
        my_stack.push(new)
        print(f"Successfully added.")
        return True
    print(f"Successfully cancelled.")
    return False

def remove():
    if my_stack.is_empty():
        print(f"Stack is empty! There is\n"
              f"nothing to be removed.")
        return False

    print(f"Are you sure you'd like to remove\n"
          f"this item from the stack?\n\n"
          f"1 - Yes      2 - No\n\n"
          f"{my_stack.peek()}\n")
    user_input = input_integer()
    print("")
    if user_input == 1:
        print(f"Successfully removed.")
        return my_stack.pop()
    print(f"Successfully cancelled.")
    return False

def main():
    print(f"Welcome to the inventory manager!")
    while True:
        print(f"Please select any of the following options:\n"
              f"1 - Add Inventory\n"
              f"2 - Remove Inventory\n"
              f"3 - Display Stack\n"
              f"4 - Exit Program\n")

        user_input = input_integer()
        print("")

        if user_input == 1:
            print(f"Adding to inventory!\n")
            add()
        elif user_input == 2:
            print(f"Removing from inventory!\n")
            remove()
        elif user_input == 3:
            print(f"Displaying inventory!\n")
            display()
        elif user_input == 4:
            print(f"Exiting program!\n"
                  f"Thank you for using the inventory manager!\n")
            return

test_inventory1 = Inventory(1, Date(1, 1, 2000), 1)
test_inventory2 = Inventory(2, Date(2, 15, 2021), 2)
test_inventory3 = Inventory(3, Date(10, 5, 2018), 3)

my_stack.push(test_inventory2)
my_stack.push(test_inventory3)
my_stack.push(test_inventory1)

if __name__ == '__main__':
    main()