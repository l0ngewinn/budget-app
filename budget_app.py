import budget

from tkinter import *

root = Tk()

root.title('Budget for Broke Bitches')
budget_button = Button(root, text='Add Budget')
budget_button.pack(side='top')
canvas = Canvas(root, width=800, height=600, bg='white')
canvas.pack(side='bottom')

root.mainloop()