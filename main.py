from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    password = password_input.get()
    email = username_input.get()
    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the detail entered:\n Email: {email} \n Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showerror(
            title="Oopssss :(", message="You Cannot leave the field Empty")

# ---------------------------- UI SETUP ------------------------------- #


# Windows
window = Tk()
window.title("Password Manager").config(padx=50, pady=50)
# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image).grid(column=1, row=0)

# Label
website_label = Label(text="Website:").grid(column=0, row=1)
username_label = Label(text="Email/Username:").grid(column=0, row=2)
password_label = Label(text="Password:").grid(column=0, row=3)

# Entry
website_input = Entry(width=35).grid(column=1, row=1, columnspan=2, sticky="EW").focus()
username_input = Entry(width=35).grid(column=1, row=2, columnspan=2, sticky="EW").insert(0, "parimal@gmail.com")
password_input = Entry(width=21).grid(column=1, row=3, sticky="EW")

# Buttons

generate_button = Button(text="Generate Password", command=generate_pass).grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
