from tkinter import *
from IOPanel import *
from Digit import *
from GridPositioner import *
from Stack import *
from Operation import *
from StackPanel import *
from BaseMenu import *
from HelpMenu import *
from math import ceil
from ProgramConstants import OPERATORS, \
     CLEAR_STACK_DEFAULT, DISPLAY_STACK_DEFAULT
from OptionsMenu import *

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
    #The title of the Base selection menu
    __BASE_MENU_TITLE = 'Base'
    #The title of the Help menu
    __HELP_MENU_TITLE = 'Help'
    #The title of the Options Menu
    __OPTIONS_MENU_TITLE = "Options"

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
    #The operator for Clear Everything button
    __CLEAR_EVERYTHING_TITLE = 'CE'
    #Sticky for the stack panel
    __STACK_STICKY = 'NS'
    #String for recognising errors from operations
    __ERROR_TAG = 'Error'
    
    # Main constructor.
    #  @parent@: The master widget of this @Calculator@ or @None@
    #  @base@: The number base for this @Calculator@.
    def __init__( self, master, title=__TITLE, base=__BASE) :
        self.__base = base
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
        self.__initialise( base=base)
        
    # Utility method for initialising this @Calculator@'s components.
    #  @base@: the number base of this @Calculator@'s operations.
    def __initialise( self, base,clearOption=CLEAR_STACK_DEFAULT,
                      displayOption=DISPLAY_STACK_DEFAULT) :
        self.__clearStack = clearOption
        self.__displayStack = displayOption
        # Initialise the IO panel component.
        self.__initialiseIOPanel( )
        # Initialise the digit panel component.
        self.__initialiseDigitPanel( base=base)
        #Initialise the operand panel component
        self.__initialiseOperandPanel()
        #Initialise the menu bar
        self.__initialiseMenu()
        #Add the Base Change dropdown
        self.__initialiseBaseMenu(base)
        #Add the Options dropdown
        self.__initialiseOptionsMenu()
        #Add the Help dropdown
        self.__initialiseHelpMenu()
        #Initialise the stack display panel, if the option is selected
        if self.__displayStack:
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
        operators = OPERATORS
        for operand in operators:
            command = lambda operand=operand:self.__onOperandButtonClick(
                operand)
            self.__addSpecialDigitPanelButton(operand,
            command)
        #Add the Clear Everything Button
        title = Calculator.__CLEAR_EVERYTHING_TITLE
        self.__addSpecialDigitPanelButton(title,
                                    self.__onClearEverythingButtonClick)
                
    def __initialiseMenu(self):
        #Initialises the menu bar
        self.__menu = Menu(self)
        self.config(menu=self.__menu)
        
    def __initialiseBaseMenu(self, base) :
        #Create the dropdown for selecting the base and add it to the
        #menu
        baseDropDown = BaseMenu(self, base)
        label = Calculator.__BASE_MENU_TITLE
        self.__menu.add_cascade(label=label, menu=baseDropDown)

    def __initialiseOptionsMenu(self):
        self.__options = OptionMenu(self,
                                self.__clearStack, self.__displayStack)
        label = Calculator.__OPTIONS_MENU_TITLE
        self.__menu.add_cascade(label=label, menu=self.__options)    

    def __initialiseHelpMenu(self):
        #Initialises the panel for giving help options. ie. instructions
        helpMenu = HelpMenu(self)
        label = Calculator.__HELP_MENU_TITLE
        self.__menu.add_cascade(label=label,menu=helpMenu)

    def __initialiseStackPanel(self):
        #Initialises the side panel that displays the current stack.
        height = Calculator.__IO_PANEL_HEIGHT
        width = Calculator.__IO_PANEL_WIDTH
        self.__stackPanel = StackPanel(master=self,height=height,width=width,
                                       stack=self.__stack)
        self.__showStack()

    def __showStack(self) :
        #A method for adding the stack panel to the window
        #This gets the last row used in the window
        rows = ceil(self.__positioner.addedWidgets /
               Calculator.__DIGITS_PER_ROW) + 1
        sticky = Calculator.__STACK_STICKY
        row = Calculator.__IO_PANEL_ROW
        col = Calculator.__DIGITS_PER_ROW + 1 #Next to the rest of the stuff
        self.__stackPanel.grid(row=row, column=col,
                               rowspan=rows, sticky=sticky)
        self.__stackPanel.update()

    def __hideStack(self) :
        #A method for hiding the stack panel
        self.__stackPanel.grid_forget()

    def onStackDisplayChange(self) :
        #A method for handling when the user changes the display stack option
        displayStack = self.__options.displayStack.get()
        if displayStack :
            #The stack is hidden, we need to add it back to view
            self.__showStack()
        else :
            #The stack is already visible, hide it
            self.__hideStack()
    
    # Callback method for push button
    def __onPushButtonClick( self ) :
        self.__pushInput()

    def __pushInput(self) :
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
        self.__pushInput()
        #Run the apply function, then display the answer
        answer = self.__operation.apply(operand,self.__base)
        if answer != None :
            #We don't want to display None in the output field
            self.__iopanel.set(answer)
            if Calculator.__ERROR_TAG in answer :
                #If the last operation gave us an error,
                #we want to remove it from the stack
                self.__stack.pop()
        self.__stackPanel.update()

    def changeBase(self, newBase) :
        #Changes between the given bases
        self.__removeAllChildren()
        clearStack = self.__options.clearStack.get()
        displayStack = self.__options.displayStack.get()
        self.__stack.clear() if clearStack else self.__operation.convertStack(
            self.__stack,newBase,self.__base)
        self.__initialise(newBase,clearStack,displayStack)

    def __removeAllChildren(self) :
        #Removes all the children from self
        for widget in self.winfo_children() :
            #Destroy all widgets in self, without destroying self
            widget.destroy()
    
    def __onClearEverythingButtonClick(self):
        #clear the stack
        self.__stack.clear()
        self.__iopanel.set("")
        self.__stackPanel.update()
        self.__iopanel.reset()
    
if __name__ == "__main__" :
     calculator = Calculator( None )
     calculator.mainloop( )
