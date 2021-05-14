from tkinter import *

THEME_COLOR = "#375362"


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Application 3000")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"))

        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, borderwidth=0, relief="flat", highlightthickness=0)
        self.correct_button.grid(column=0, row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, borderwidth=0, relief="flat", highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()
