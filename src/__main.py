import tkinter as tkinter
from tkinter import filedialog as FileDialog
from Properties import Properties

class Main():
	def __init__(self):
		self.Window = tkinter.Tk()
		self.Properties = Properties()
		self.setTitle('Bloc Note')
		self.setSize(self.Properties.x, self.Properties.y)
		self.Frame = tkinter.Frame(self.Window).pack(fill="x", padx=1, pady=1)
		self.TextScroll = tkinter.Scrollbar(self.Frame)
		self.Text = tkinter.Text(self.Frame, width=97, height=25, font=("Helvetica", self.Properties.TextSize, "bold"),
			selectbackground="gray",
			selectforeground="black",
			undo=True,
			yscrollcommand=self.TextScroll.set
		)
		self.TextScroll.config(command=self.Text.yview)
		self.Text.pack()
	def setTitle(self, str):
		self.Window.title(str)
	def setSize(self, x, y):
		self.Window.geometry(f'{x}x{y}')
		self.Properties.x = x
		self.Properties.y = y
	def newFile(self):
		self.setTitle('New File - Bloc Note')
		self.Properties.File = False

Main = Main()
Main.Window.mainloop()