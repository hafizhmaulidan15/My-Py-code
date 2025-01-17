import sys
from PIL import ImageTk, Image
from threading import Thread

import tkinter as tk
from tkinter import ttk, filedialog

x = 600
y = 700

class ImageConverter(tk.Frame):
	def __init__(self, window):
		super().__init__(window)
		self.init_ui()
		
	def init_ui(self):
		self.pack()
		self.label = tk.Label(self, text='IMAGE CONVERTER', font=('Helvetica',20))
		self.label.pack()
		self.openbtn = tk.Button(self, text='Load Image', command=self.open_image)
		self.openbtn.pack()
		self.imageframe = tk.LabelFrame(self, text='Image View')
		self.imageframe.pack()
		self.labelimage = tk.Label(self.imageframe, width=100, height=30)
		self.labelimage.pack()
		self.convertbtn = tk.Button(self, text='Convert Image')
		self.convertbtn.pack()
		self.combobox = ttk.Combobox(self)
		self.combobox['values'] = ['BMP', 'GIF', 'JPEG', 'PNG', 'TIFF']
		self.combobox.pack()
		self.progress = ttk.Progressbar(self)
		self.progress.pack()
		self.convertbtn.bind("<Button-1>", self.run_threading)
		
	def open_image(self):
		self.filename = filedialog.askopenfilename()
		self.img = Image.open(self.filename)
		self.x = int(self.img.size[0]*0+x*.50)
		self.y = int(self.img.size[1]*0+y*.60)
		self.img2 = self.img.resize((self.x, self.y))
		self.imgtk = ImageTk.PhotoImage(self.img)
		self.labelimage.config(image=self.imgtk, width=500, height=500)
		
	def run_threading(self, event):
		t = Thread(target=self.convert_image)
		t.start()
		
	def convert_image(self):
		self.progress.start()
		self.format = self.combobox.get()
		self.new_img = self.img.save('convertedImage'+f'.{self.format}')
		for i in range(1000):
			self.progress['value'] = i
		self.progress.stop()
		
		self.top = tk.Toplevel(width=300, height=300)
		self.toplabel = tk.Label(self.top, width=40, height=40, text=f"Image berhasil di konversi ke {self.combobox.get()}")
		self.toplabel.pack()
		self.top.mainloop()
		
window = tk.Tk()
gui = ImageConverter(window)
window.geometry(f'{x}x{y}')

window.mainloop()