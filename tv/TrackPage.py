import tkinter as tk
import tkinter.ttk as ttk

from tv.KmlTrack import KmlTrack
from tv.TrackPlot import TrackPlot
from tv.VelocityPlot import VelocityPlot

class TrackPage(ttk.Frame):
    def __init__(self, master, track:KmlTrack= None) -> None:
        super().__init__(master)        
        label = ttk.Label(self, text=f'Name: {track.name} Author:{track.author}' )
        label.grid(row=0, column=0, sticky=tk.W, pady=4, padx=4)
        label = ttk.Label(self, text=f' len(whens): {len(track.whens)}  len(lon): {len(track.lon)}  len(lat):{len(track.lat)} len(speed):{len(track.speed)}' )
        label.grid(row=2, column=0, sticky=tk.W, pady=4, padx=4)
        #df = pd.DataFrame(data = zip(track.whens, track.lon, track.lat, track.alt), columns=['time', 'lon', 'lat', 'alt'])
        #print(df)

        nb= ttk.Notebook(self)
        tp = TrackPlot(self, track )
        nb.add(tp, text="Track", underline=0, sticky=tk.NE + tk.SW)
        vp = VelocityPlot(self, track )
        nb.add(vp, text="Velocity", underline=0, sticky=tk.NE + tk.SW)        
        nb.grid(row=3, column=0, sticky=tk.W, pady=4, padx=4)

        #plot = TrackPlot(self, track )
        #plot.grid(row=3, column=0, sticky=tk.W, pady=4, padx=4)