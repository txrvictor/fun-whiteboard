import tkinter as tk
import whiteboard as wb

def main():
    root = tk.Tk()
    root.title("Fun Whiteboard")
    root.geometry("800x600")

    canvas = tk.Canvas(root, bg = "white")
    canvas.pack(fill = tk.BOTH, expand = True)

    controls_frame = tk.Frame(root)
    controls_frame.pack(side = tk.TOP, fill = tk.X)

    color_button = tk.Button(
            controls_frame, text = "Change Color", 
            command = wb.change_drawing_color)
    color_button.pack(side = tk.LEFT, padx = 5, pady = 5)

    clear_button = tk.Button(
            controls_frame, text = "Clear Canvas",
            command = lambda: canvas.delete("all"))
    clear_button.pack(side = tk.LEFT, padx = 5, pady = 5)

    line_width_label = tk.Label(controls_frame, text = "Line Width:")
    line_width_label.pack(side = tk.LEFT, padx = 5, pady = 5)

    line_width_slider = tk.Scale(
            controls_frame, from_ = 1, to = 10,
            orient = tk.HORIZONTAL, command = lambda val: wb.change_line_width(val))
    line_width_slider.set(wb.line_width)
    line_width_slider.pack(side = tk.LEFT, padx = 5, pady = 5)

    def draw_on_canvas(event):
        wb.draw(event, canvas)

    canvas.bind("<Button-1>", wb.start_drawing)
    canvas.bind("<B1-Motion>", draw_on_canvas)
    canvas.bind("<ButtonRelease-1>", wb.stop_drawing)

    root.mainloop()

if __name__ == "__main__":
    main()
