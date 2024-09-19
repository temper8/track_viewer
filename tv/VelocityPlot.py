import tkinter as tk
import tkinter.ttk as ttk

from matplotlib import cm
from matplotlib.patches import Circle, Ellipse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from tv.VerticalNavigationToolbar import VerticalNavigationToolbar2Tk
from tv.KmlTrack import KmlTrack

def circle(x,y,r):
    return Ellipse(
            xy=(x, y),
            width=r/2,
            height=r/2,
            angle=0,
            facecolor="none",
            edgecolor="b"
        )

class VelocityPlot(ttk.Frame):
    def __init__(self, master, track:KmlTrack) -> None:
        super().__init__(master)  
        self.track= track
        self.title = 'Track Plot'

        self.fig, self.axd = plt.subplot_mosaic([['left', 'right A'], ['left', 'right B'], ['left', 'right C']],
                              figsize=(14, 7), layout="constrained")
        
        #self.axd['left'].plot(track.lon, track.lat)
        X = np.array(track.lon)
        Y = np.array(track.lat)
        speed = np.array(track.speed)
        course = np.array(track.course)
        U, V = speed*np.sin(course), speed*np.cos(course)
        self.x_speed = U
        self.y_speed = V
        self.axd['left'].scatter(U, V, c='blue',  alpha=0.3, edgecolors='none')
        self.axd['left'].plot(U, V,  alpha=0.3, linewidth=0.5 )
        self.axd['left'].axis('equal')
        #Q = self.axd['left'].quiver(X, Y, U, V)

        #self.axd['left'].add_patch(circle(0,0,1.5))
        self.circ = Circle((0.0, 0.0), 0.5, facecolor="none", edgecolor="b")
        self.axd['left'].add_artist(self.circ)
        # now determine nice limits by hand:
        binwidth = 0.1
        speed_ymax = np.max(np.abs(speed))
        lim = (int(speed_ymax/binwidth) + 1) * binwidth
        self.bins = np.arange(0, lim + binwidth, binwidth)
        self.axd['right A'].hist(speed, bins=self.bins, label='speed hist')
        #self.axd['right A'].plot(track.alt, label='alt')
        self.axd['right A'].legend(loc='upper right')

        self.axd['right B'].hist(speed, bins=self.bins, label='speed hist')
        self.axd['right B'].legend(loc='upper right')

        self.axd['right C'].plot(track.speed, label='speed')
        self.speed_var, = self.axd['right C'].plot(track.speed, label='speed')
        self.axd['right C'].legend(loc='upper right')


        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        #toobar = NavigationToolbar2Tk(self.canvas, frame)
        tb = VerticalNavigationToolbar2Tk(self.canvas, self)
        tb.update()
        tb.grid(row=0, column=0, sticky=tk.N)    
        self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)        
        self.rowconfigure(0, weight=1)

        tb = self.make_toolbar()
        tb.grid(row=1, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W) 


    def make_toolbar(self):
        frame = ttk.Frame(self)
  
        self.chk_var = tk.IntVar(master = self, value=True)
  
        #self.checkbtn = ttk.Checkbutton(master=  frame, text="test", variable=self.chk_var, command=self.checkbtn_changed )
        #self.checkbtn.pack(side=tk.LEFT, expand=1, fill=tk.X, padx=5) 
        self.x_speed_var = tk.DoubleVar(master = self, value=0)
        self.x_speed_var.trace_add('write', self.on_update_value)
        self.slider_1 = tk.Scale(master=  frame, variable = self.x_speed_var, orient = tk.HORIZONTAL, 
                                    sliderlength = 20,
                                    width = 10,            
                                    label='x speed',
                                    from_= -2, 
                                    to= 2, 
                                    resolution= 0.02 )
        self.slider_1.pack(side=tk.LEFT, expand=1, fill=tk.X, padx=5) 

        self.y_speed_var = tk.DoubleVar(master = self, value=0.0)
        self.y_speed_var.trace_add('write', self.on_update_value)
        self.slider_2 = tk.Scale(master=  frame, variable = self.y_speed_var, orient = tk.HORIZONTAL,
                                    sliderlength = 20,
                                    width = 10,            
                                    label='y speed',
                                    from_=-2, 
                                    to=2, 
                                    resolution= 0.02 )
        self.slider_2.pack(side=tk.LEFT, expand=1, fill=tk.X, padx=5)   
            
        self.max_speed = tk.DoubleVar(master = self, value=1.1)
        self.max_speed.trace_add('write', self.on_update_value)
        self.slider_3 = tk.Scale(master=  frame, variable = self.max_speed, orient = tk.HORIZONTAL,
                                    sliderlength = 20,
                                    width = 10,            
                                    label='max speed',
                                    from_=0, 
                                    to=4, 
                                    resolution= 0.02 )
        self.slider_3.pack(side=tk.LEFT, expand=1, fill=tk.X, padx=5)   

        return frame
        
    def checkbtn_changed(self):
        if self.chk_var.get() == 1:
            self.уscale_log = True
        else:
            self.уscale_log = False
        self.show_series(save_lim = False) 

    def on_update_value(self, var, indx, mode):
        x_speed = self.x_speed_var.get()
        y_speed = self.y_speed_var.get()
        max_speed = self.max_speed.get()
        #x, y = speed*np.sin(course), speed*np.cos(course)
        self.circ.center = x_speed, y_speed
        self.circ.radius = max_speed
        speed = np.sqrt(np.square(x_speed)+ np.square(y_speed))
        course = np.atan2(x_speed, y_speed)
        print(f"speed= {speed} course= {course} course= {max_speed}")
        xx_speed = self.x_speed - x_speed
        yy_speed = self.y_speed - y_speed
        full_speed = np.sqrt(np.square(xx_speed)+ np.square(yy_speed))
        self.axd['right B'].clear()
        self.axd['right B'].hist(full_speed, bins=self.bins, label='speed hist')
        #self.axd['right C'].plot(full_speed, alpha=0.3, label='speed')
        self.speed_var.set_ydata(full_speed)
        self.canvas.draw()

    def update(self, series, time_stamp):
        self.fig.suptitle(f'{self.title}. Time={time_stamp}')
        self.show_series()

    def show_series(self, save_lim = True):
        if save_lim:
            bottom, top = self.ax1.get_ylim()
            left, right = self.ax1.get_xlim()        
        self.ax1.clear()
        i1 = self.index_1.get()
        i2 = i1 + self.index_2.get()
        if i2>len(self.series):
            i2 = len(self.series)
        print(f'{i1} {i2}')
        for item in self.series[i1:i2]:
            self.ax1.plot(item['X'], item['Y']);
        if self.уscale_log:
            self.ax1.set_yscale('log')
        if save_lim:
            self.ax1.set_ylim(bottom, top)
            self.ax1.set_xlim(left, right)            
        self.canvas.draw()

    def destroy(self):
        if self.fig:
            plt.close(self.fig)
        super().destroy()                   