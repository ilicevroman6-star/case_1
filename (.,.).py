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
    color("blue")
    fillcolor('blue')
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
    home()

def trapezoid(x, y, a):
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
trapezoid(-150, 0, 200)
rhombus(100, 0, 100)

done()




from turtle import *
import math

speed(1)
fillcolor("orange")
pencolor("orange")

def right_triangle_by_angles(x, y, angle1, angle2, side_length):
    """
    x, y - координаты начала
    angle1, angle2 - острые углы треугольника (в градусах)
    """
    up()
    setposition(x, y)
    down()
    color("orange")
    fillcolor("orange")
    pencolor("orange")
    begin_fill()

    # Переводим углы в радианы для расчетов
    rad1 = math.radians(angle1)
    rad2 = math.radians(angle2)

    # Вычисляем длины катетов
    a = side_length # первый катет
    b = a * math.tan(rad2)  # второй катет
    c = a / math.cos(rad2)  # гипотенуза

    forward(a)
    left(90)
    forward(b)
    forward(c)

    left(180 - angle1)  # возвращаем черепаху в исходное направление

    end_fill()
    home()

right_triangle_by_angles(0, 0, 30, 60, 50)

hideturtle()
done()


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

