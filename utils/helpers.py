from model.ship import Ship
from model.position import Position

def dict_to_ship(data: dict) -> Ship:
    position = Position(data["x"], data["y"], data["azimuth"])
    return Ship(
        name=data["name"],
        nation=data["nation"],
        ship_class=data["ship_class"],
        position=position,
        health_points=data["health_points"],
        speed=data["speed"],
        base_damage=data["base_damage"],
        attack_distance=data["attack_distance"]
    )

def get_coordinates():
    while True:
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            return x, y
        except ValueError:
            print("Ошибка! Введите целые числа.")

def get_azimuth():
    while True:
        try:
            azimuth = int(input("Введите азимут (0–360): "))
            if 0 <= azimuth <= 360:
                return azimuth
            print("Азимут должен быть от 0 до 360.")
        except ValueError:
            print("Ошибка! Введите число.")
