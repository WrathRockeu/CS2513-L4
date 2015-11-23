from tkinter import *
class OptionMenu(Menu):
    def __init__(self,master):
        Menu.__init__(self,master=master)
        self.config(tearoff=0)
        self.__addOptions()

    def __addOptions(self):
        self.CS = BooleanVar()
        self.CS.set(1)
        self.add_checkbutton(label="Clear Stack on Base Change",variable=self.CS,
                             onvalue = 1,offvalue = 0)

        """Not sure if we want this"""
        """Well, I dont really give a fuck... If I feel like it I will implement
           this
           Regards,
           Grzegorz Ikwanty"""
        self.DS = BooleanVar()
        self.DS.set(1)
        self.add_checkbutton(label="Dispaly Stack",variable=self.DS,
                             onvalue = 1,offvalue = 0)
