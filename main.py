BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
e_word=[]
count=3
current_card={}
to_learn={}

window=Tk()
window.title("Flashy")
window.minsize(800,526)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)



canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="card_front.png")
canvas_image=canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0,row=0,columnspan=2)


card_back_img=PhotoImage(file="card_back.png")



try:
    file=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    file=pandas.read_csv("french_words.csv")
    to_learn=file.to_dict(orient="records")
else:
    to_learn=file.to_dict(orient="records")



Lang=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(canvas_image,image=card_front_img)
    canvas.itemconfig(Lang,text="French",fill="black")
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    flip_timer=window.after(3000,flipcard)

wrong_image = PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

def right_button_pressed():
    # Perform your specific task here
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")
    # Then call next_card() to show the next card
    next_card()

right_image = PhotoImage(file="right.png")
right_button=Button(image=right_image,bg=BACKGROUND_COLOR,command=right_button_pressed,highlightthickness=0)
right_button.grid(column=1,row=1)


def flipcard():
    global e_word
    canvas.itemconfig(canvas_image,image=card_back_img)
    canvas.grid(column=0,row=0,columnspan=2)
    canvas.itemconfig(Lang,text="English",fill="white")
    canvas.itemconfig(word,text=current_card["English"],fill="white")
flip_timer=window.after(3000,flipcard)
next_card()



















window.mainloop()