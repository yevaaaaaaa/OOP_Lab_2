from turtle import *
from random import randint
from triangle import Triangle

def createTriangles(number):
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
    triangles = []
    for i in range(number):
        x1 = randint(-bound, bound)
        y1 = randint(-bound, bound)
        x2 = randint(-bound, bound)
        y2 = randint(-bound, bound)
        t = Triangle(x1, y1, x2, y2)
        color_num = randint(0, len(colors) - 1)
        t.set_color(colors[color_num])
        triangles.append(t)
    return triangles

if __name__ == '__main__':

    triangles = createTriangles(100)
    for t in triangles:
        bound = 100
        x0 = randint(-bound, bound)
        y0 = randint(-bound, bound)
        t.set_position(x0, y0)
        t.draw()

    mainloop()