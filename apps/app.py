from tkinter import ttk
import tkinter as tk
import os

class GuestCount(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.app_widgets()

    def app_widgets(self):
        self.header = ttk.Label(
            self,
            text="HKCCTV GUEST COUNT", padding=[10,30],
            font=['arial', 30]
        )

        self.header.pack()

if __name__ == '__main__':
   os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
   window = tk.Tk()
   window.geometry("750x500")
   window.title("GUEST COUNT HKCCTV")

   apps =  GuestCount(window)
   apps.pack()

   window.mainloop()
   