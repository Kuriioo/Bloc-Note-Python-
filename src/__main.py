import tkinter as tkinter
from tkinter import filedialog as FileDialog
from Properties import Properties

class Main():
	def __init__(self):
		self.Window = tkinter.Tk()
		self.Properties = Properties()
		self.setTitle('Bloc Note')
		self.setSize(self.Properties.x, self.Properties.y)
	def setTitle(self, str):
		self.Window.title(str)
	def setSize(self, x, y):
		self.Window.geometry(f'{x}x{y}')
		self.Properties.x = x
		self.Properties.y = y

Main = Main()
Main.Window.mainloop()