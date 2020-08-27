from tkinter import *

f = lambda i, j : i*8 + j

last_clicked = [None, False] # last clicked cell, whether there is a cell

class Cell(Canvas):

	def __init__(self, master, color, coord):

		Canvas.__init__(self, master, width=50, height=50, bg=color, highlightthickness=0)
		self.coord = coord
		self.color = color

		self.piece = 'none' # none, white, red
		self.isKing = False # True, False

		self.length = 50
		self.radius = 4/5*self.length/2

		self.circle=self.create_oval(self.length/2-self.radius,self.length/2-self.radius,\
                         self.length/2+self.radius, self.length/2+self.radius,\
                         outline=self.color,fill=self.color)

		self.bind("<Button-1>", lambda event : self.move())

		self.highlighted=False

	def change_piece(self, to_color):
		self.piece = to_color
		self.update_piece_graphics()

	def update_piece_graphics(self):
		if self.piece == 'none':
			self.itemconfig(self.circle, fill=self.color)
			self.itemconfig(self.circle, outline=self.color)
		else:
			self.itemconfig(self.circle, fill=self.piece)
			self.itemconfig(self.circle, fill=self.piece)

	def highlight(self):
		self.highlighted=True
		self['bg']='light green'

	def unhighlight(self):
		self.highlighted=False
		self['bg']=self.color

	def move(self):
		global last_clicked

		if self.piece!='none':
			if self.highlighted:
				self.unhighlight()
				last_clicked = [None, False]
				return
			if last_clicked[1]: 
				last_clicked[0].unhighlight()
			self.highlight()
			last_clicked = [self, True]
		else:
			if last_clicked[0]==None:
				return
			if self.master.valid_move():
				last_clicked[0].unhighlight()
				self.change_piece(last_clicked[0].piece)
				last_clicked[0].change_piece('none')
				last_clicked = [None, False]

class Board(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()

		self.cells = []
		for i in range(8):
			for j in range(8):
				if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
					self.cells.append(Cell(self, 'blanched almond', (i, j)))
				else:
					self.cells.append(Cell(self, 'dark green', (i, j)))
				self.cells[f(i, j)].grid(row=i, column=j)

		for i in [f(6, 1), f(5, 0), f(5, 2), f(7, 2), f(6, 3), f(7, 4), f(5, 4), f(6, 5), f(7, 6), f(5, 6), f(6, 7), f(7, 0)]:
			self.cells[i].change_piece('red')

		for i in [f(1, 0), f(0, 1), f(2, 1), f(1, 2), f(0, 3), f(2, 3), f(1, 4), f(0, 5), f(2, 5), f(1, 6), f(0, 7), f(2, 7)]:
			self.cells[i].change_piece('white')

	def valid_move(self):
		return True


def play_checkers():
	root = Tk()
	root.title('Checkers')
	game = Board(root)
	root.mainloop()

play_checkers()