from tkinter import *

# Creating Basic Window
window = Tk()
window.geometry('312x324')
# window.resizable(0,0) # This prevents from resizing the window
window.title("Calculator")


##########################   Functions   ##########################
# btn_click Function will continuously update the input field whenever you enter a number
def btn_click(item) :
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# brn_clear function will clear the input field
def btn_clear() :
    global expression
    expression = ''
    input_text.set(expression)

def btn_equal() :
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ''

def btn_dash() :
    global expression
    if expression=='' :
        return
    else :
        expression = expression[:-1]
        input_text.set(expression)

expression = ''
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()


# Creating a frame for the input field
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground='black', highlightcolor='black')
input_frame.pack(side=TOP)

# Creating a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 10, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # ipday is internal padding to increase the height of input field 

# Creating another frame for the button below the input frame
btn_frame = Frame(window, width=312, height=274, bg='grey')
btn_frame.pack()

# First Row
clear = Button(btn_frame, text='C', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=btn_clear).grid(row=0, column=0)
dash = Button(btn_frame, text='<--', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=btn_dash).grid(row=0, column=1)
divide = Button(btn_frame, text='/', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('/')).grid(row=0, column=2)

# Second Row
seven = Button(btn_frame, text='7', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('7')).grid(row=1, column=0)
eight = Button(btn_frame, text='8', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('8')).grid(row=1, column=1)
nine = Button(btn_frame, text='9', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('9')).grid(row=1, column=2)
multiply = Button(btn_frame, text='X', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('*')).grid(row=1, column=3)

# Third Row
four = Button(btn_frame, text='4', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('4')).grid(row=2, column=0)
five = Button(btn_frame, text='5', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('5')).grid(row=2, column=1)
six = Button(btn_frame, text='6', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('6')).grid(row=2, column=2)
minus = Button(btn_frame, text='-', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('-')).grid(row=2, column=3)

# Fourth Row
one = Button(btn_frame, text='1', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('1')).grid(row=3, column=0)
two = Button(btn_frame, text='2', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('2')).grid(row=3, column=1)
three = Button(btn_frame, text='3', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('3')).grid(row=3, column=2)
plus = Button(btn_frame, text='+', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('+')).grid(row=3, column=3)

# Fifth Row
zero = Button(btn_frame, text='0', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('0')).grid(row=4, column=0)
point = Button(btn_frame, text='.', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=lambda : btn_click('.')).grid(row=4, column=1)
equals = Button(btn_frame, text='=', fg='black', width=10, height=3, bd=0, bg='white', cursor='hand2', command=btn_equal).grid(row=4, column=2)

window.mainloop()