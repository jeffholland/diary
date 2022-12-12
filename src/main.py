import tkinter as tk

from colors import *
from constants import HEIGHT, WIDTH
from entries import Entries
from input import Input
from settings import Settings

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=0)

        load_colors()
        
        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.top_frame_height = (HEIGHT // 3) * 2

        self.top_frame = Entries(
            width=WIDTH, 
            height=self.top_frame_height,
            master=self)
        self.top_frame.grid_propagate(0)
        self.top_frame.grid(row=0, column=0)

        self.bottom_frame_height = HEIGHT // 3

        self.bottom_frame = Input(
            width=WIDTH,
            height=self.bottom_frame_height,
            master=self
        )
        self.bottom_frame.grid_propagate(0)
        self.bottom_frame.grid(row=1, column=0)

        self.settings_frame = Settings(self, width=WIDTH, height=HEIGHT)
        self.settings_frame.grid_propagate(0)

    def refresh_entries(self):
        self.top_frame.refresh_entries()

    def refresh_colors(self):
        self.colors = get_colors()

        self.top_frame.configure(bg=self.colors["HL1"])
        self.bottom_frame.configure(bg=self.colors["BG2"])
        self.settings_frame.configure(bg=self.colors["BG1"])

        self.top_frame.refresh_colors()
        self.bottom_frame.refresh_colors()
        self.settings_frame.refresh_colors()

    def show_settings(self):
        self.top_frame.grid_remove()
        self.bottom_frame.grid_remove()

        self.settings_frame.grid(row=0, column=0)

    def hide_settings(self):
        self.settings_frame.grid_remove()

        self.top_frame.grid()
        self.bottom_frame.grid()
        


app = Application()
app.master.title("Diary")
app.master.geometry(str(WIDTH) + "x" + str(HEIGHT))
app.mainloop()