import tkinter as tk
import tkinter.font as tkFont

from constants import *

class Entry(tk.Frame):
    def __init__(self, date, time, text, width, height, bg, master=None):

        # TODO: make height dynamic according to length of text
        tk.Frame.__init__(
            self, 
            master, 
            width=width, 
            height=height, 
            bg=bg)

        self.date = date
        self.time = time
        self.text = text
        self.bg = bg

        self.font = tkFont.Font(
            family='Helvetica', 
            size=FONT_SIZE)
        self.font_bold = tkFont.Font(
            family='Helvetica', 
            size=FONT_SIZE, 
            weight="bold")

        self.create_widgets()


    def create_widgets(self):
        self.date_label = tk.Label(self, 
            text=self.date,
            font=self.font_bold)
        self.date_label.grid(
            row=0, 
            column=0, 
            sticky=tk.W)

        self.time_label = tk.Label(self, 
            text=self.time,
            font=self.font)
        self.time_label.grid(
            row=0, 
            column=2,
            sticky=tk.E)

        self.text_label = tk.Label(self, 
            text=self.text,
            bg=self.bg, 
            fg=HL_2, 
            font=self.font,
            wraplength=720)

        self.text_label.grid(
            row=1, 
            column=0, 
            padx=PADDING,
            pady=PADDING,
            columnspan=3)

        # Grid_bbox gives dimensions of Entry
        self.update()
        # print(self.grid_bbox(column=0, row=1))