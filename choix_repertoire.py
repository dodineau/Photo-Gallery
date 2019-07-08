#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter.filedialog import askdirectory

def directory():
    os.chdir('/home')
    root = tk.Tk()
    root.withdraw()
    return askdirectory()
# directory

if __name__ == "__main__":
    directory()
# if
