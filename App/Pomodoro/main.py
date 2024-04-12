from tkinter import *
import math

PINK = "#e2979c"
RED = "#7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
running = True


# Time Meachanism
def start_timer():
    global reps
    global running
    running = True
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [1,3,5,7]:
        count_down(work_sec)
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN)
        tick_label.config(text="✓", bg=YELLOW, fg=GREEN)
    elif reps in [2,4,6]:
        count_down(short_break_sec)
        timer_label.config(text="Break Time!", bg=YELLOW, fg=PINK)
        tick_label.config(text="x", bg=YELLOW, fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break Long Time!", bg=YELLOW, fg=RED)
        tick_label.config(text="x", bg=YELLOW, fg=RED)
    
def reset_timer():
    global reps
    global running
    running = False
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# Time Countdown
def count_down(count):
    global running
    if running:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        else:
            start_timer()


# Window Game
window = Tk()
window.title("Pomodoro by Hau")
window.config(padx=100,pady=50,bg=YELLOW)


# Main Screen
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=250,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Project Code/App/Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightthickness=0,bg="white",borderwidth=0, command=start_timer)
start_button.grid(row=2,column=0)


reset_button = Button(text="Reset",highlightthickness=0,bg="white",borderwidth=0, command= reset_timer)
reset_button.grid(row=2,column=2)

tick_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME,15,"bold"))
tick_label.grid(row=3,column=1)


window.mainloop()