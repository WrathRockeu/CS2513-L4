from tkinter import *
from ProgramConstants import TEAROFF, RESIZABLE_X, RESIZABLE_Y

class HelpMenu(Menu):
    #Class for creating the Help dropdown menu

    #Filename for the instructions file
    __INSTRUCTIONS_FILE = "instr.txt"
    #Filename for the about file
    __ABOUT_FILE = "about.txt"
    
    #Instructions Label
    __INSTRUCTIONS_LABEL = "Instructions"
    #About Label
    __ABOUT_LABEL = "About"
    #Button text
    __BUTTON_TEXT = "Close"

    
    def __init__(self,master):
        #Create the 'Help' drop down menu.
        Menu.__init__(self,master=master,tearoff=TEAROFF)
        self.__addButtons()

    def __addButtons(self):
        #Creates the buttons used for the drop down menu.
        instructionsLabel = HelpMenu.__INSTRUCTIONS_LABEL
        aboutLabel = HelpMenu.__ABOUT_LABEL
        self.add_command(label=instructionsLabel,command=self.__instructions)
        self.add_command(label=aboutLabel,command=self.__about)

    def __instructions(self):
        #Display a window of instructions for the program
        #Create the window
        self.__info = Tk()
        self.__info.resizable(RESIZABLE_X,RESIZABLE_Y)
        title = HelpMenu.__INSTRUCTIONS_LABEL
        self.__info.title(title)

        #Get and display the text from the __INSTRUCTIONS_FILE
        filename = HelpMenu.__INSTRUCTIONS_FILE
        text=self.__getText(filename)
        msg = Message(self.__info,text=text)
        msg.pack()

        #Create a button to close the window
        buttonText = HelpMenu.__BUTTON_TEXT
        button = Button(self.__info,text=buttonText,
                        command=self.__info.destroy)
        button.pack()

    def __about(self):
        #Display a window about the program
        #Create the window
        self.__about = Tk()
        self.__about.resizable(RESIZABLE_X,RESIZABLE_Y)
        title = HelpMenu.__ABOUT_LABEL
        self.__about.title(title)
        
        #Get and display the text from the __ABOUT_FILE
        filename = HelpMenu.__ABOUT_FILE
        text = self.__getText(filename)
        about = Message(self.__about,text=text)
        about.pack()

        #Create a button to close the window
        buttonText = HelpMenu.__BUTTON_TEXT
        button = Button(self.__about,text=buttonText,
                        command=self.__about.destroy)
        button.pack()

    def __getText(self,filename):
        #Opens the file 'filename' and returns it as a string.
        filehandle = open(filename,"r")
        return filehandle.read()
