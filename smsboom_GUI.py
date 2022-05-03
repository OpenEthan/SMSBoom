from tkinter import Tk, StringVar
from tkinter import ttk


class InputWidget(ttk.Frame):
    """输入框,确认框"""

    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.phone = StringVar()
        self.createWidget()

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.pack()

    def createWidget(self):
        """InputWidget"""
        ttk.Label(self, text="手机号:").grid(column=0, row=0, sticky='nsew')
        ttk.Entry(self, textvariable=self.phone).grid(
            column=1, row=0, columnspan=3, sticky='nsew')
        ttk.Button(self, text="启动轰炸").grid(
            column=4, row=0, sticky='nsew')


class Application(ttk.Frame):
    """APP main frame"""

    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        # 伸缩
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.createWidget()
        # 间隔
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.pack()

    def createWidget(self):
        """Widget"""
        input_wiget = InputWidget(self)


if __name__ == "__main__":
    root = Tk()
    root.title("SMSBoom - 短信轰炸机 ©落落")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Application(parent=root)
    root.mainloop()
