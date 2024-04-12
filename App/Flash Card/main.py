from tkinter import *
import pandas as pd
import random

# Create Data
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("Project Code/App/Flash Card/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Project Code/App/Flash Card/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Radom Word
def radom_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_front.itemconfig(title_label, text="French", fill="black")
    card_front.itemconfig(vocab_label,text=current_card["French"], fill="black")
    card_front.itemconfig(card_image, image=logo_img_1)
    flip_timer = window.after(3000,flip_card)

def flip_card():
    global current_card
    current_card = random.choice(to_learn)
    card_front.itemconfig(title_label, text="English", fill="white")
    card_front.itemconfig(vocab_label,text=current_card["English"], fill="white")
    card_front.itemconfig(card_image, image=logo_img_2)

def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("Project Code/App/Flash Card/data/words_to_learn.csv")
    radom_word()


# Screen
window = Tk()
window.title("Flash Card by Tran Cong Hau")
window.config(padx=50, pady=50,bg="#B1DDC6")

flip_timer = window.after(3000,flip_card)

# Main Screen
card_front = Canvas(width=800,height=526,highlightthickness=0,bg="#B1DDC6")
logo_img_1 = PhotoImage(file="Project Code/App/Flash Card/images/card_front.png")
logo_img_2 = PhotoImage(file="Project Code/App/Flash Card/images/card_back.png")
card_image = card_front.create_image(400,270,image=logo_img_1)
card_front.grid(row=0,column=0,columnspan=2)

title_label = card_front.create_text(400,150,font=("Ariel", 40,"italic"), text="")
vocab_label = card_front.create_text(400,263,font=("Ariel", 45,"bold"), text="")

right_img = PhotoImage(file="Project Code/App/Flash Card/images/right.png")
right = Button(image=right_img, bg="#B1DDC6",bd=0, activebackground="#B1DDC6", command=is_know)
right.grid(row=1,column=1)

wrong_img = PhotoImage(file="Project Code/App/Flash Card/images/wrong.png")
wrong = Button(image=wrong_img, bg="#B1DDC6",bd=0, activebackground="#B1DDC6", command=radom_word)
wrong.grid(row=1,column=0)

radom_word()


window.mainloop()