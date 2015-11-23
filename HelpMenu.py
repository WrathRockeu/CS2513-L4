from tkinter import *
class HelpMenu(Menu):

    def __init__(self,master):
        Menu.__init__(self,master=master)
        self.__helpDropDown = Menu(self,tearoff=0)
        self.__AddCommands()

    def __AddCommands(self):
        self.__helpDropDown.add_command(label="Instructions",command=self.__Ins)
        self.__helpDropDown.add_command(label="About",command=self.__Info)

    def __Ins(self):
        Toplevel()

    def __Info(self):
        Toplevel()
