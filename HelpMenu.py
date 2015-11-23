from tkinter import *
class HelpMenu(Menu):
    __INSTR_FILE = "instr.txt"
    __ABOUT_FILE = "about.txt"
    def __init__(self,master):
        Menu.__init__(self,master=master)
        self.config(tearoff=0)
        self.__AddCommands()

    def __AddCommands(self):
        self.add_command(label="Instructions",command=self.__Ins)
        self.add_command(label="About",command=self.__Info)

    def __Ins(self):
        self.__info = Tk()
        self.__info.resizable(0,0)
        self.__info.title("Instructions")
        msg = Message(self.__info,text=self.__openfile(HelpMenu.__INSTR_FILE))
        msg.pack()
        button = Button(self.__info,text="Back",command=self.__info.destroy)
        button.pack()

    def __Info(self):
        self.__about = Tk()
        self.__about.resizable(0,0)
        self.__about.title("About")
        msg = Message(self.__about,text=self.__openfile(HelpMenu.__ABOUT_FILE))
        msg.pack()
        button = Button(self.__about,text="Back",command=self.__about.destroy)
        button.pack()

    def __openfile(self,filename):
        filehandle = open(filename,"r")
        return filehandle.read()
