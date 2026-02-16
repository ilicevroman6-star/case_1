#Разработчики: Белявская Алиса, Пимшина Дарья, Макарова Анастасия, Ильичёв Роман

from turtle import *
from math import sqrt
from math import acos
from math import degrees
from math import atan
speed(7)

#параллелограмм, a,b - пары параллельных сторон; начинает рисовать с левого нижнего угла
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

#равнобедренный треугольник, b - основание, a - равные стороны; начинает рисовать с левого угла при основании
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

# прямоугольник: а - длина, b - высота 
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

#равносторонний треугольник
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

#прямоугольный треугольник, отзеркаленный относительно катета b
def right_triangle_2(x, y, a, b, color):
    up()
    setposition(x, y)
    down()
    fillcolor(color)
    pencolor(color)
    begin_fill()
    forward(a)
    right(90)
    forward(b)
    c = sqrt(a ** 2 + b ** 2) #гипотенуза
    o = degrees(atan(a / b))
    right(180 - o)
    forward(c)
    end_fill()
    up()
    home()

#рыба
def fish():
    left(-60)
    parallelogram(-293, -211, -45, -27, 'green')
    rhombus(-290, -215, 27, 'orange')
    left(180)
    right_triangle(-293, -219, 27, 30, 'pink')
    right_triangle(-353, -249, 27, 30, 'purple')
    left(90)
    right_triangle(-257.5, -214, 47.5, 27, 'red')
    right_triangle(-284.5, -263.5, 27, 47.5, 'yellow')
    right(90)
    triangle(-251.5,-195,32.5,40, 'cyan')

#кот
def cat():
    right(90)
    rhombus(-160, -90, 35, 'blue')
    right(97)
    triangle(-188,-55,38,47, 'orange')
    left(97)
    triangle(-126,-102,38,47,'red')
    left(90)
    triangle(-152,-190,52,64, 'cyan')
    right(90)
    triangle(-147,-126,70,115, 'green')
    right_triangle(-172, -285, 71, 100, 'purple')
    parallelogram(-98, -285, 50, 45, 'yellow')

# рисунок "самолёт"
def plane():
    parallelogram(20, 200, 60, 35, "skyblue")
    equilateral_triangle(84, 200, 35, "lightblue")
    right_triangle(107, 230, 55, 95, "royalblue")
    left(90)
    right_triangle(162, 133, 95, 55, "royalblue")
    square(165, 205, 35, "skyblue")
    left(180)
    right_triangle(243, 240, 40, 35, "deepskyblue")
    right_triangle(193, 243, 50, 35, "navy")

# рисунок "вертолёт"
def helicopter():
    left(45)
    square(45, 43, 40, "coral")
    left(180)
    triangle(112, 53, 35, 52, "crimson")
    triangle(91, 30, 35, 52, "crimson")
    left(90)
    triangle(175, 5, 74, 100, "maroon")
    left(270)
    triangle(180, 105, 74, 100, "firebrick")
    parallelogram(180, 110, 55, 35, "coral")
    triangle(110, 110, 50, 65, "lightcoral")

#кролик
def rabbit():
    right_triangle(-370, 180, 80, 80, "crimson")
    square(-285, 240, 40, "coral")
    parallelogram(-295, 285, 30, 50, "yellow green")
    left(180)
    right_triangle(-290, 175, 80, 80, "goldenrod")
    right(90)
    triangle(-285, 205, 40, 60, "hot pink")
    right_triangle(-365, 95, 50, 50, "light slate blue")
    left(180)
    right_triangle_2(-280, 95, 30, 30, 'orchid')

#цветок
def flower():
    left(180)
    trapezoid(-80, 135, 100, "dark olive green")
    left(180)
    trapezoid(-55, 180, 150, "pale violet red")
    rhombus(-145, 207, 30, "light cyan")
    left(90)
    trapezoid(-130, 235, 90, "khaki")
    right(90)
    trapezoid(-130, 325, 90, "khaki")
    left(90)
    equilateral_triangle(-175, 260, 40, "medium purple")
    left(30)
    equilateral_triangle(-175, 300, 50, "medium purple")
    right(30)
    equilateral_triangle(-130, 325, 50, "medium purple")
    right(90)
    equilateral_triangle(-85, 298, 40, "medium purple")
    right(30)
    equilateral_triangle(-130, 235, 50, "medium purple")
    left(150)
    equilateral_triangle(-130, 233, 50, "medium purple")

#робот
def robot():
    square(60, -245, 70, "green")
    triangle(60, -170, 50, 65, 'blue')
    rectangle(27, -244, 30, 70, 'red')
    rectangle(134, -244, 30, 70, 'pink')
    rectangle(65, -318, 20, 70, 'orange')
    rectangle(100, -318, 20, 70, 'yellow')
    rhombus(82, -210, 25, 'purple')

#ракета
def rocket():
    equilateral_triangle(209, -140, 50, "green")
    left(90)
    right_triangle(260, -198, 54, 55, 'blue')
    right(90)
    triangle(207, -150, 65, 90, 'red')
    left(90)
    triangle(257, -288, 65, 90, 'pink')
    left(45)
    square(207, -309, 45, 'orange')
    left(45)
    right_triangle(190, -328, 25, 50, 'yellow')
    right(90)
    parallelogram(260, -240, 50, 43, 'purple')

hideturtle()

rabbit()
flower()
fish()
cat()
plane()
helicopter()
robot()
rocket()

done()


