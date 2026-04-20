from tkinter import Button
import settings

class Cell:
    all = [] # Class attribute: Stores all instances of Cell

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # Add every new object to the list upon creation
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}" # Placeholder text
        )
        # Binding events is key to interaction
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        # Logic: What happens when you click?
        if self.is_mine:
            print("BOOM! Game Over")
        else:
            print(f"Cell {self.x},{self.y} is safe.")

    def right_click_actions(self, event):
        # Logic: Flagging a suspected mine
        print("Flagged!")