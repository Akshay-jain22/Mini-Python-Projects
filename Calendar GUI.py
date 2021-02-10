from tkinter import *
import calendar

root = Tk()
root.geometry('510x700')
root.columnconfigure(0, weight=1)
root.title("Calendar GUI")

def changeYear():
    YEAR = entry.get()

    if YEAR.isdigit():
        text = calendar.calendar(int(YEAR))
        label.config(text="CALENDAR "+YEAR)
        label2.config(text="Enter the Year", fg="black")
        label3.config(text=text)
    else:
        label2.config(text="Invalid Year", fg="red")

label = Label(root, text="CALENDAR 2020", bg="dark gray", font=("times", 28, "bold"))
label.grid()

label2 = Label(root, text="Enter the Year", bg="white", font=20)
label2.grid()

entryVar = StringVar()
entry = Entry(root, width=50, textvariable=entryVar)
entry.grid()

show = Button(root, width=10, bg="red", fg="white", text="DISPLAY", command=changeYear)
show.grid()

root.config(background="white")

text = calendar.calendar(2020)

label3 = Label(root, text=text, font=("Consolas 10 bold"))
label3.grid()

root.mainloop()