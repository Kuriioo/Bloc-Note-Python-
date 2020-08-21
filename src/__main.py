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
		self.Menu = tkinter.Menu(self.Window)
		self.Window.config(menu=self.Menu)
		self.Files = tkinter.Menu(self.Window, tearoff=False)
		self.Menu.add_cascade(label='File', menu=self.Files)
		self.Files.add_command(label='New File', command=self.newFile)
		self.Files.add_command(label='Open File', command=self.openFile)
		self.Files.add_command(label='Save File', command=self.saveFile)
		self.Files.add_command(label='Save As', command=self.saveAsFile)
		self.Files.add_command(label='Exit', command=self.Window.quit)
	def setTitle(self, str):
		self.Window.title(str)
	def setSize(self, x, y):
		self.Window.geometry(f'{x}x{y}')
		self.Properties.x = x
		self.Properties.y = y
	def newFile(self):
		self.Text.delete('1.0', 'end')
		self.setTitle('New File - Bloc Note')
		self.Properties.File = False
	def openFile(self):
		TextFile = FileDialog.askopenfilename(defaultextension=".*", title="Open File")
		if TextFile:
			self.Text.delete('1.0', 'end')
			self.Properties.File = TextFile			
			File = TextFile
			self.setTitle(f'{File} - Bloc Note')
			TextFile = open(TextFile, 'r')
			Lines = enumerate(TextFile)
			for index, key in Lines:
				self.Text.insert('end', key)
			TextFile.close()
	def saveFile(self):
		if self.Properties.File:
			TextFile = open(self.Properties.File, 'w')
			TextFile.write(self.Text.get('1.0', 'end'))
			TextFile.close()
		else:
			self.saveAsFile()
	def saveAsFile(self):
		TextFile = FileDialog.asksaveasfilename(defaultextension=".*", title="Save As", filetypes=(("All Files", "*.*")))
		if TextFile:
			self.Properties.File = TextFile
			File = TextFile
			self.setTitle(f'{File} - Bloc Note')
			TextFile = open(TextFile, 'w')
			TextFile.write(self.Text.get('1.0', 'end'))
			TextFile.close()
Main = Main()
Main.Window.mainloop()