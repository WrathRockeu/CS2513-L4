from tkinter import *
from ProgramConstants import CLEAR_STACK_DEFAULT, DISPLAY_STACK_DEFAULT
class OptionMenu(Menu):

    #Label for the Clear Stack option
    __CLEAR_STACK_LABEL = "Clear Stack on Base Change"
    #Label for the Display Stack option
    __DISPLAY_STACK_LABEL = "Display Stack"
    
    def __init__(self,master,clearStack=CLEAR_STACK_DEFAULT,
                 displayStack=DISPLAY_STACK_DEFAULT):
        #A constructor for the options menu
        #Call the superclass constructor
        Menu.__init__(self,master=master,tearoff=0)
        #Save the master for later use
        self.__master = master
        #Create a BooleanVar for whether or not we clear the stack on base change
        self.__clearStack = BooleanVar()
        self.__clearStack.set(clearStack)
        #Create a BooleanVar for whether or not we should display the stack panel
        self.__displayStack = BooleanVar()
        self.__displayStack.set(displayStack)
        #Add the options checkboxes
        self.__addOptions()
        
    def __addOptions(self):
        #Adds the checkboxes to the menu
        #Checkbox for clearing the stack
        clearLabel = OptionMenu.__CLEAR_STACK_LABEL
        self.add_checkbutton(label=clearLabel,variable=self.__clearStack,
                             onvalue = 1,offvalue = 0)

        """Not sure if we want this"""
        """Well, I dont really give a fuck... If I feel like it I will implement
           this
           Regards,
           Grzegorz Ikwanty"""
        #Checkbox for displaying the stack
        displayLabel = OptionMenu.__DISPLAY_STACK_LABEL
        command = self.__master.onStackDisplayChange
        self.add_checkbutton(label=displayLabel,variable=self.__displayStack,
                             onvalue = 1,offvalue = 0,command=command)

    @property
    def clearStack(self) :
        #Public getter for self.__clearStack
        return self.__clearStack

    @property
    def displayStack(self) :
        #Public getter for self.__displayStack
        return self.__displayStack
