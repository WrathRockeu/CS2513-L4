from tkinter import *
class StackPanel(PanedWindow):
    #title of the stack field
    __TITLE = "Stack"
    __STACK_WIDTH = 10
    __ANCHOR = "e"
    def __init__(self,master,width,height,title=__TITLE,stack):
        self.__stack = stack
        PanedWindow,__init__(self,master=master,orient=VERTICAL)
        self.var = self.__initialiseStackView(title,width,height)

    def __initialiseStackView(title,width,height):
        frame = LabelFrame(self,title,width,height)
        self.add(frame)
        var = StringVar()
        var.set("")
        label = Label(frame,width=StackPanel.__STACK_WIDTH,
                      textvariable=var,anchor=StackPanel.__ANCHOR)
        label.pack()
        return var

    def set(self,string):
        self.var.set(string)
        

    