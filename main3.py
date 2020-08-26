import tkinter as tk
import tkinter.ttk as ttk


class File1App:
    def __init__(self, master=None):
        # build ui
        frame_1 = ttk.Frame(master)
        frame_2 = ttk.Frame(frame_1)
        label_1 = ttk.Label(frame_2)
        label_1.config(text='Vehicle #')
        label_1.pack(side='top')
        text_1 = tk.Text(frame_2)
        text_1.config(height='10', width='50')
        _text_ = '''text_1'''
        text_1.insert('0.0', _text_)
        text_1.pack(side='top')
        message_1 = tk.Message(frame_2)
        message_1.config(text='message_1')
        message_1.pack(side='top')
        frame_2.config(height='500', relief='flat', width='500')
        frame_2.pack(side='top')
        frame_1.config(height='200', width='200')
        frame_1.pack(side='top')

        # Main widget
        self.mainwindow = frame_1


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = File1App(root)
    app.run()

