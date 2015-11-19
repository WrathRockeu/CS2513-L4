from tkinter import *

class BasePanel(PanedWindow) :
    #Utility class for displaying and changing the current base of the
    #calculator
    
    #Number of widgets in this panel
    __WIDGETS = 2
    
    def __init__(self, master, base, span) :
        #Initialise the BasePanel with the 'master' window, the 'base' of
        #the calculator, and the 'span' of how wide we can make it

        #Create the paned window to store our widgets in
        PanedWindow.__init__(self, master=master, orient=VERTICAL)
        #Create the base input field
        self.__initialiseBaseField(base, span)
        #Create the apply button
        self.__intialiseApplyButton()

    def __initialiseBaseField(self, base, span) :
        #Initialise the base input field, with width 1 less than 'span'
        #and the current 'base' already in the field

        #Create string variable to store the base
        self.__baseVariable = StringVar()
        #Initialise it to the current base
        self.__baseVariable.set(str(base))
