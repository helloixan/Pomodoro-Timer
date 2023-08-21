from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_header.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0 :
        title_header.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
    elif reps != 8 :
        title_header.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else :
        title_header.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1)
    else :
        start_timer()
        marks = ""
        work_sessions = floor(reps/2)
        for _ in range (work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title_header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_header.grid(row=0, column=1)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, 'normal'), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", font=(FONT_NAME, 10, 'normal'), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()