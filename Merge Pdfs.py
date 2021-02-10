from PyPDF2 import PdfFileMerger
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.columnconfigure(0, weight=1)
root.title("PDF Merger")
root.resizable(False, False)

def mergePDF():
    DIRECTORY_NAME = filedialog.askdirectory()

    if(len(DIRECTORY_NAME)>1):
        locError.config(text=DIRECTORY_NAME, fg="green")
    else:
        locError.config(text="Please Choose Folder", fg="red")
        return

    try:
        merger = PdfFileMerger()
        for item in os.listdir(DIRECTORY_NAME):
            if item.endswith('.pdf'):
                merger.append(DIRECTORY_NAME + "/" + item)

        merger.write(DIRECTORY_NAME + "/merged_pdf.pdf")
        merger.close()
        locError.config(text="Successfully Merged the PDFs", fg="green")
    
    except:
        locError.config(text="Cannot Merge the PDFs", fg="red")
    

label = Label(root, text="Select the Folder", font=('jost', 15))
label.grid()

selectFolder = Button(root, width=10, bg="red", fg="white", text="Choose Path", command=mergePDF)
selectFolder.grid()

locError = Label(root, text="Error Message Of Path", fg="red", font=('jost', 10))
locError.grid()

root.mainloop()