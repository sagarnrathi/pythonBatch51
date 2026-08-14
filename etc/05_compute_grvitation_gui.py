from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

default_msg="the output will be diplayed here"

def do_complete():
    try :
        m1 = float(m1_str_var.get())
        m2 = float(m2_str_var.get())
        r = float(r_str_var.get())
        if m1 <= 0.0 or m2 <= 0.0 or r<=0.0:
            raise ValueError("mass and distance must be +ve values") ;
        G = 6.67 *(10 ** -11) 
        F = (G * m1 * m2)/ (r**2)


