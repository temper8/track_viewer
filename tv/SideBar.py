import tkinter as tk
import tkinter.ttk as ttk



def construct(master, app):
    rf = SideBar(master, app)
    #ListView(rf, f, command= rf.on_select_item).pack(expand=1, fill=tk.BOTH, padx=(10,0), pady=(5,5))

    ttk.Separator(rf, orient='horizontal').pack(fill='x')

    ttk.Radiobutton(rf, text="Run ", variable= rf.v, value="imped", width=25, 
                    style = 'Toolbutton').pack(expand=0, fill=tk.X)

    return rf

class SideBar(ttk.Frame):
    def __init__(self, master, app) -> None:
        super().__init__(master)
        self.app = app
        self.on_select = None
        self.active_view = None
        self.v = tk.StringVar(self, "xxx")  # initialize