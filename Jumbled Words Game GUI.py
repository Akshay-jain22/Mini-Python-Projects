import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
from words import word_list

Jumbles = []
num = 0

for i in word_list:
    chars = list(i)
    shuffle(chars)
    word = "".join(chars)
    Jumbles.append(word)

def init():
    global Jumbles, num
    length = len(word_list)
    num = random.randint(0, length-1)
    label1.config(text=Jumbles[num])

def check_answer():
    global Jumbles, num
    user_word = entry.get()

    if user_word.upper() == word_list[num].upper():
        messagebox.showinfo("Correct", "Woah!! You got it Right")
        reset_word()
        entry.delete(0, END)
    else:
        messagebox.showinfo("Wrong", "Nope! You got it Wrong")
        entry.delete(0, END)

def reset_word():
    init()

root = Tk()
root.geometry("300x300")
root.title("JUMBLED WORDS")
root.config(background="yellow")
root.resizable(False, False)

label1 = Label(root, font="times 20")
label1.pack(pady=30, ipady=10, ipadx=10)

entryVar = StringVar()
entry = Entry(root, width=30, textvariable=entryVar)
entry.pack(ipady=5, ipadx=5)

check = Button(root, width=10, bg="blue", fg="white", text="Check", command=check_answer)
check.pack(pady=40)

reset = Button(root, width=10, bg="green", fg="white", text="RESET", command=reset_word)
reset.pack()

init()
root.mainloop()