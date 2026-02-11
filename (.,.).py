#Белявская Алиса, Пимшина Дарья, Макарова Анастасия, Ильичёв Роман
from turtle import *
speed(1)
def parallelogram(x, y, a, b):
    fillcolor('yellow')
    begin_fill()
    up()
    goto(x, y)
    down()
    forward(a)
    left(60)
    forward(b)
    left(120)
    forward(a)
    left(60)
    forward(b)
    end_fill()
    up()
    home()

def triangle(x, y, a, b):
    fillcolor('blue')
    begin_fill()
    up()
    goto(x, y)
    down()
    forward(a)
    left(143)
    forward(b)
    left(74)
    forward(b)
    left(143)
    up()
    end_fill()
    home()

def rectangle(x, y, a, b):
    #a - длина прямоугольника, b - высота прямоугольника
    down()
    color("red")
    fillcolor('red')
    begin_fill()

    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)

    end_fill()
    up()
    home()


def equilateral_triangle(x, y, a):
    #a - длина стороны треугольника
    color("green")
    fillcolor("green")
    up()
    setposition(x, y)  #начальная точка
    down()

    begin_fill()

    forward(a)
    left(120)
    forward(a)
    left(120)
    forward(a)

    end_fill()
    up()
    home()

def trapezoid(x, y, a):
    color('purple')
    up()
    setposition(x, y)
    down()
    fillcolor('purple')
    begin_fill()
    forward(a)
    left(120)
    forward(a / 2)
    left(60)
    forward(a / 2)
    left(60)
    forward(a / 2)
    left(60)
    end_fill()
    up()
    home()

def rhombus(x, y, a):
    color('cyan')
    up()
    setposition(x, y)
    down()
    fillcolor('cyan')
    begin_fill()
    right(60)
    for _ in range(2):
        forward(a)
        left(120)
        forward(a)
        left(60)
    end_fill()
    up()
    home()

hideturtle()
parallelogram(10,40,50,45)
triangle(-50,-40,80,50)
rectangle(10,40,50,45)
equilateral_triangle(10,40,50)
trapezoid(-150, 0, 200)
rhombus(100, 0, 100)

done()

