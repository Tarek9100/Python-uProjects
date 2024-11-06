from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import json

WHITE = "#ffffff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)

def search_website():
    website = website_entry.get()
    try:
        # Attempt to load data from data.json
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except:
        # Error if the file does not exist
        messagebox.showerror(title="Error", message=f"No details for '{website}' exists.")
    else:
        # Check if the website exists in the data
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for '{website}' exists.")

def generate_password():
    password_entry.delete(0, END)
    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    passwrd = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": passwrd
        }
    }
    if len(username) < 3 or len(website) < 2 or len(passwrd) < 6:
        messagebox.showerror(title="Oops",message="Invalid username/password")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Username: {username}\n Password: {passwrd}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json",mode="r") as data_file:
                    data = json.load(data_file)

            except:
                    data = {}
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels and Entries
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)
website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1,columnspan=2,sticky="w")
website_entry.focus()

username_label = Label(text="Email/Username:", bg=WHITE)
username_label.grid(row=2, column=0)
username_entry = Entry(window, width=30)
username_entry.grid(row=2, column=1,columnspan=2,sticky="w")
username_entry.insert(0,"tareki9100@gmail.com")

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)
password_entry = Entry(window)
password_entry.grid(row=3, column=1,sticky="w",padx=(0,0))

# Buttons
search_button = Button(text="Search", bg=WHITE,command=search_website)
search_button.grid(row=1, column=2,sticky="w",padx=(0,0))

generate_password_button = Button(text="Generate Password", bg=WHITE,command=generate_password)
generate_password_button.grid(row=3, column=2,sticky="w",padx=(0,0))

add_button = Button(text="Add", bg=WHITE, width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky="w")

window.mainloop()
