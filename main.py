from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the racce? Enter a color: ")
all_turtles = []
position = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True


while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if(winning_color == user_bet):
                print("You have won! The {winning_color} turtle")
            else:
                print(f"Sorry you Lost! The {winning_color} is the winner")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
