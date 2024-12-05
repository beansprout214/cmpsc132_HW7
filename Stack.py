class Stack():
        def __init__(self):
            self.__list = []

        def __str__(self):
            concat = ""
            for item in self.__list:
                if concat == "":
                    concat = str(item)
                    continue
                concat = f"{concat}, {str(item)}"
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