import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image

root = Tk()
root.title("PNG to JPG Converter")
root.resizable(False, False)

canvas1 = Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = Label(root, text='File Conversion Tool', bg='azure3', font=('helevetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = Button(text='Select PNG File', command=getPNG, bg='royalblue', fg='white', font=('helevetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

def convertToJPG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton = Button(text='CONVERT', command=convertToJPG, bg='royalblue', fg='white', font=('helevetica', 12, 'bold'))
canvas1.create_window(150,180, window=saveAsButton)

root.mainloop()

