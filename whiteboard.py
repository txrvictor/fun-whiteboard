from tkinter import filedialog, ROUND
from tkinter.colorchooser import askcolor
from PIL import ImageGrab

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

    def change_canvas_color(self):
        latest_canvas_color = self.canvas.config('bg')[-1]
        color = askcolor(initialcolor = latest_canvas_color if latest_canvas_color else 'white')[1]
        if color:
            self.canvas.configure(bg=color)
    
    def save_image(self):
        self.canvas.update()
        self.canvas.focus()

        x0 = self.canvas.winfo_rootx()
        y0 = self.canvas.winfo_rooty()
        x1 = x0 + self.canvas.winfo_width()
        y1 = y0 + self.canvas.winfo_height()

        img = ImageGrab.grab((x0, y0, x1, y1))
        
        # only save after grabbing the image, otherwise it will screen capture
        # the filedialog window or anything over the canvas as well
        filename = filedialog.asksaveasfile(mode = 'w', defaultextension = ".jpg")
        if not filename:
            return

        img.save(filename)
