from tkinter import *

class BaseMenu(Menu) :
    #Class for a menu that allows for quick changing of bases

    #Lowest base the calculator runs in
    __MIN_BASE = 2
    #Highest base the calculator runs in
    __MAX_BASE = 10

    def __init__(self, master, currentBase) :
        #Constructor of a menu with radiobuttons to select the new base
        #'current_base''s radiobutton will already be selected
        Menu.__init__(self, master=master)
        basesDropDown = Menu(self, tearoff=0)

        #Save the current base of the calculator
        self.__currentBase = currentBase
        #Save the master (Calculator instance)
        self.__master = master
        
        minBase = BaseMenu.__MIN_BASE
        maxBase = BaseMenu.__MAX_BASE
        for base in range(minBase, maxBase + 1) :
            state = DISABLED if base == currentBase else ACTIVE
            command = lambda base=base : self.__master.changeBase(base)
            basesDropDown.add_command(label="Base %i" %(base),
                                          command=command, state=state)
        self.add_cascade(label="Choose Base", menu=basesDropDown)
        
