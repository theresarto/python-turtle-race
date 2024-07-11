from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=600)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. "
                                                           "Enter a colour "
                                                           "(purple, blue, green, gold, orange, or red): ")
print(user_bet)

purple = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
red = Turtle()

list_of_turtles = [purple, blue, green, yellow, orange, red]
colours = ["purple", "blue", "green", "gold", "orange", "red"]


def change_shape():
    for turtle in list_of_turtles:
        turtle.shape("turtle")


change_shape()


def change_colour():
    for turtle, colour in zip(list_of_turtles, colours):
        turtle.color(colour)


change_colour()


def starting_position():
    starting_x = -380 # Screen width is 800, so half of axis is 400. Lessen by 20 for margin
    number_of_turtles = len(list_of_turtles)
    y_adjustment = 600 / (number_of_turtles + 1)
    y_range = 600 / 2  # Starting from the middle of the screen height

    for i, turtle in enumerate(list_of_turtles):
        turtle.penup()
        starting_y = y_range - (i + 1) * y_adjustment
        turtle.goto(starting_x, starting_y)
        turtle.pendown()


is_race_on = False
if user_bet:
    is_race_on = True

starting_position()

pen = Turtle()
pen.penup()
pen.ht()

while is_race_on:
    for turtle in list_of_turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 380:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Check if the user's bet matches the winning turtle
            if winning_color == user_bet:
                pen.goto(0, 0)
                pen.write("You won the bet!", align="center", font=('Arial', 18, 'normal'))
            else:
                pen.goto(0, 0)
                pen.write(f"You lost. The {winning_color} turtle won.", align="center", font=('Arial', 18, 'normal'))
            break

screen.exitonclick()
