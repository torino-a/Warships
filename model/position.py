import math

class Position:
    def __init__(self, x, y, azimuth):
        self.x = x
        self.y = y
        self.azimuth = azimuth

    def distance_to(self, other):
        """вычисление дистанци между кораблями через формулу "Евклидово расстояние" d(p,q) = ((p1 - q1)**2 + (p2-q2)**2)**1/2 , d(p,q) = дистанция между коряблями"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def move(self, speed):
        # вычисление радианы
        rad = math.radians(self.azimuth)
        # нахождение точки х по горизонтали (x = l*cos(rad), l = длина вектора)
        self.x += speed * math.cos(rad)
        # нахождение точки х по вертикали (у = l*sin(rad), l = длина вектора)
        self.y += speed * math.sin(rad)