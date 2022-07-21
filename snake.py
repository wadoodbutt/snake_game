from turtle import Turtle, Screen

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_size = 0
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake) - 1]
        self.body = []

    def create_snake(self):
        for x in range(0, 3):
            square = Turtle()
            square.shape("square")
            square.color("SpringGreen")
            square.penup()
            x_cord = (x * 20) - 20
            square.goto(x=x_cord, y=0)
            self.snake.append(square)
            self.snake_size += 3

    def move_forward(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def turn_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def turn_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def grow(self):
        square = Turtle()
        square.hideturtle()
        square.goto(x=self.tail.xcor(), y=self.tail.ycor())
        square.shape("square")
        square.color("SpringGreen")
        square.penup()
        square.showturtle()
        self.snake.append(square)
        self.snake_size += 1

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            prev_x_cord = self.snake[segment - 1].xcor()
            prev_y_cord = self.snake[segment - 1].ycor()
            self.snake[segment].goto(y=prev_y_cord, x=prev_x_cord)
        self.snake[0].forward(MOVE_DISTANCE)
