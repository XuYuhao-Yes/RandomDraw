from tkinter import *
import sys
import random
import threading
import time


class Screen:
    def __init__(self):
        self.screen = Tk()

        self.start = True

    def style(self):
        self.screen.geometry("%sx%s+%s+%s" % (self.screen.winfo_screenwidth(),
                                              200, int((self.screen.winfo_screenwidth() -
                                                        self.screen.winfo_screenwidth()) / 2),
                                              int((self.screen.winfo_screenheight() - 200) / 2)))
        self.screen.resizable(False, False)
        self.screen.attributes("-alpha", 0.7)
        self.screen.attributes("-topmost", True)
        self.screen.overrideredirect(True)
        self.screen.configure(bg="black")
        self.screen.title("RandomDraw")

    def run(self):
        self.style()

        self.screen.mainloop()
