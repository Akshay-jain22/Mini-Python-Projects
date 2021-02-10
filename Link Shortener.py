import pyshorteners
from tkinter import *

root = Tk()
root.columnconfigure(0, weight=1)
root.title("Link Shortener")
root.resizable(False, False)

def Short_URL():
    original_link = link.get()

    try:
        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(original_link)
        label2.config(text=short_link)
    
    except Exception as e:
        label2.config(text="Improper Internet Connection")

def copyContent():
    content = label2['text']
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()
    copy.config(text="Content Copied", bg="green")


label = Label(root, text="Enter the Link", font=('jost', 15))
label.grid()

link = Entry(root, width=50)
link.grid()

shorten = Button(root, width=10, bg="red", fg="white", text="GENERATE", command=Short_URL)
shorten.grid()

label2 = Label(root, text="Shortened Link", font=10)
label2.grid()

copy = Button(root, width=12, bg="red", fg="white", text="Copy Short URL", command=copyContent)
copy.grid()

root.mainloop()