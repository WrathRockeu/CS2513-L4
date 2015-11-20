from tkinter import *

# Class for representing a digit button on a calculator.
class Digit( Button ) :

    # Main constructor.
    # The @master@ parameter is the widgit that the current digit
    # button is on; @digit@ is the digit on the button, and
    # @appendee@ should reference the object that represent the
    # input field of the caluclator: it should provide an instance
    # method called @append( )@.
    def __init__( self, master, digit, appendee ) :
       # Call the constructor of the @Button@ class, making sure
       # the button calls the @__onButtonClick( )@ method when
       # the button is clicked.
       Button.__init__( self, master=master, text=str( digit ),
                        command=self.__onButtonClick )
       # initialise this objects state
       self.__appendee = appendee
       self.__digit = digit

    # Callback method, which should be carried out when the button
    # is clicked.
    def __onButtonClick( self ) :
       # Append current button's digit to output field of @self.__appendee@.
       #IFF there is less than 20 digits in the box already
       if len(self.__appendee.get()) < 20 :
           self.__appendee.append( str( self.__digit ) )
