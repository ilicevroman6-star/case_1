#Белявская Алиса, Пимшина Дарья, Макарова Анастасия, Ильичёв Роман
from turtle import *
from math import sqrt
from math import acos
from math import degrees
from math import atan
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
#трапеция, а - нижнее основание, в - верхнее основание
def trapezoid(x, y, a, b):
    up()
    setposition(x, y)
    down()
    pencolor('purple')
    fillcolor('purple')
    begin_fill()
    forward(a)
    left(120)
    forward(100)
    left(60)
    forward(b)
    left(60)
    forward(100)
    end_fill()
    up()
    home()
#ромб, а - стороны
def rhombus(x, y, a):
    color('cyan')
    up()
    setposition(x, y)
    down()
    pencolor('cyan')
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


#квадрат, а - сторона
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
    up()
    home()
    down()


#прямоугольный треугольник, a, b - катеты
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
    o = degrees(atan(a / b))
    left(180 - o)
    forward(c)
    end_fill()
    up()
    home()
#рыба
def fish():
    left(-60)
    parallelogram(-290, -215, -45, -27)
    rhombus(-290, -215, 27)
    left(180)
    right_triangle(-290, -215, 27, 30)
    right_triangle(-346, -245, 27, 30)
    left(90)
    right_triangle(-261.5, -215, 47.5, 27)
    right_triangle(-288.5, -262.5, 27, 47.5)
    right(90)
    triangle(-261.5,-195,32.5,40)

fish()

#кот
def cat():
    right(90)
    rhombus(-160, -90, 35)
    right(90)
    triangle(-190,-60,38,47)
    left(90)
    triangle(-130,-106,38,47)
    left(90)
    triangle(-150,-185,52,64)
    right(90)
    triangle(-148,-121,70,115)
    right_triangle(-174, -275, 71, 100)
    parallelogram(-103, -275, 50, 45)

cat()

# рисунок "самолёт"

def plane():
    parallelogram(20, 200, 60, 35)
    equilateral_triangle(84, 200, 35)
    right_triangle(107, 230, 55, 95)
    left(90)
    right_triangle(162, 133, 95, 55)
    square(165, 205, 35)
    left(180)
    right_triangle(243, 240, 40, 35)
    right_triangle(193, 243, 50, 35)

plane()

# рисунок "вертолёт"

def helicopter():
    left(45)
    square(45, 43, 40)
    left(180)
    triangle(112, 53, 35, 52)
    triangle(91, 30, 35, 52)
    left(90)
    triangle(175, 5, 74, 100)
    left(270)
    triangle(180, 105, 74, 100)
    parallelogram(180, 110, 55, 35)
    triangle(110, 110, 50, 65)


helicopter()
hideturtle()


done()











