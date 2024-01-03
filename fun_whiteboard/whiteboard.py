import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

from tkinter.colorchooser import askcolor

def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y

def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(
            prev_x, prev_y, current_x, current_y, 
            fill = drawing_color, width = line_width,
            capstyle = tk.ROUND, joinstyle = tk.ROUND,
            smooth = True)
        prev_x, prev_y = current_x, current_y
        
def stop_drawing(event):
    global is_drawing
    is_drawing = False

def change_drawing_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

def change_line_width(value):
    global line_width
    line_width = int(value)

root = tk.Tk()
root.title("Fun Whiteboard")
root.geometry("800x600")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

is_drawing = False
drawing_color = "black"
line_width = 2

controls_frame = tk.Frame(root)
controls_frame.pack(side = tk.TOP, fill = tk.X)

color_button = tk.Button(
    controls_frame, text = "Change Color", 
    command = change_drawing_color)
color_button.pack(side = tk.LEFT, padx = 5, pady = 5)

clear_button = tk.Button(
    controls_frame, text = "Clear Canvas",
    command = lambda: canvas.delete("all"))
clear_button.pack(side = tk.LEFT, padx = 5, pady = 5)

line_width_label = tk.Label(controls_frame, text = "Line Width:")
line_width_label.pack(side = tk.LEFT, padx = 5, pady = 5)

line_width_slider = tk.Scale(
    controls_frame, from_ = 1, to = 10,
    orient = tk.HORIZONTAL, command = lambda val: change_line_width(val))
line_width_slider.set(line_width)
line_width_slider.pack(side = tk.LEFT, padx = 5, pady = 5)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()
