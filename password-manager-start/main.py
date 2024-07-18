from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ------------------------------ SEARCH FUNCTION -------------------------------- #
def find_password():
    search_item = website_input_box.get()
    try:
        with open("passwords_file.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if search_item in data:
            email = data[search_item]["email"]
            password = data[search_item]["password"]
            messagebox.showinfo(title=f"{search_item} Login Information", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Invalid Entry", message="No details for the website exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    password_entry_box.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry_box.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input_box.get()
    email = email_input_box.get()
    password = password_entry_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Empty Fields!")
    else:
        try:
            with open("passwords_file.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)
        with open("passwords_file.json", "w") as file:
            json.dump(data, file, indent=4)
            website_input_box.delete(0, END)
            password_entry_box.delete(0, END)

        messagebox.showinfo(title=f"{website} Entry", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", padx=5, pady=5)
website_label.grid(column=0, row=1)

search_button = Button(text="Search", padx=0, pady=0, borderwidth=0, bg="white", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

website_input_box = Entry()
website_input_box.focus()
website_input_box.grid(column=1, row=1, sticky="EW")

email_label = Label(text="Email/Username:", bg="white", padx=5, pady=5)
email_label.grid(column=0, row=2)

email_input_box = Entry()
email_input_box.insert(END, "max_c@live.com")
email_input_box.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:", bg="white", padx=5, pady=5)
password_label.grid(column=0, row=3)

password_entry_box = Entry()
password_entry_box.grid(column=1, row=3, sticky="EW")

generate_pw_button = Button(text="Generate Password", padx=0, pady=0, borderwidth=0, bg="white",
                            command=generate_password)
generate_pw_button.grid(column=2, row=3, sticky="EW")

add_pw_button = Button(text="Add", width=35, borderwidth=0, pady=0, padx=0, bg="white", command=save)
add_pw_button.grid(column=1, row=4, columnspan=2, sticky="EW")
window.mainloop()
