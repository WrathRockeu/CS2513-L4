from tkinter import *
from IOPanel import *
from Digit import *
from GridPositioner import *
from Stack import *
from Operation import *
from StackPanel import *
from BasePanel import *
from BaseMenu import *
from math import ceil

# Class for a GUI-based calculator.
class Calculator( Tk ) :
    # Width of @IOPanel@ in pixels.
    __IO_PANEL_WIDTH = 200
    # Height of @IOPanel@ in pixels.
    __IO_PANEL_HEIGHT = 50
    # Row number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_ROW = 0
    # Column number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_COL = 0
    # Span of @IOPanel@ in widgets in the grid layout of the calculator.
    __IO_PANEL_SPAN = 3

    # The default base of the calculator.
    __BASE = 10

    # The title of this calculator's window.
    __TITLE = "Calculator"

    # Row number of the first digit row in grid layout of the calculator.
    __DIGIT_ROW = 1
    # Column number of the first digit row in grid layout of the calculator.
    __DIGIT_COL = 0
    # Number of digit buttons per row in grid layout of the calculator.
    __DIGITS_PER_ROW = 3

    # Text on the clear button.
    __CLEAR_TITLE = "C"
    # Text on the push button.
    __PUSH_TITLE  = "P"
    #Sticky for the stack panel
    __STACK_STICKY = 'NS'
    #Operand strings for the operand buttons
    __OPERANDS  = ["+","-","*","/","(-)","CE"]
    
    # Main constructor.
    #  @parent@: The master widget of this @Calculator@ or @None@
    #  @base@: The number base for this @Calculator@.
    def __init__( self, master, title=__TITLE, base=__BASE ) :
        #INITIALIZE THE STACK
        self.__stack = Stack()
        #Initialise the Operation class
        self.__operation = Operation(self.__stack)
        # Initialise main calculator window.
        Tk.__init__( self, master )
        # Set title.
        self.title( title )
        #Set not resizable
        self.resizable(0,0)
        # Save @master@. Not used...
        self.__master = master
        # Finish rest of initialisation.
        self.__initialise( base=base )
        
    # Utility method for initialising this @Calculator@'s components.
    #  @base@: the number base of this @Calculator@'s operations.
    def __initialise( self, base ) :
        # Initialise the IO panel component.
        self.__initialiseIOPanel( )
        # Initialise the digit panel component.
        self.__initialiseDigitPanel( base=base)
        #Initialise the operand panel component
        self.__initialiseOperandPanel()
        #Initialise the base-change widgets
        self.__initialiseBaseMenu(base)
        #Initialise the stack display panel
        self.__initialiseStackPanel()

    # Initialise the digit panel widget of this @Calculator@.
    #  @base@: the number base of this @Calculator@'s operations.
    #  @row@: row number in grid layout of this @Calculator@.
    #  @col@: column number in grid layout of this @Calculator@.
    #  @digitsPerRow@: digits per row in grid layout of this @Calculator@.
    def __initialiseDigitPanel( self,
                                base,
                                row=__DIGIT_ROW,
                                col=__DIGIT_COL,
                                digitsPerRow=__DIGITS_PER_ROW ) :
        appendee = self.__iopanel
        self.__base = base
        self.__positioner = GridPositioner( row=row, col=col,
                                            columns=digitsPerRow )
        for digit in [ digit for digit in range( 1, base ) ] + [ 0 ] :
            button = Digit( master=self, digit=digit, appendee=appendee )
            self.__positioner.add( button )
        self.__addSpecialDigitPanelButton( text=Calculator.__CLEAR_TITLE,
                                        command=self.__onClearButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__PUSH_TITLE,
                                        command=self.__onPushButtonClick )

    # Utility method for adding additional button to the digit panel.
    #  @text@: the text on the button.
    #  @command@: the button's callback method.
    def __addSpecialDigitPanelButton( self, text, command ) :
        button = Button( master=self, text=text, command=command )
        self.__positioner.add( button )

    # Initialise the IO panel widget of this @Calculator@.
    def __initialiseIOPanel( self ) :
        width = Calculator.__IO_PANEL_WIDTH 
        height = Calculator.__IO_PANEL_HEIGHT
        # create the IO panel.
        iopanel = IOPanel( master=self, width=width, height=height )
        row = Calculator.__IO_PANEL_ROW
        col = Calculator.__IO_PANEL_COL
        span = Calculator.__IO_PANEL_SPAN
        # Add the IO panel to the current crid layout.
        iopanel.grid( row=row, column=col, columnspan=span )
        # Save object reference to the IO panel for future use.
        self.__iopanel = iopanel

    def __initialiseOperandPanel( self ):
        #Add the Operand buttons to the panel
        for operand in Calculator.__OPERANDS:
            if operand == Calculator.__OPERANDS[-1]:
                #Position of the clear everything operand string
                self.__addSpecialDigitPanelButton(operand,self.__onClearAllButtonClick)
            else:
                self.__addSpecialDigitPanelButton(operand,
                                                  lambda operand=operand:self.__onOperandButtonClick(operand))
                
    def __initialiseBaseMenu(self, base) :
        #Create the panel for changing calculator base, put it at the bottom
        baseMenu = BaseMenu(self, base)
        self.config(menu=baseMenu)

    def __initialiseStackPanel(self):
        self.__stackPanel = StackPanel(master=self,width=(Calculator.__IO_PANEL_WIDTH//2),
                            height=Calculator.__IO_PANEL_HEIGHT,
                            stack=self.__stack)
        #This gets the last row used in the window
        rows = ceil(self.__positioner.addedWidgets /
               Calculator.__DIGITS_PER_ROW) + 1
        sticky = Calculator.__STACK_STICKY
        self.__stackPanel.grid(row=0, column=Calculator.__DIGITS_PER_ROW +1, rowspan=rows, sticky=sticky)
        self.__stackPanel.update()

    # Callback method for push button
    def __onPushButtonClick( self ) :
        #push the value of the input field onto the stack
        var = self.__iopanel.get( )
        if var != "":
            self.__stack.push(var)
            self.__stackPanel.update()
            self.__iopanel.reset( )

    # Callback method for clear button
    def __onClearButtonClick( self ) :
        self.__iopanel.reset( )

    #Handle presses of operand buttons
    def __onOperandButtonClick(self, operand) :
        #Handle the clicking of operand buttons
        #Push any input in the field onto the stack, if any
        self.__onPushButtonClick()
        #Run the apply function, then display the answer
        self.__iopanel.set(self.__operation.apply(operand,self.__base))
        self.__stackPanel.update()

    def changeBase(self, newBase) :
        for widget in self.winfo_children() :
            #Destroy all widgets in self, without destroying self
            widget.destroy()
        self.__stack.clear()
        self.__initialise(newBase)
    
    def __onClearAllButtonClick(self):
        #clear the stack
        self.__stack.clear()
        self.__iopanel.set("")
        self.__stackPanel.update()
        self.__iopanel.reset()
    
if __name__ == "__main__" :
     calculator = Calculator( None )
     calculator.mainloop( )
