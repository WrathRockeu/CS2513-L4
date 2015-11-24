from tkinter import *
from ProgramConstants import TEAROFF

class BaseMenu(Menu) :
    #Class for a menu that allows for quick changing of bases

    #Lowest base the calculator runs in
    __MIN_BASE = 2
    #Highest base the calculator runs in
    __MAX_BASE = 10
    #Label for the Base buttons
    __BASE_LABEL = "Base %i"

    def __init__(self, master, currentBase) :
        #Constructor of a menu with radiobuttons to select the new base
        #'current_base''s button will already be selected
        Menu.__init__(self, master=master, tearoff=TEAROFF)

        #Save the current base of the calculator
        self.__base = currentBase
        #Save the master (Calculator instance)
        self.__master = master

        #Create the dropdown menu
        self.__initialiseDropDown()

    def __initialiseDropDown(self) :
        #Create the options in the dropdown menu
        currentBase = self.__base
        minBase = BaseMenu.__MIN_BASE
        maxBase = BaseMenu.__MAX_BASE
        label = BaseMenu.__BASE_LABEL
        for base in range(minBase, maxBase + 1) :
            state = DISABLED if base == currentBase else ACTIVE
            command = lambda base=base : self.__master.changeBase(base)
            self.add_command(label=label %(base),
                                          command=command, state=state)
        
