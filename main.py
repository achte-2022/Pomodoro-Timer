# Importing Libraries
import tkinter

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_FILE_PATH = "./images/tomato.png"
TOMATO_HEIGHT = 224
TOMATO_WIDTH = 202
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# UI Setup
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(width=TOMATO_WIDTH, height=TOMATO_HEIGHT)
tomato_img = tkinter.PhotoImage(file=TOMATO_FILE_PATH)
canvas.create_image(TOMATO_WIDTH / 2, TOMATO_HEIGHT / 2, image=tomato_img)
canvas.pack()


window.mainloop()
