#Белявская Алиса, Пимшина Дарья, Макарова Анастасия, Ильичёв Роман
from turtle import *
from math import sqrt
from math import acos
from math import degrees
from math import atan
speed(7)


#параллелограмм, a,b - пары параллельных сторон
def parallelogram(x, y, a, b, color):
    fillcolor(color)
    pencolor(color)
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
def triangle(x, y, a, b, color):
    fillcolor(color)
    pencolor(color)
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

# прямоугольник: а- длина, b - высота 
def rectangle(x, y, a, b, color):
    up()
    goto(x, y)
    down()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
    end_fill()
    up()
    home()

def equilateral_triangle(x, y, a, color):
    #a - длина стороны треугольника
    pencolor(color)
    fillcolor(color)
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

#трапеция, а - нижнее основание
def trapezoid(x, y, a, color):
    up()
    setposition(x, y)
    down()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    forward(a)
    left(120)
    forward(50)
    left(60)
    forward(a-50)
    left(60)
    forward(50)
    end_fill()
    up()
    home()
#ромб, а - стороны
def rhombus(x, y, a, color):
    pencolor(color)
    up()
    setposition(x, y)
    down()
    fillcolor(color)
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
def square(x, y, a, color):
    up()
    setposition(x, y)
    down()
    pencolor(color)
    fillcolor(color)
    begin_fill()

    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    up()
    home()
    down()


#прямоугольный треугольник, a, b - катеты
def right_triangle(x, y, a, b, color):
    up()
    setposition(x, y)
    down()
    pencolor(color)
    fillcolor(color)
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
    parallelogram(-290, -215, -45, -27, "green")
    rhombus(-290, -215, 27, 'orange')
    left(180)
    right_triangle(-290, -215, 27, 30, "pink")
    right_triangle(-346, -245, 27, 30, "purple")
    left(90)
    right_triangle(-261.5, -215, 47.5, 27, "red")
    right_triangle(-288.5, -262.5, 27, 47.5, "yellow")
    right(90)
    triangle(-261.5,-195,32.5,40, "cyan")


def cat():
    right(90)
    rhombus(-160, -90, 35, "blue")
    right(90)
    triangle(-190,-60,38,47, "orange")
    left(90)
    triangle(-130,-106,38,47, "red")
    left(90)
    triangle(-150,-185,52,64, "cyan")
    right(90)
    triangle(-148,-121,70,115, "green")
    right_triangle(-174, -275, 71, 100, "purple")
    parallelogram(-103, -275, 50, 45, "yellow")



# рисунок "самолёт"
def plane():
    parallelogram(20, 200, 60, 35, "blue")
    equilateral_triangle(84, 200, 35, "lightblue")
    right_triangle(107, 230, 55, 95, "blue")
    left(90)
    right_triangle(162, 133, 95, 55, "blue")
    square(165, 205, 35, "green")
    left(180)
    right_triangle(243, 240, 40, 35, "blue")
    right_triangle(193, 243, 50, 35, "lightblue")


# рисунок "вертолёт"
def helicopter():
    left(45)
    square(45, 43, 40, "red")
    left(180)
    triangle(112, 53, 35, 52, "orange")
    triangle(91, 30, 35, 52, "yellow")
    left(90)
    triangle(175, 5, 74, 100, "red")
    left(270)
    triangle(180, 105, 74, 100, "green")
    parallelogram(180, 110, 55, 35, "blue")
    triangle(110, 110, 50, 65, "salmon")

def rabbit():
    right_triangle(-370,180,80,80, "purple")
    square(-285, 240,40, "black")
    left(180)
    parallelogram(-265, 285, 30, 50, "yellow")
    left(180)
    right_triangle(-290, 175, 80, 80, "blue")
    right(90)
    triangle(-285, 205, 40, 60, "green")
    right_triangle(-365, 95, 50, 50, "red")
    left(180)
    

def flower():
    
    trapezoid(-80, 135, 100, "yellow")
    left(180)
    trapezoid(-55, 180, 150, "blue")
    rhombus(-145, 207, 30, "red")
    left(90)
    trapezoid(-130, 235, 90, "purple")
    right(90)
    trapezoid(-130, 325, 90, "purple")
    left(90)
    equilateral_triangle(-175, 260, 40, "green")
    left(30)
    equilateral_triangle(-175,300,50, "green")
    right(30)
    equilateral_triangle(-130, 325, 50, "green")
    right(90)
    equilateral_triangle(-85, 298, 40, "green")
    right(30)
    equilateral_triangle(-130, 235, 50, "green")
    left(150)
    equilateral_triangle(-130, 233, 50, "green")

hideturtle()
rabbit()
flower()
fish()
cat()
plane()
helicopter()



done()




















