from tkinter import *

class BasePanel(PanedWindow) :
    #Utility class for displaying and changing the current base of the
    #calculator
    
    #Number of widgets in this panel
    __WIDGETS = 2
    #Row to use for the widgets
    __WIDGET_ROW = 0
    #Column for the Entry widget (button is placed relative to span of
    #panel)
    __ENTRY_COLUMN = 0
    #Anchor for the text entry
    __ANCHOR = RIGHT
    #Text for the button
    __TEXT = "Change"
    #Sticky for each widget
    __STICKY = "EW"
    
    def __init__(self, master, base, span) :
        #Initialise the BasePanel with the 'master' window, the 'base' of
        #the calculator, and the 'span' of how wide we can make it

        #Create the paned window to store our widgets in
        PanedWindow.__init__(self, master=master, orient=VERTICAL)
        #Create the base input field
        self.__initialiseBaseField(base, span)
        #Create the apply button
        self.__initialiseApplyButton(span)
        self.pack()
        

    def __initialiseBaseField(self, base, span) :
        #Initialise the base input field, with width 1 less than 'span'
        #and the current 'base' already in the field

        #Create string variable to store the base
        self.__baseVariable = StringVar()
        #Initialise it to the current base
        self.__baseVariable.set(str(base))

        textvar = self.__baseVariable
        anchor = BasePanel.__ANCHOR
        #Create the textbox to display/change the base
        self.__baseEntry = Entry(master = self, textvariable =
                                 textvar, justify=anchor)

        #Add the Entry to the panel
        row = BasePanel.__WIDGET_ROW
        column = BasePanel.__ENTRY_COLUMN
        sticky = BasePanel.__STICKY        
        #Span is span for panel, we want this entry to
        #take up the remaining space if the button takes 1 column
        if span == 1 :
            #We need to put the button underneath the Entry as there is
            #only 1 widget per row
            columnspan = span
            BasePanel.__WIDGET_ROW += 1 #For the button
        else :
            columnspan = span - 1
            
        self.__baseEntry.grid(row=row, column=column,
                              columnspan=columnspan, sticky=sticky)

    def __initialiseApplyButton(self, span) :
        applyButton = Button(master=self, text=BasePanel.__TEXT,
                             command=self.__onApplyButtonClick)
        row = BasePanel.__WIDGET_ROW
        column = span - 1
        sticky = BasePanel.__STICKY
        applyButton.grid(row=row, column=column, sticky=sticky)

    def __onApplyButtonClick(self) :
        pass

win = Tk()
bp = BasePanel(win, 10, 3)
win.mainloop()
