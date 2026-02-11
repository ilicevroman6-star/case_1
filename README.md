from turtle import *
speed(1)
fillcolor("orange")
pencolor("orange")
def right_triangle(x, y, a, b):
    up()
    setposition(x, y)
    down()
    color("orange")
    fillcolor("orange")
    pencolor("orange")
    begin_fill()

    forward(a)
    left(90)
    forward(b)

    import math
    c = math.sqrt(a ** 2 + b ** 2) #гипотенуза
    forward(c)

    left(135)

    end_fill()
    home()

right_triangle(0, 0, 100, 80)









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


hideturtle()
done()
