from tkinter import *

class Cell(Canvas):

	def __init__(self, master, color):

		pass

class Board(Frame):

	def __init__(self, master):

		pass

def play_checkers():
	root = Tk()
	root.title('Checkers')
	game = Board(root)
	root.mainloop()

play_checkers()