from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Settings for the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper OOP Project")
root.resizable(False, False)
root.configure(bg="black")

# Create UI Frames (Top, Left, and Center)
top_frame = Frame(root, bg='black', width=settings.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0, y=0)

center_frame = Frame(root, bg='black', width=utils.width_prct(75), height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# Create the Grid of Cells
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Run the window
root.mainloop()