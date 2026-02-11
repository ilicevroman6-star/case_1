from turtle import *
speed(1)
fillcolor("pink")
pencolor("pink")

def square(x, y, a):
    up()
    setposition(x, y)
    down()
    color("pink")
    fillcolor("pink")
    pencolor("pink")
    begin_fill()

    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)

    end_fill()
    home()

square(0, 0, 50)
hideturtle()
done()