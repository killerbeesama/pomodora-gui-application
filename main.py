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
countdown_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(countdown_timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer",fg=PINK)
    label2.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)
    if reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label1.config(text="Break", fg=PINK)
    if reps == 8:
        count_down(long_break_sec)
        label1.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second == 0:
        count_second = int("00")
    if count_second < 10:
        count_second = f"{int(0)}{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count >= 0:
        global countdown_timer
        countdown_timer = window.after(1000, count_down, count - 1)
    else:
        check_mark = ""
        start_timer()
        for _ in range(math.floor(reps/2)):
            check_mark += "✔"
        label2.config(text=f"{check_mark}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodora gui application/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
label1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
label1.grid(column=1, row=0)
label2 = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
label2.grid(column=1, row=3)
button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()
