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