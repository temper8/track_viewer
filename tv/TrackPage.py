import tkinter as tk
import tkinter.ttk as ttk

from tv.KmlTrack import KmlTrack
from tv.TrackPlot import TrackPlot

class TrackPage(ttk.Frame):
    def __init__(self, master, track:KmlTrack= None) -> None:
        super().__init__(master)        
        label = ttk.Label(self, text=f'Name: {track.name} Author:{track.author}' )
        label.grid(row=0, column=0, sticky=tk.W, pady=4, padx=4)
        #df = pd.DataFrame(data = zip(track.whens, track.lon, track.lat, track.alt), columns=['time', 'lon', 'lat', 'alt'])
        #print(df)
        plot = TrackPlot(self, track )
        plot.grid(row=1, column=0, sticky=tk.W, pady=4, padx=4)