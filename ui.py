from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, brain: QuizBrain):
        self.window = Tk()
        self.quiz = brain
        self.window.title("Quiz Application 3000")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.text_displayed = self.canvas.create_text(150, 125, width=280, text="Question",
                                                      font=("Arial", 20, "italic"))

        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, borderwidth=0, relief="flat",
                                     highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, borderwidth=0, relief="flat",
                                   highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_displayed, text=question_text)
        else:
            self.canvas.itemconfig(self.text_displayed, text="You are done with the quiz!")
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    def true_pressed(self):
        check_result = self.quiz.check_answer("True")
        self.give_feedback(check_result)

    def false_pressed(self):
        check_result = self.quiz.check_answer("False")
        self.give_feedback(check_result)

    def give_feedback(self, check_result: bool):
        if check_result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
