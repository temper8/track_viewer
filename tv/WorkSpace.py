import os
import json
import tkinter as tk
from pathlib import Path

from tv.KmlTrack import KmlTrack

_location = Path('workspace')

def open(path: None):
    if path:
        _location= path

def get_file_list():
    if _location.exists():
        print(f"exists{_location}")
        return [p.name  for p in _location.glob('*.*') if p.name !='.gitignore']
   
    else:
        return []

def simple_read(path):
    try:
        with path.open(mode= "r", encoding='utf-8') as file:
            data = file.read()
            #print(data)
            return data
    except Exception as e :
        print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: \n{e}")            
        return None


def print_child_features(element, depth=0):
    """Prints the name of every child node of the given element, recursively."""
    print("{}, {}".format(element.name, element.description))
    if not getattr(element, "features", None):
        return
    for feature in element.features:
        print("  " * depth + feature.name)
        print_child_features(feature, depth + 1)


import pandas as pd
  

def load_file(file_name):
    loc = _location.joinpath(file_name)
    if loc.exists():
        match loc.suffix:
            case '.kml':
                track =  KmlTrack(simple_read(loc))
                df = pd.DataFrame(data = zip(track.whens, track.lon, track.lat, track.alt), columns=['time', 'lon', 'lat', 'alt'])
                print(df)
            case _:
                simple_read(loc)


