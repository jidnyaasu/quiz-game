from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quiz Game")
        self.root.config(bg=THEME_COLOR)
        self.root.config(padx=20, pady=20)

        # Score Label
        self.score = Label(self.root, text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 12, "bold"))
        self.score.grid(column=1, row=0, pady=(20, 0))

        # Question canvas
        self.canvas = Canvas(self.root, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question here", fill=THEME_COLOR, font=("Ariel", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(self.root, image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=10)
        self.false_button = Button(self.root, image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=10)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="lavender")
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz. You can close the app window",
                fill="crimson"
            )
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)
            messagebox.showinfo("Quiz finished!", f"Your final score was {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
