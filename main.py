from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    password = password_input.get()
    email = username_input.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password} \n")
        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Windows
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# Canvas
canvas = Canvas(width=200 , height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image=logo_image)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1,columnspan=2, sticky="EW")
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "parimalmeshram15@gmail.com" )

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# Buttons

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()