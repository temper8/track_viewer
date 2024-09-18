import tkinter as tk
import tkinter.ttk as ttk

class EmptyPage(ttk.Frame):
    def __init__(self, master, model=None) -> None:
        super().__init__(master)        
        label = ttk.Label(self, text='Empty Page')
        label.grid(row=0, column=0, sticky=tk.W, pady=4, padx=4)

