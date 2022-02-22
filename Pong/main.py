import turtle
# turtle module is for graphic -> suitable for simple game


class Player:
    def __init__(self, sc):
        self.score = sc


p_A = Player(0)
p_B = Player(0)

# create window
wn = turtle.Screen()
wn.title("Pong by CC")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)             # this stop window from updating automatically

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()            # hide the board, displaying only what is written
pen.goto(0, 260)
pen.write(f"Player A: {p_A.score} | Player B: {p_B.score}", align="center", font=("Courier", 24, "normal"))


# Functions to move
def paddle_a_up():
    # first we need to know the current coordinate
    y = paddle_A.ycor()
    # now move up
    y += 20
    paddle_A.sety(y)


def paddle_a_down():
    # first we need to know the current coordinate
    y = paddle_A.ycor()
    # now move up
    y -= 20
    paddle_A.sety(y)


def paddle_b_up():
    # first we need to know the current coordinate
    y = paddle_B.ycor()
    # now move up
    y += 20
    paddle_B.sety(y)


def paddle_b_down():
    # first we need to know the current coordinate
    y = paddle_B.ycor()
    # now move up
    y -= 20
    paddle_B.sety(y)


def move_the_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# keyboard binding
wn.listen()                             # this tells the window to 'listen' to keyboard input
wn.onkeypress(paddle_a_up, 'w')         # set the 'w' key is for moving paddle A up
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# main game loop
if __name__ == "__main__":
    while True:
        wn.update()
        move_the_ball()

        # boarder check
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            p_A.score += 1
            pen.clear()
            pen.write(f"Player A: {p_A.score} | Player B: {p_B.score}", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            p_B.score += 1
            pen.clear()
            pen.write(f"Player A: {p_A.score} | Player B: {p_B.score}", align="center", font=("Courier", 24, "normal"))

        # colliding check
        if (ball.xcor() >= 330) and (ball.ycor() < (paddle_B.ycor() + 50)) and (ball.ycor() > (paddle_B.ycor() - 50)):
            ball.setx(330)
            ball.dx *= -1

        if (ball.xcor() <= -330) and (ball.ycor() < (paddle_A.ycor() + 50)) and (ball.ycor() > (paddle_A.ycor() - 50)):
            ball.setx(-330)
            ball.dx *= -1
