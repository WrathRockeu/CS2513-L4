from tkinter import *

# Utility class for representing the input and output fields of a calculator.
class IOPanel( PanedWindow ) :
    # Title of input field
    __INPUT_TITLE = "Input"
    # Title of output field
    __OUTPUT_TITLE = "Output"
    # Default value for input field
    __DEFAULT_INPUT = ""
    # Default value for output field
    __DEFAULT_OUTPUT = ""

    # Number of characters we can put in the input/output field
    __WIDTH = 20
    # Anchor for the text in the input/output field
    __ANCHOR="e"

    # Basic constructor of an @IOPanel@.
    #   @master@: the widget that this @IOPanel@ is in.
    #   @width@: the width of the @IOPanel@ in pixels.
    #   @height@: the height of the @IOPanel@ in pixels.
    #   @inputTitle@: the title of the input field.
    #   @outputTitle@: the title of the output field.
    def __init__( self, master, width, height,
                  inputTitle = __INPUT_TITLE,
                  outputTitle = __OUTPUT_TITLE ) :
        # Create a paned window for input and output fields.
        PanedWindow.__init__( self, master=master, orient=VERTICAL )
        # Create the input field.
        self.__initialiseInput( title=inputTitle, width=width, height=height )
        # Create the output field.
        self.__initialiseOutput( title=outputTitle, width=width, height=height )

    # Initialise the input frame.
    def __initialiseInput( self, title, width, height ) :
        # Define the default text for the input field.
        default = IOPanel.__DEFAULT_INPUT
        # Create input field and the variable that holds the field's text.
        var = self.__initialiseIOField( title=title, width=width,
                                        height=height, default=default )
        # Create instance variable that references this field's variable.
        self.__inputVariable = var

    # Initialise the output frame.
    def __initialiseOutput( self, title, width, height ) :
        # Define the default text for the input field.
        default = IOPanel.__DEFAULT_OUTPUT
        # Create input field and the variable that holds the field's text.
        var = self.__initialiseIOField( title=title, width=width,
                                        height=height, default=default )
        # Create instance variable that references this field's variable.
        self.__outputVariable = var

    # initialise an input or output label and return the @StringVar@
    # that holds the text of the label.
    def __initialiseIOField( self, title, width, height, default ) :
        # Create a labelled frame with a text for the label
        frame = LabelFrame( self, text=title, width=width, height=height )
        # Add frame tot the current widget.
        self.add( frame )
        # Create the @StringVar@ that holds the text that's in the frame.
        variable = StringVar( )
        # Set the de
        variable.set( default )
        # Create the text label for the field and add it to the frame.
        label = Label( frame, width=IOPanel.__WIDTH, 
                       textvariable=variable, anchor=IOPanel.__ANCHOR )
        # Use pack layout manager (without this text may not appear).
        label.pack( )
        # Return the label variable.
        return variable

    # Set text of output to the string that is given by @string@.
    def set( self, string ) :
        self.__outputVariable.set( string )

    # Append text of input with the string that is given by @string@.
    def append( self, string ) :
        inputvar = self.__inputVariable
        inputvar.set( inputvar.get( ) + string )

    # Reset the input field to the default input value.
    def reset( self ) :
        self.__inputVariable.set( IOPanel.__DEFAULT_INPUT )

    # Determine the value of the text in the input field.
    def get( self ) :
        return self.__inputVariable.get( )
