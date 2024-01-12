from tkinter import ROUND
from tkinter.colorchooser import askcolor

class Whiteboard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.is_drawing = False
        self.drawing_color = "black"
        self.line_width = 2

    def start_drawing(self, event):
        self.is_drawing = True
        self.prev_x, self.prev_y = event.x, event.y

    def draw(self, event):
        if self.is_drawing:
            current_x, current_y = event.x, event.y
            self.canvas.create_line(
                self.prev_x, self.prev_y,
                current_x, current_y, 
                fill = self.drawing_color, width = self.line_width,
                capstyle = ROUND, joinstyle = ROUND,
                smooth = True)
            self.prev_x, self.prev_y = current_x, current_y
            
    def stop_drawing(self, _):
        self.is_drawing = False

    def change_drawing_color(self):
        color = askcolor(initialcolor = self.drawing_color)[1]
        if color:
            self.drawing_color = color

    def change_line_width(self, value):
        self.line_width = int(value)
