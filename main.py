# ... (inside your main.py setup)
# Create the Label in the top_frame
cell_count_label = Label(
    top_frame,
    bg='black',
    fg='white',
    text=f"Cells Left: {settings.CELL_COUNT}",
    font=("", 30)
)
cell_count_label.place(x=utils.width_prct(25), y=0)

# Connect the label to the Cell class so the class can update it
Cell.cell_count_label_object = cell_count_label