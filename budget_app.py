import budget

import tkinter as tk

root = tk.Tk()
root.title('Budget Planner for Broke Bitches')
open_button = tk.Button(root, text='Add budget')
open_button.pack(side='top')
canvas = tk.Canvas(root, width=800, height=400, bg='white')
canvas.pack(side='bottom')
canvas.create_text(text='Ello mate')

tk.mainloop()