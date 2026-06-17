import tkinter 
import tkinter.ttk
import sys

def terminate():
    print("exiting the app")
    sys.exit(0)

root_window = tkinter.Tk()
root_window.title("Test Window")

master_frame = tkinter.ttk.Frame(root_window,padding = "3 3 12 12")
master_frame.grid(row = 0,column=0,sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))
B = tkinter.Button(master_frame)
B.configure(text="EXIT_BUTTON",command=terminate)
B.grid(row = 0,column =0)

root_window.mainloop();

