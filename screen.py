from tkinter import *
from function import Function


class Screen:
    def __init__(self):
        self.screen = Tk()

        self.function = Function()

        self.start = True

        self.menubar = Menu(self.screen, tearoff=0)

        self.name_Label = Label(self.screen, text=self.function.config["Start_prompt"],
                                font=("微软雅黑", self.function.config["word_size"], 'bold'),
                                bg=self.function.config["bg_color"], fg=self.function.config["word_color"])

    def menu(self):
        def show_menu(event):
            self.menubar.post(event.x_root, event.y_root)

        self.menubar.add_cascade(label="关闭", command=self.function.close, background="black", foreground="white")
        self.menubar.add_cascade(label="设置", command=self.function.setting, background="black", foreground="white")

        self.screen.bind("<Button-3>", show_menu)

    def render(self):
        self.name_Label.pack(anchor='center', fill='both', expand=True)

    def style(self):
        self.screen.geometry("%sx%s+%s+%s" % (self.screen.winfo_screenwidth(),
                                              200, int((self.screen.winfo_screenwidth() -
                                                        self.screen.winfo_screenwidth()) / 2),
                                              int((self.screen.winfo_screenheight() - 200) / 2)))
        self.screen.resizable(False, False)
        self.screen.attributes("-alpha", self.function.config["alpha"])
        self.screen.attributes("-topmost", True)
        self.screen.overrideredirect(True)
        self.screen.configure(bg=self.function.config["bg_color"])
        self.screen.title(self.function.config["title"])

    def run(self):
        self.style()
        self.menu()
        self.render()

        self.screen.mainloop()
