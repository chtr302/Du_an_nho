from tkinter import *
from Quiz_brain import *

THEME_COLOR = '#375362'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler by Hau")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        # Score 
        self.score_point = 0
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0,column=1)

        # Quiz Square
        self.quiz_square = Canvas(width=300,height=250, bg="white")
        self.quiz_question = self.quiz_square.create_text(
            155,
            120,
            text="My Question",
            font=("Arial",20,"italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.quiz_square.grid(row=1,column=0,columnspan=2, pady=20, padx=0)

        # Button Check
        first_image = PhotoImage(file="Game/Quiz/images/true.png")
        second_image = PhotoImage(file="Game/Quiz/images/false.png")

        self.true = Button(image=first_image, highlightthickness=0,borderwidth=0, command=self.check_true)
        self.true.grid(row=2,column=0)

        self.false =  Button(image=second_image, highlightthickness=0,borderwidth=0, command=self.check_false)
        self.false.grid(row=2,column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.quiz_square.config(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.quiz_square.itemconfig(self.quiz_question, text=q_text)
        else:
            self.quiz_square.itemconfig(self.quiz_question, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def check_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def check_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        
    def give_feedback(self, is_right):
        if is_right:
            self.quiz_square.config(bg="green")
            self.score_point += 1
            self.score.config(text=f"Score: {self.score_point}",fg="white")
        else:
            self.quiz_square.config(bg="red")
            
        self.window.after(200,self.get_next_question)
