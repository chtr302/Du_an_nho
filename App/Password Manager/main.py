from tkinter import *
from tkinter import messagebox
import random
import json

# Save Data
def save_data():
    website = website_entry.get()
    info = conf_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : info,
            "password" : password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Error", message="Please, input information:")
    else:
        try:
            with open("Project Code/App/Password Manager/data.json","r") as f:
                # Read and Update data
                data = json.load(f)
                data.update(new_data)
        except json.JSONDecodeError:
            data = new_data
        
        with open("Project Code/App/Password Manager/data.json","w") as f:
        # Write data
            json.dump(data, f, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
           
def create_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0,password)

def search():
    website = website_entry.get()
    with open("Project Code/App/Password Manager/data.json","r") as f:
        data = json.load(f)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.askyesno(title = website, message=f"The {website} has:\n"
                                f"Email: {email}\n" f"Password: {password}")
        else:
            messagebox.askyesno(title = website,message= f"No data found for {website}")


# Window Game
window = Tk()
window.title("Password Manager by Hau")
window.minsize(width=450,height=200)
window.config(padx=20,pady=20,bg="white")

# Mainscreen
canvas = Canvas(width=200,height=200,bg="white", highlightthickness=0)
logo_img = PhotoImage(file="Project Code/App/Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

# Label
website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1,column=0,)

conf_label = Label(text="Email/Username: ", bg="white")
conf_label.grid(row=2,column=0)

password_label = Label(text="Password: ", bg="white", padx=20)
password_label.grid(row=3,column=0)

# Entry
website_entry = Entry(width=20, highlightthickness=0, bg="white", borderwidth=2, relief="groove")
website_entry.grid(row=1,column=1, sticky='w')
website_entry.focus()

conf_entry = Entry(width=35, highlightthickness=0, bg="white", borderwidth=2, relief="groove")
conf_entry.grid(row=2,column=1)
conf_entry.insert(0,"thau1298@gmail.com")

password_entry = Entry(width=17, highlightthickness=0, bg="white", borderwidth=2, relief="groove")
password_entry.grid(row=3,column=1, sticky='w')

# Button
password_button = Button(width=14,text="Generate Password",bg="white",borderwidth=0, command=create_pass)
password_button.grid(row=3,column=1, sticky='e')

add_button = Button(text="Add", bg="white",borderwidth=0, width=30, command=save_data)
add_button.grid(row=4, column=1)

search_button = Button(width=10,text="Search",bg="white",borderwidth=0, command=search)
search_button.grid(row=1,column=1, sticky='e')

window.mainloop()