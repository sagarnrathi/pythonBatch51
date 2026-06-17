from tkinter import *
from tkinter import ttk

def button_handler():
    print("Hello")

def main():
    root_window = Tk()
    root_window.title("feet to meter conversion")
    master_frame = ttk.Frame(root_window,padding="3 3 12 12")
    master_frame.grid(column=0,row=0,sticky=(N,W,S,E))

    root_window.columnconfigure(0,weight=1)
    root_window.rowconfigure(0,weight=1)

    B = ttk.Button(master_frame,)
    B.configure(text='Hello',command=button_handler)
    B.grid(row =10 ,column =10,padx=250,pady=25)
    root_window.mainloop()

main()