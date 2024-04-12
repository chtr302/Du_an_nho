from tkinter import *
import requests

# Fix text
def text_fix():
    response = requests.get("https://api.kanye.rest/")
    data = response.json()["quote"]
    quotes.itemconfig(text, text=data, fill = "white")


#Setup Screen
window = Tk()
window.title("Kane Quotes")
window.config(padx=20, pady=20, bg="white")

# Main Screen
quotes = Canvas(width=300,height=400,bg="white", highlightthickness=0)
quotes_image = PhotoImage(file="Project Code/App/APIs/Kanye Quotes/background.png")
quotes.create_image(150,200,image=quotes_image)
quotes.grid(row=0,column=0)

text = quotes.create_text(150,150,width=260,font=("Ariel", 20), text="Hello!", fill="white")


kanye_image = PhotoImage(file="Project Code/App/APIs/Kanye Quotes/kanye.png")
kanye = Button(image=kanye_image,bg="white",highlightthickness=0,bd=0, activebackground="white",command=text_fix)
kanye.grid(row=1,column=0)

window.mainloop()