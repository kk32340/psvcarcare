from tkinter import *
#print("test app")
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self , master)
        self.master=master
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.mainloop()
