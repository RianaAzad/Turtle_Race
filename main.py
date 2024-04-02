from turtle import *
import random


screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "DarkBlue", "Coral4", "Chocolate", "DarkSlateGray", "DarkMagenta"]
user_bet = screen.textinput(title="Turtle Race", prompt="Which color do you think will win the race?")

is_race_on = True
all_turtles = []
x = -230
y = -70
for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x, y)
    all_turtles.append(tim)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            turtle.shapesize(4,4)

            if winner == user_bet:
                screen.bgpic("WINNER.png")
                print(f"You've won the race! The {winner} turtle is winner.")
            else:
                screen.bgpic("loss.png")
                print(f"You've lost the race! The {winner} turtle is winner.")


screen.exitonclick()
