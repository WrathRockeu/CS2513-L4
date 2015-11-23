from tkinter import *
class HelpMenu(Menu):

    def __init__(self,master):
        Menu.__init(self,master=master)
        self.__helpMenu = Menu(self,tearoff=0)
        self.__AddCommands()

    def __AddCommands(self):
        self.__helpMenu.add_command(label="Instructions",command=self.__Ins)
        self.__helpMenu.add_command(label="About",command=self.__Info)

    def __Ins(self):
        Toplevel()

    def __Info(self):
        Toplevel()
