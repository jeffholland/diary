import json
from os import scandir


class Colors:
    def __init__(self, master):
        self.master = master

        self.color_scheme_index = 0

        self.color_schemes = []

        self.colors = []

        self.load_colors()

    def load_colors(self, refresh=True):
        if refresh:
            self.color_schemes.clear()

            with scandir("json/color_schemes/") as entries:
                for entry in entries:
                    if entry.name[-5:] == ".json":
                        self.color_schemes.append(entry.name[:-5])
            
            self.color_schemes.sort()

            scheme_name = ""

            with open("json/settings.json") as f:
                settings = json.load(f)

                scheme_name = settings["default_color_scheme"]

        else:
            scheme_name = self.color_schemes[self.color_scheme_index]

        filepath = f"json/color_schemes/{scheme_name}.json"

        with open(filepath, 'r') as f:
            self.colors = json.load(f)


    def get_colors(self):
        return self.colors


    def get_color_schemes(self):
        self.load_colors()
        return self.color_schemes


    def get_current_color_scheme(self):
        return self.color_schemes[self.color_scheme_index]


    def switch_color_scheme(self, dir="right"):

        if (dir == "left"):
            if self.color_scheme_index <= 0:
                self.color_scheme_index = len(self.color_schemes) - 1
            else:
                self.color_scheme_index -= 1
        else:
            if self.color_scheme_index >= len(self.color_schemes) - 1:
                self.color_scheme_index = 0
            else:
                self.color_scheme_index += 1
        
        self.load_colors(refresh=False)

    def set_color_scheme(self, name):

        index = self.color_schemes.index(name)
        
        if index >= 0 and index < len(self.color_schemes):
            self.color_scheme_index = index

            self.load_colors()

    def new_color_scheme(self, scheme, name="new_scheme"):
        filepath = f"json/color_schemes/{name}.json"

        with open(filepath, "w") as f:
            json.dump(scheme, f)