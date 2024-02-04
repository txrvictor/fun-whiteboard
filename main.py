#!/usr/bin/env python3

import whiteboard as wb

def main():
    try:
        import tkinter as tk
    except:
        exit("Must install tkinter for your OS")

    root = tk.Tk()
    root.title("Fun Whiteboard")
    root.geometry("800x600")

    controls_frame = tk.Frame(root)
    controls_frame.pack(side = tk.LEFT, fill = tk.Y)

    canvas = tk.Canvas(root, bg = "white")
    canvas.pack(fill = tk.BOTH, expand = True)

    whiteboard = wb.Whiteboard(canvas)

    canvas.bind("<Button-1>", whiteboard.start_drawing)
    canvas.bind("<B1-Motion>", whiteboard.draw)
    canvas.bind("<ButtonRelease-1>", whiteboard.stop_drawing)

    bgcolor_button = tk.Button(
            controls_frame, text = "Canvas Color", 
            command = whiteboard.change_canvas_color)
    bgcolor_button.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5)

    color_button = tk.Button(
            controls_frame, text = "Line Color", 
            command = whiteboard.change_drawing_color)
    color_button.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5)

    line_width_label = tk.Label(controls_frame, text = "Line Width:")
    line_width_label.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 0)

    line_width_slider = tk.Scale(
            controls_frame, from_ = 1, to = 10,
            orient = tk.HORIZONTAL, command = lambda val: whiteboard.change_line_width(val))
    line_width_slider.set(whiteboard.line_width)
    line_width_slider.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 0)

    clear_button = tk.Button(
            controls_frame, text = "Clear Canvas",
            fg = "white", bg = "#F44336",
            activeforeground = "white", activebackground = "#f6685e",
            command = lambda: canvas.delete("all"))
    clear_button.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5)

    color_button = tk.Button(
            controls_frame, text = "Save JPG", 
            fg = "white", bg = "#5b5b5b",
            activeforeground = "white", activebackground = "#787878",
            command = whiteboard.save_image)
    color_button.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5)

    root.mainloop()

if __name__ == "__main__":
    main()
