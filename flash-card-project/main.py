BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/german_words.csv")
finally:
    words_dict = data.to_dict(orient="records")
flip_timer = None
current_card = {}
def next_card():
    global flip_timer, current_card
    if flip_timer:
        window.after_cancel(flip_timer)
    canvas.itemconfig(img , image=front_card_img)
    current_card = random.choice(words_dict)
    canvas.itemconfig(dynamic_text, text=current_card["German"],fill="black")
    canvas.itemconfig(title_text, text="German",fill="black")
    flip_timer= window.after(3000, flip_card) 
    
def flip_card():
    canvas.itemconfig(img , image=back_card_img)
    canvas.itemconfig(dynamic_text, text=current_card["English"],fill="white")
    canvas.itemconfig(title_text, text="English",fill="white")

def known_word():
    words_dict.remove(current_card)
    updated_data = pandas.DataFrame(words_dict)
    updated_data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()
def unknown_word(): 
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,next_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
img = canvas.create_image(400, 263, image=front_card_img)
title_text = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
dynamic_text = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0, column=0,columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_image,highlightthickness=0,command=unknown_word)
right_button = Button(image=right_image,highlightthickness=0,command=known_word)
wrong_button.grid(row=1,column=0)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()