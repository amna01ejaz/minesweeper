from tkinter import Button, Label
import settings

class Cell:
    all = []
    cell_count_label_object = None # New attribute to hold the label

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False # Track if cell is already clicked
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    
    def show_cell(self):
        if not self.is_opened:
            # Modification: Decrement the count and update the UI
            settings.CELL_COUNT -= 1
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {settings.CELL_COUNT}"
                )
            self.is_opened = True
            self.cell_btn_object.configure(bg='SystemButtonFace') # Change color when opened