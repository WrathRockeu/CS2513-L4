import re
from Stack import *

class Operation :
    #A class for running operations in the calculator

    #A list of all possible operators that can be given to apply()
    __OPERATORS = ['+', '-', '*', '/', '(-)']

    #A list of all of the operation functions, where the index of the
    #function in this list is equal to the index of its operator
    #in the other list
    #THe functions will be added in the __init__
    __OPERATION_FUNCTIONS = []

    def __init__(self, stack) :
        #Initialise the operation class with access to the stack
        self.__stack = stack
        Operation.__OPERATION_FUNCTIONS = [Operation.__add,
        Operation.__subtract, Operation.__multiply, Operation.__divide,
        Operation.__negate]

    def apply(self, operator, current_base) :
        #Applies the 'operator' to the appropriate values on the stack

        #Get the index of the operator in the operators list and apply 
        #that indexed function from the functions list
        operator_index = Operation.__OPERATORS.index(operator)
        Operation.__OPERATION_FUNCTIONS[operator_index](self.__stack, 
                                                        current_base)

        #Since all op_functions push the answer onto the stack, we just
        #return the top of the stack
        return self.__stack.top()

    def __add(stack, current_base) :
        #Add the top two operands on the stack, and push the new value
        if stack.length()>1:
            #These are strings
            value1 = stack.pop()
            value2 = stack.pop()
            #Convert from the current_base to decimal
            #These are now ints
            value1 = Operation.__convertToDecimal(value1, current_base)
            value2 = Operation.__convertToDecimal(value2, current_base)

            answer = value1 + value2

            #Return the answer to the appropriate base
            #This is a string
            answer = Operation.__convertFromDecimal(answer, current_base)
            stack.push(answer)

    def __subtract(stack, current_base) :
        #Subtract the second item from the top of the stack from the top item
        #and push the answer on the stack
        if stack.length()>1:
            #These are strings
            value2 = stack.pop() #Top item
            value1 = stack.pop() #Second from the top

            #Convert from the current_base to decimal
            #These are now ints
            value1 = Operation.__convertToDecimal(value1, current_base)
            value2 = Operation.__convertToDecimal(value2, current_base)

                    #Second - top
            answer = value1 - value2

            #Return the answer to the appropriate base
            #This is a string
            answer = Operation.__convertFromDecimal(answer, current_base)
            stack.push(answer)

    def __multiply(stack, current_base) :
        #Multiply the top two items on the stack together, and push the
        #answer onto the stack
        if stack.length()>1:
            #These are strings
            value1 = stack.pop()
            value2 = stack.pop()

            #Convert from the current_base to decimal
            #These are now ints
            value1 = Operation.__convertToDecimal(value1, current_base)
            value2 = Operation.__convertToDecimal(value2, current_base)

            answer = value1 * value2

            #Return the answer to the appropriate base
            #This is a string
            answer = Operation.__convertFromDecimal(answer, current_base)
            stack.push(answer)

    def __divide(stack, current_base) :
        #Divide the second item from the top of the stack by the top item
        #and push the answer on the stack
        if stack.length()>1:
            #These are strings
            value2 = stack.pop() #Top item
            value1 = stack.pop() #Second from top

            #Convert from the current_base to decimal
            #These are now ints
            value1 = Operation.__convertToDecimal(value1, current_base)
            value2 = Operation.__convertToDecimal(value2, current_base)
      
                    #second // top
            answer = value1 // value2

            #Return the answer to the appropriate base
            #This is a string
            answer = Operation.__convertFromDecimal(answer, current_base)
            stack.push(answer)
            
    def __negate(stack, current_base) :
        #Negates the top item of the stack

        #String value of the top of the stack
        value = stack.pop()

        #Convert from current_base to decimal
        #Now int value
        value = Operation.__convertToDecimal(value, current_base)

        answer = value * -1

        #Return the answer to the appropriate base
        #Now string value
        answer = Operation.__convertFromDecimal(answer, current_base)
        stack.push(answer)

    def __convertToDecimal(number, old_base) :
        #Converts the string 'number' in base 'old_base' into an integer in
        #base 10 
        return int(str(number), old_base)

    def __convertFromDecimal(number, new_base) :
        #Converts the integer 'number' in base 10 to the string equivalent
        #in base 'new_base'
        if number == 0 :
            number_string = '0'
        else :
            if number < 0 :
                #Negative numbers will have a - sign in front of them
                number *= -1
                sign = '-'
            else :
                sign = ''
            number_string = ''
            while number > 0 :
                number_string = str(number % new_base) + number_string
                number //= new_base
            number_string = sign + number_string
        return number_string

def test() :
    base = 10
    binary_ops = ['+', '-', '*', '/']
    stack = Stack()
    operation = Operation(stack)
    loop = True
    while loop :
        value = input('Input a value (ops are +, -, *, /, *-1) >>> ')

        try :
            int(value)
            stack.push(value)

        except :
            if value.lower() == 'q' :
                loop = False

            elif value in binary_ops :
                if stack.length() < 2 :
                    print('Not enough operands on the stack')
                else :
                    operation.apply(value, base)
                    print(stack.top())

            elif value == '*-1' :
                if stack.length() < 1 :
                    print('Not enough operands on the stack')
                else :
                    operation.apply(value, base)
                    print(stack.top())
            else :
                print('Invalid input')
        print(stack)
#test()
