from turtle import *
from random import randint
import math
import turtle
import time
from triangle import Triangle

def create_triangle():
    colors = [
        "green yellow",
        "teal",
        "deep pink",
        "rosy brown",
        "red",
        "green",
        "black",
    ]

    bound = 350
    x1 = randint(-bound, bound)
    y1 = randint(-bound, bound)
    x2 = randint(-bound, bound)
    y2 = randint(-bound, bound)
    t = Triangle(x1, y1, x2, y2)
    color_num = randint(0, len(colors) - 1)
    t.set_color(colors[color_num])
    
    return t

if __name__ == '__main__':
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.tracer(0, 0)  

    t = create_triangle()
    t.set_position(0, 0)

    for angle in range(0, 360, 5):
        t.set_rotation(math.radians(angle))
        turtle.clear()
        t.draw()
        turtle.update()
        time.sleep(0.05)
        
    for scale_factor in range(1, 10):
        t.set_scale(scale_factor, scale_factor)
        turtle.clear()
        t.draw()
        turtle.update()
        time.sleep(0.05)

    turtle.mainloop()