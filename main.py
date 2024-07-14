from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title= "Make your bet!", prompt="Who will win the race? ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
contestants = []

for i in range(6):
    kratos = Turtle(shape="turtle")
    kratos.color(color[i])
    kratos.penup()
    kratos.goto(-230, y)
    y += 50
    contestants.append(kratos)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in contestants:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")
            is_race_on = False

        randistance = random.randint(0, 10)
        turtle.forward(randistance)


screen.exitonclick()