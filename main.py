import time
import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = 0
display_score = Turtle()
display_score.penup()
display_score.color("white")
display_score.goto(x=0, y=270)
display_score.hideturtle()

screen.listen()
screen.onkey(snake.move_forward, "w")
screen.onkey(snake.turn_right, "d")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    with open("high_score.txt", mode="r") as file:
        display_score.write(f"Score: {score} | High Score: {file.read()}", False, "center", ("TW Cen MT", 20, 'normal'))

    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        food.relocate()
        snake.grow()
        score += 1
        display_score.clear()
        with open("high_score.txt", mode="r") as file:
            display_score.write(f"Score: {score} | High Score: {file.read()}", False, "center",
                                ("TW Cen MT", 20, 'normal'))

    if snake.head.xcor() >= WIDTH / 2 or snake.head.ycor() >= HEIGHT / 2 or snake.head.xcor() <= -1 * WIDTH / 2 or snake.head.ycor() <= -1 * HEIGHT / 2:
        game_is_on = False

    for segment in snake.snake:
        if snake.head.distance(segment) == 0:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False

with open("high_score.txt", mode="w") as file:
    file.write(f"{score}")


screen.exitonclick()
