from tkinter import *
from GridPositioner import *

class BasePanel(PanedWindow) :
    #Utility class for displaying and changing the current base of the
    #calculator
    
    #Row to use for the widgets
    __WIDGET_ROW = 0
    #Column to use for the widgets
    __WIDGET_COLUMN = 0
    #Columns per row
    __WIDGETS_PER_ROW = 3
    #Anchor for the text entry
    __ANCHOR = RIGHT
    #Text for the information label
    __LABEL_TEXT = "Base :"
    #Text for the button
    __BUTTON_TEXT = "Change"
    #Size (in chars) for entry
    __ENTRY_WIDTH = 2
    
    def __init__(self, master, base, width) :
        #Initialise the BasePanel with the 'master' window, the 'base' of
        #the calculator, and the 'width' of the window

        #Create a positioner to position the widgets
        row = BasePanel.__WIDGET_ROW
        col = BasePanel.__WIDGET_COLUMN
        cols = BasePanel.__WIDGETS_PER_ROW
        self.__positioner = GridPositioner(row=row, col=col, columns=cols)
        self.__width = width

        #Create the paned window to store our widgets in
        PanedWindow.__init__(self, master=master, orient=VERTICAL, width=width)
        #Create a Label for information
        self.__initialiseBaseLabel()
        #Create the base input field
        self.__initialiseBaseEntry(base)
        #Create the apply button
        self.__initialiseApplyButton()
        
    def __initialiseBaseLabel(self) :
        #Create a label to inform what this panel is for
        text = BasePanel._BasePanel__LABEL_TEXT
        info = Label(master=self, text=text)
        self.__positioner.add(info)

    def __initialiseBaseEntry(self, base) :
        #Initialise the base entry, with the current 'base'
        #already in the box

        #Create string variable to store the base
        self.__baseVariable = StringVar()
        #Initialise it to the current base
        self.__baseVariable.set(str(base))

        textvar = self.__baseVariable
        anchor = BasePanel.__ANCHOR
        width = BasePanel.__ENTRY_WIDTH
        #Create the textbox to display/change the base
        baseEntry = Entry(master=self, textvariable=textvar,
                                 justify=anchor, width=width)

        #Add the Entry to the panel       
        self.__positioner.add(baseEntry)

    def __initialiseApplyButton(self) :
        text = BasePanel.__BUTTON_TEXT
        changeButton = Button(master=self, text=text)
        #This is currently public as the Calculator class gives it its
        #command
        self.changeButton = changeButton
        self.__positioner.add(changeButton)

    def reset(self, base) :
        #In case of someone inputting an invalid base, set the display back
        #to the current base
        self.__baseVariable.set(str(base))

    def getBase(self) :
        #Return the base in the entry
        return self.__baseVariable.get()
