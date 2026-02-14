#Белявская Алиса, Пимшина Дарья, Макарова Анастасия, Ильичёв Роман
from turtle import *
from math import sqrt
from math import acos
from math import degrees
speed(2)

#параллелограмм, a,b - пары параллельных сторон
def parallelogram(x, y, a, b):
    fillcolor('yellow')
    pencolor('yellow')
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

#равнобедренный треугольник, b - основание, a - равные стороны
def triangle(x, y, a, b):
    fillcolor('blue')
    pencolor('blue')
    begin_fill()
    up()
    goto(x, y)
    down()
    t1 = degrees(acos(b / (2 * a))) #величина угла при основании в градусах
    t2 = degrees(acos(1 - (b**2 / (2 * a**2)))) #величина угла между равными сторонами в градусах
    forward(b)
    left(180 - t1)
    forward(a)
    left(180 - t2)
    forward(a)
    end_fill()
    up()
    home()

def rectangle(x, y, a, b):
    #a - длина прямоугольника, b - высота прямоугольника
    goto(x, y)
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
    c = sqrt(a ** 2 + b ** 2) #гипотенуза
    forward(c)
    left(135)
    end_fill()
    home()

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

hideturtle()
right_triangle(0, 0, 100, 80)
square(0, 0, 50)
parallelogram(10,40,50,45)
triangle(-50,-40,80,50)
rectangle(10,40,50,45)
equilateral_triangle(10,40,50)
trapezoid(-150, 0, 200)
rhombus(100, 0, 100)

done()

