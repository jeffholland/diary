import tkinter as tk

from constants import *
from entry import Entry
from group_menu import GroupMenu

class Group(tk.Frame):
    def __init__(self, master, width, entry_height, entries_data, name, font):
        self.entry_height = entry_height

        tk.Frame.__init__(
            self, 
            master,
            width=width,
            height=entry_height
        )

        self.width = width
        self.height = entry_height
        self.name = name
        self.master = master
        self.font = font
        self.entries_data = entries_data

        self.show_dates = True
        self.show_times = True

        self.entries = []

        self.create_widgets()



    def create_widgets(self):

        # Group menu - contains name label and buttons

        self.group_menu = GroupMenu(
            self,
            self.name,
            len(self.entries_data)
        )
        self.group_menu.grid(
            row=0,
            column=0
        )

        # Show entries

        for count in range(len(self.entries_data)):
            try:
                checked_bool = self.entries_data[count]["checked"]
            except KeyError:
                checked_bool = False

            entry_date = None
            if self.show_dates:
                entry_date = self.entries_data[count]["date"]
            entry_time = None
            if self.show_times:
                entry_time = self.entries_data[count]["time"]

            self.entries.append(Entry(
                self,
                date=entry_date,
                time=entry_time,
                menu=True,
                text=self.entries_data[count]["text"],
                width=self.width - PADDING * 4,
                height=self.entry_height,
                index=self.entries_data[count]["index"],
                font=self.font,
                checkbox=True,
                checked=checked_bool,
                group=self.name
            ))
            self.entries[count].grid_propagate(0)
            self.entries[count].grid(
                row=count + 1, 
                column=0,
                padx=PADDING, 
                pady=PADDING,
                columnspan=2
            )
        self.calculate_height()



    def refresh_colors(self, colors):
        self.colors = colors

        self.configure(bg=self.colors["BG2"])

        for entry in self.entries:
            entry.refresh_colors(colors)

        self.group_menu.refresh_colors(colors)



    def calculate_height(self):
        self.height = 0

        for entry in self.entries:
            self.height += entry.height + PADDING * 2

        self.height += 80

        self.configure(height=self.height)

    def delete(self):
        for entry in self.entries_data:
            for master_entry in self.master.master.master.entries_data:
                try:
                    if master_entry["index"] == entry["index"]:
                        master_entry["group"] = "None"
                except KeyError:
                    if master_entry["text"] == entry["text"]:
                        master_entry["index"] = entry["index"]
                        master_entry["group"] = "None"


        self.master.master.master.group_names.remove(self.name)
        self.master.master.master.refresh_entries(refresh_data=False)