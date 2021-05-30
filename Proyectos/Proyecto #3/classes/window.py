import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("App")

if __name__ == "__main__":
    app = App()
    app.mainloop()