from tkinter import ROUND
from tkinter.colorchooser import askcolor

is_drawing = False
drawing_color = "black"
line_width = 2

def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y

def draw(event, canvas):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(
            prev_x, prev_y, current_x, current_y, 
            fill = drawing_color, width = line_width,
            capstyle = ROUND, joinstyle = ROUND,
            smooth = True)
        prev_x, prev_y = current_x, current_y
        
def stop_drawing(_):
    global is_drawing
    is_drawing = False

def change_drawing_color():
    global drawing_color
    color = askcolor(initialcolor = drawing_color)[1]
    if color:
        drawing_color = color

def change_line_width(value):
    global line_width
    line_width = int(value)
