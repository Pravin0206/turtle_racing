from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red","orange","yellow","green","blue","purple"]
y_positions= [-170, -105, -40, 25, 90, 155]
all_turtles = []

for i in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-230,y=y_positions[i])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!!!!{winning_color} turtle is the winner!!!")
            else:
                print(f"You lose :){winning_color} turtle is the winner!!!")

        turtle.forward(random.randint(1,10))


screen.exitonclick()