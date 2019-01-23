"""
Provides convenient tkinter app widgets for viewing
and editing and creating drawings. 
"""

import sys
if sys.platform.startswith("2"):
    import tkinter as tk
else:
    import tkinter as tk

from .canvas import Canvas


#######


class AggCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.drawer = Canvas(width=kwargs["width"],
                             height=kwargs["height"],
                             background=kwargs["bg"])

    def draw_rectangle(self):
        pass

    def draw_polygon(self):
        pass
