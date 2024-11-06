from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
count_text = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(count_text,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_seconds = int(count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(count_text,text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_label.config(text=marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=150,pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN,font=(FONT_NAME,38,"bold"),bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0,column=1)



start_button = Button(text="Start", command=start_timer,highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
count_text=canvas.create_text(100,130,text="00:00",fill ="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=0)
check_label.grid(row=3, column=1)


window.mainloop()