import math

class Position:
    def __init__(self, x, y, azimuth):
        self.x = x
        self.y = y
        self.azimuth = azimuth

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def move(self, speed):
        rad = math.radians(self.azimuth)
        self.x += speed * math.cos(rad)
        self.y += speed * math.sin(rad)