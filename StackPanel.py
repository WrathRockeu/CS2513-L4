from tkinter import *
class StackPanel(PanedWindow):
    #title of the stack field
    __TITLE = "Stack"
    __STACK_WIDTH = 20
    __ANCHOR = "s"
    def __init__(self,master,width,height,stack,title=__TITLE):
        self.__stack = stack
        PanedWindow.__init__(self,master=master,orient=VERTICAL)
        self.__var = self.__initialiseStackView(title,width,height)

    def __initialiseStackView(self,title,width,height):
        frame = LabelFrame(self,text=title,width=width,height=height)
        self.add(frame)
        var = StringVar()
        var.set("")
        label = Label(frame, width=StackPanel.__STACK_WIDTH,
                      textvariable=var,anchor=StackPanel.__ANCHOR)
        label.pack(fill=BOTH,expand=True)
        return var
       
    def update(self):
        self.__var.set(str(self.__stack))
