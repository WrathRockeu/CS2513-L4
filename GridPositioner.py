from tkinter import *

# Utility class for adding widgets to their master's grid layout.
class GridPositioner :

    #Sticky placement for widgets
    __STICKY = "EW"

    # Main constructor:
    #  @row@: The row relative to which the widgets get placed.
    #  @col@: The column relative to which the widgets get placed.
    #  @columns@: The number of columns per row.
    def __init__( self, row, col, columns ) :
         self.__row = row
         self.__col = col
         self.__addedWidgets = 0
         self.__columns = columns

    # Add a widget to the target grid layout.
    #  @widget@ is the widget that gets added.
    def add( self, widget ) :
        widgets = self.__addedWidgets
        columns = self.__columns
        sticky = GridPositioner.__STICKY
        # Determine row and column in target grid layout.
        row = self.__row + widgets // columns
        col = self.__col + widgets %  columns
        # Place the widget
        widget.grid( row=row, column=col, sticky=sticky )
        # Adjust number of widgets placed by this object.
        self.__addedWidgets += 1

    @property
    def addedWidgets(self) :
        #Getter for the number of widgets added
        #Used for the Base panel's row calculation
        return self.__addedWidgets
