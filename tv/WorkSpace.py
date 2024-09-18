import os
import json
import tkinter as tk
from pathlib import Path

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
    

def load_file(file_name):
    loc = _location.joinpath(file_name)
    if loc.exists():
        print(loc)
        try:
            with loc.open(mode= "r", encoding='utf-8') as file:
                data = file.read()
                print(data)
        except Exception as e :
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: \n{e}")            