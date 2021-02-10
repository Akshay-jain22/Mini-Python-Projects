from faker import Faker
from tkinter import *

root = Tk()
root.columnconfigure(0, weight=1)
root.title("Fake Profile Generator")
root.resizable(False, False)

Fake = Faker()

def generate():
    name.config(text=Fake.name())
    email.config(text=Fake.email())
    country.config(text=Fake.country())
    text.config(text=Fake.text())
    url.config(text=Fake.url())
    location.config(text="Latitude : " + str(Fake.latitude()) + ", Longitude : " + str(Fake.longitude()))
    copy.config(text="Copy Fake-Data", bg="red")

def copyContent():
    content = name['text'] + ", " + email['text'] + ", " + country['text'] + ", " + text['text'] + ", " + url['text'] + ", " + location['text']
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()
    copy.config(text="Content Copied", bg="green")

label = Label(root, text="Fake Data Generator", font=("times", 28, "bold"))
label.grid()

gen = Button(root, width=20, bg="red", fg="white", text="Generate Fake-Data", command=generate)
gen.grid()

name = Label(root, text="Fake Name", font=("times", 10))
name.grid()

email = Label(root, text="Fake Email-ID", font=("times", 10))
email.grid()

country = Label(root, text="Fake Country", font=("times", 10))
country.grid()

text = Label(root, text="Fake Text", font=("times", 10))
text.grid()

url = Label(root, text="Fake URL", font=("times", 10))
url.grid()

location = Label(root, text="Fake Location", font=("times", 10))
location.grid()

copy = Button(root, width=20, bg="red", fg="white", text="Copy Fake-Data", command=copyContent)
copy.grid()

root.mainloop()