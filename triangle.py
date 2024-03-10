from turtle import *
import math

class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)
        self._color = "black"
        self.rotation = 0  # Додано обертання, радіани
        self.scale = (1, 1)  # Додано масштабування, масштаб по осям x та y

    def translate(self, dx, dy):
        self._position = (self._position[0] + dx, self._position[1] + dy)

    def set_position(self, x, y):
        self._position = (x, y)

    def set_color(self, color):
        self._color = color

    def set_rotation(self, rotation):  # значення в радіанах
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):  # значення розтягу по осях x та y відповідно
        self.scale = (scale_x, scale_y)

    def calc_absolute_position(self, vertex):
        # Масштабування
        scaled_x = vertex[0] * self.scale[0]
        scaled_y = vertex[1] * self.scale[1]
        # Обертання
        rotated_x = scaled_x * math.cos(self.rotation) - scaled_y * math.sin(self.rotation)
        rotated_y = scaled_x * math.sin(self.rotation) + scaled_y * math.cos(self.rotation)
        # Переміщення
        x = self._position[0] + rotated_x
        y = self._position[1] + rotated_y
        return x, y

    def draw(self):
        v0 = self.calc_absolute_position((0, 0))
        v1 = self.calc_absolute_position(self._vertex1)
        v2 = self.calc_absolute_position(self._vertex2)
        up()
        pencolor(self._color)
        setpos(*v0)
        down()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        up()

