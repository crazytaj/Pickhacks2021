import tkinter as tk
from tkinter import ttk
import keyboard
import time

def press(src):

    keyboard.start_recording()
    time.sleep(1)
    gen = keyboard.stop_recording()

    bind = str(list(keyboard.get_typed_strings(gen)))[2].lower()

    if bind == "'":
        bind = None
        pass
    else:
        keyboard.remap_key(src, bind)
    return bind