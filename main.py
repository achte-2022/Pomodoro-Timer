# IMPORTING LIBRARIES
import tkinter

# CONSTANTS
RED = "#F32424"
BLUE = "#3B44F6"
BLACK = "#000000"
YELLOW = "#F7EC09"
GREEN = "#446A46"
FONT_NAME = "Courier"
WORK_MIN = 8
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 6
TOMATO_FILE_PATH = "./images/tomato.png"
TOMATO_HEIGHT = 224
TOMATO_WIDTH = 202
CHECKMARKS = "✓"
REPS_LENGTH = 8

# Global Variables
reps = 0
timer = None

# TIMER RESET
def reset_timer():
    global reps

    reps = 0
    timer_text_init = "00:00"
    canvas.itemconfig(timer_text, text=timer_text_init)
    window.after_cancel(timer)
    checkmarks_label.config(text="")
    timer_label.config(text="Timer", fg=BLACK)
    return


# Timer
def start_timer():
    global reps

    work_seconds = WORK_MIN
    short_break_seconds = SHORT_BREAK_MIN
    long_break_seconds = LONG_BREAK_MIN
    current_rep_number = reps % REPS_LENGTH

    if (current_rep_number % 2) == 0:
        timer_label.config(text="Work", fg=RED)
        countdown(work_seconds)
    elif current_rep_number < 7:
        timer_label.config(text="Break", fg=GREEN)
        countdown(short_break_seconds)
    else:
        timer_label.config(text="Break", fg=BLUE)
        countdown(long_break_seconds)

    reps += 1
    return


# Countdown
def countdown(count):
    global reps
    global CHECKMARKS
    global timer

    count_minutes = count // 60
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)
    if count_minutes < 10:
        count_minutes = "0" + str(count_minutes)
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
        timer = window.after(1000, countdown, (count - 1))
    else:
        if (reps % REPS_LENGTH) == 0:
            checkmarks = CHECKMARKS * (reps // REPS_LENGTH)
            checkmarks_label.config(text=checkmarks)
        start_timer()

    return


# UI SETUP
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)


# TIMER LABEL
timer_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 30, "bold"), fg=BLACK, bg=YELLOW
)
timer_label.grid(row=0, column=1)

# CANVAS
canvas = tkinter.Canvas(
    width=TOMATO_WIDTH, height=TOMATO_HEIGHT, bg=YELLOW, highlightthickness=0
)
tomato_image = tkinter.PhotoImage(file=TOMATO_FILE_PATH)
canvas.create_image(TOMATO_WIDTH / 2, TOMATO_HEIGHT / 2, image=tomato_image)
timer_text_init = "00:00"
timer_text = canvas.create_text(
    TOMATO_WIDTH / 2,
    TOMATO_HEIGHT / 2 + 20,
    text=timer_text_init,
    font=(FONT_NAME, 40, "bold"),
    fill=BLACK,
)
canvas.grid(row=1, column=1)

# START BUTTON
start_button = tkinter.Button(
    text="Start",
    font=(FONT_NAME, 15, "bold"),
    fg=YELLOW,
    bg=BLUE,
    highlightthickness=0,
    command=start_timer,
)
start_button.grid(row=2, column=0)

# RESET BUTTON
reset_button = tkinter.Button(
    text="Reset",
    font=(FONT_NAME, 15, "bold"),
    fg=YELLOW,
    bg=BLUE,
    highlightthickness=0,
    command=reset_timer,
)
reset_button.grid(row=2, column=2)

# CHECKMARKS LABEL
checkmarks_label = tkinter.Label(font=(FONT_NAME, 60, "bold"), fg=BLUE, bg=YELLOW)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
