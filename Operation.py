from Stack import *
from ProgramConstants import OPERATORS

class Operation :
    #A class for running operations in the calculator

    #A list of all of the operation functions, where the index of the
    #function in this list is equal to the index of its operator
    #in the other list
    #THe functions will be added in the __init__
    __OPERATION_FUNCTIONS = []

    #Length of stack required for Binary Operations
    __BINARY_LENGTH = 2

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
        operators = OPERATORS
        operationFunctions = Operation.__OPERATION_FUNCTIONS
        operatorIndex = operators.index(operator)
        operationFunctions[operatorIndex](self.__stack, current_base)

        #Since all op_functions push the answer onto the stack, we just
        #return the top of the stack
        return self.__stack.top()

    def __add(stack, current_base) :
        #Add the top two operands on the stack, and push the new value
        if stack.length() >= Operation.__BINARY_LENGTH :
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
        if stack.length() >= Operation.__BINARY_LENGTH :
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
        if stack.length() >= Operation.__BINARY_LENGTH :
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
        if stack.length() >= Operation.__BINARY_LENGTH :
            #We want to ensure we don't try to divide by 0
            if stack.top() != '0' :
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
            else :
                #If we try to divide by 0, we want to display the error in the
                #output field
                stack.pop()
                stack.push('ZeroDivisionError')
            
    def __negate(stack, current_base) :
        #Negates the top item of the stack
        #Check if the stack has at least one item on it
        if stack.top() != None :
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
