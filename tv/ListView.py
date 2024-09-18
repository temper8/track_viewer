import tkinter as tk
import tkinter.ttk as ttk

class ListView(ttk.Frame):
    def __init__(self, master, content, height= 5, command= None) -> None:
        super().__init__(master)  
        self.content = content   
        
        self.on_select_item = command
        lab = ttk.Label(self, text= 'Explorer')
        lab.grid(row=0, column=0, sticky=tk.W)
        self.nodes = {}
        self.tree = ttk.Treeview(self,  selectmode="browse", show="", columns=  ( "#1"), height= height)

        self.tree.heading('#1', text='File')
        #self.tree.heading('#2', text='Comment')
        self.tree.column('#0', stretch=tk.NO)
        self.tree.column('#1', width=30)
        #self.tree.column('#2', width=35)
                    
        self.update_tree()

        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        self.tree.grid(row=1, column=0,  columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)
        ysb.grid(row=1, column=2, sticky=tk.N + tk.S)
        self.tree.bind("<<TreeviewSelect>>", self.select_node)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)        


    def selection_clear(self):
        print('explorer selection clear')
        self.tree.selection_set(())

    def update_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.nodes = {}
        for item in self.content:
            self.tree.insert('', tk.END, text=item,  values=(item,), tags=('show'))  
            #self.tree.insert('', tk.END, text=item.name,  values=(item.name, 't15 pam 25 ph0 1D',), tags=('show'))  
            
    def select_node(self, event):
        sel_id = self.tree.selection()
        #print(f"selection = {sel_id}")
        if len(sel_id)>0:
            selected_item = self.tree.item(sel_id)
            tag = selected_item["tags"][0]            
            text = selected_item['text']

            action = {
                'action': tag,
                'payload' : text
                }

            self.on_select_item(action)
