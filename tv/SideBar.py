import tkinter as tk
import tkinter.ttk as ttk

from tv.ListView import ListView
import tv.WorkSpace as WorkSpace




def construct(master, command, btn_command):
    sb = SideBar(master)
    content = WorkSpace.get_file_list()
    ListView(sb, content, command= command).pack(expand=1, fill=tk.BOTH, padx=(10,0), pady=(5,5))

    ttk.Separator(sb, orient='horizontal').pack(fill='x')

    ttk.Radiobutton(sb, text="refresh",  value="imped", width=30, command= btn_command,
                    style = 'Toolbutton').pack(expand=0, fill=tk.X)

    return sb

class SideBar(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.on_select = None
        self.active_view = None
        self.v = tk.StringVar(self, "xxx")  # initialize