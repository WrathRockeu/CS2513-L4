from tkinter import *
class StackPanel(PanedWindow):
    
    #Title of the stack field
    __TITLE = "Stack"
    #Width of the stack space in characters
    __STACK_WIDTH = 21 #1 Additional space for the '-' sign
    #Anchor for the label
    __ANCHOR = "s"
    #Fill for the label
    __FILL = BOTH
    #Should the label expand
    __EXPAND = True
    
    def __init__(self,master,width,height,stack,title=__TITLE):
        #Constructor for the stack panel, being passed the stack to keep
        #it's own reference to the main Calculator stack
        self.__stack = stack
        PanedWindow.__init__(self,master=master,orient=VERTICAL)
        self.__var = self.__initialiseStackView(title,width,height)

    def __initialiseStackView(self,title,width,height):
        #Create a LabelFrame and a Label to display the current status of the stack
        frame = LabelFrame(self,text=title,width=width,height=height)
        self.add(frame)

        #StringVar for updating the stack display
        stackText = StringVar()
        stackText.set("")

        #The Label for actually displaying the stack
        width = StackPanel.__STACK_WIDTH
        anchor = StackPanel.__ANCHOR
        label = Label(frame, width=width, textvariable=stackText,
                      anchor=anchor)
        fill = StackPanel.__FILL
        expand = StackPanel.__EXPAND
        label.pack(fill=fill, expand=expand)
        
        #Return the StringVar so it can be manipulated later
        return stackText
       
    def update(self):
        #Update the stack display with the new state of the stack
        self.__var.set(str(self.__stack))
