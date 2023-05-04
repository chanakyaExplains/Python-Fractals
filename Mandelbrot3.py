import turtle
import random

WIDTH = 600
HEIGHT = 400
MAX_ITER = 80
Plotter = turtle.Turtle()
Plotter.speed("fastest")
Plotter.left(90)
Plotter.showturtle()
turtle.colormode(255)
Plotter.up()

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

while (True):

    x = random.randrange(0,WIDTH)
    y = random.randrange(0,HEIGHT)

    Plotter.up()
    Plotter.setx(x-300)
    Plotter.sety(y-200)
    Plotter.down()

    c = complex(-2 + (x / WIDTH) * (3),
                    -1 + (y / HEIGHT) * (2))
    m = mandelbrot(c)
    color = 255 - int((m * 255) / MAX_ITER)
    Plotter.color(color,color,color)
    Plotter.dot(2)
