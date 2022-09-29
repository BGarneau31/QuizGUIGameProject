from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT =("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=40)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Placeholder",
            font=FONT,
            fill=THEME_COLOR,
            width=280)

        self.true_button = Button()
        true_image = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_image, padx=20, pady=20, highlightthickness=0, command=self.check_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button()
        false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_image, padx=20, pady=40, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        answer_is_right = self.quiz.check_answer("True")
        self.give_feedback(answer_is_right)

    def check_false(self):
        answer_is_right = self.quiz.check_answer("False")
        self.give_feedback(answer_is_right)

    def give_feedback(self, answer_is_right):
        if answer_is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



