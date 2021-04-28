from turtle import Turtle
import pandas

us_states = pandas.read_csv("50_states.csv")
state_list = us_states["state"].to_list


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        s

    def user_answer(self):
        user_answer = self

