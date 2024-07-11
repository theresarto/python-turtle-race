from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(width=800, height=600)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race.Enter a colour: ")
print(user_bet)

screen.exitonclick()
