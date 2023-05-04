import turtle
import time

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

for x in range(0, WIDTH):
    Plotter.sety(-200)
    Plotter.setx(x-300)
    for y in range(0, HEIGHT):
        c = complex(-2 + (x / WIDTH) * (3),
                    -1 + (y / HEIGHT) * (2))
        m = mandelbrot(c)
        color = 255 - int((m * 255) / MAX_ITER)
        color = (color/2) +100
        color = int(color)
        Plotter.color(color,color,color)
        Plotter.forward(1)
        Plotter.down()
    Plotter.up()

time.sleep(100)