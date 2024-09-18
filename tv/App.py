import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from functools import partial

from tv.EmptyPage import EmptyPage
from tv.TrackPage import TrackPage
import tv.WorkSpace as WorkSpace
from tv.ContentFrame import ContentFrame
import tv.SideBar as SideBar


def run():
    app = App()
    app.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Track Viewer")
        self.minsize(1300, 630)        

           
        # first paned window
        main_panel = tk.PanedWindow(self, background='#C0DCF3')  
        main_panel.pack(fill=tk.BOTH, expand=1) 

        # second paned window
        left_panel = tk.PanedWindow(main_panel, orient=tk.VERTICAL)  
        main_panel.add(left_panel)  

        rack_frame = SideBar.construct(left_panel, self.on_select_item)
        left_panel.add(rack_frame)

        self.content_frame = ContentFrame(main_panel)
        main_panel.add(self.content_frame)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def on_select_item(self, action):
        print(action)
        track = WorkSpace.load_file(action['payload'])
        if track:
            page = TrackPage(self.content_frame, track) 
            self.content_frame.set_content(page)
        else:
            page = EmptyPage(self.content_frame) 
            self.content_frame.set_content(page)         

    def open_work_space_dialog(self):
        dir = tk.filedialog.askdirectory()
        if len(dir)>0:
            self.open_work_space(dir)
        #self.v.set('xxx')

    def open_work_space(self, path):
        pass

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            

    def show_about(self):
        messagebox.showinfo("Tack Viewer", "version x.y.z")


