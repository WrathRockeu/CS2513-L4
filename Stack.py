class Stack:
    #A standard Stack class

    #Representative string for the top of stack
    __STACK_TOP = '^\n'
    #Representative string for the bottom of the stack
    __STACK_BOTTOM = '--'
    
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
        top = Stack.__STACK_TOP
        bottom = Stack.__STACK_BOTTOM
        stack_string = top + stack_string + bottom
        return stack_string


    def pop(self):
        #Remove and return the top element of the stack.
        if len(self.__list) == 0:
            element = None
        else :
            element = self.__list.pop()
        return element

    def push(self, element):
        #Place element onto the top of the stack.
        self.__list.append(element)

    def top(self) :
        #Return the top element of the stack without removing it
        if self.length() > 0 :
            answer = self.__list[-1]
        else :
            answer = None
        return answer

    def length(self):
        #Return the number of elements on the stack.
        return len(self.__list)

    def clear(self):
        #clear the stack
        self.__list = []
