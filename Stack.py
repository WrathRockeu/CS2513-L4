class Stack:
    #A standard Stack class
    
    def __init__(self):
        #Initialise the Stack as an empty list
        self.__list = []

    def __str__(self):
        #Returns the stack as a string of numbers, one on top of the other,
        #with the top of the stack as the first line
        stack_string = ''
        if self.length() != 0 :
            for index in range(self.length() - 1, 0, -1) :
                stack_string += str(self.__list[index]) + '\n'

            #When we add the bottom item of the stack to the string, we don't
            #want to also add a line break, so we always add the 0th item here
            stack_string += str(self.__list[0]) + '\n'

        #Add some decorations to make it look a little nicer
        stack_string = '^\n' + stack_string + '--'
        return stack_string


    def pop(self):
        #Remove and return the top element of the stack.
        if len(self.__list) == 0:
            return None
        return self.__list.pop()

    def push(self, element):
        #Place element onto the top of the stack.
        self.__list.append(element)

    def top(self) :
        #Return the top element of the stack without removing it
        return self.__list[-1]

    def length(self):
        #Return the number of elements on the stack.
        return len(self.__list)

    def clear(self):
        #clear the stack
        self.__list = []

    def test() :
        stack = Stack()
        for i in range(2,6) :
            stack.push(i)
        print(stack)
