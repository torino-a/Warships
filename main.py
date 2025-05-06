import json
import copy

from battle.battle_logger import logo
from fleets import fleet_team1, fleet_team2
from utils.helpers import get_coordinates, get_azimuth, dict_to_ship
from battle.battle_engine import battle

with open('ships.json', 'r', encoding='utf-8') as file:
    ships_data = json.load(file)

logo()

while True:
    try:
        # запрашиваем  у пользователя, чтобы определить режим боя
        user_choice = int(input("Выберите режим боя! (1 - Дуэль, 2 - Командный бой): "))
        if user_choice in (1, 2):
            ship_count = 1 if user_choice == 1 else int(input("Сколько кораблей в каждой команде? "))
            break
        else:
            print("Введите 1 или 2!")
    except ValueError:
        print("Ошибка! Введите число.")

# Цикл выбора и создания кораблей для обеих команд
for _ in range(ship_count):
    for team_num, fleet in [(1, fleet_team1), (2, fleet_team2)]:
        while True:
            # Пользователь вводит имя корабля (в нижнем регистре для сопоставления с ключами словаря)
            ship_name = input(f"Введите имя корабля(Hood,Belfast,Hipper,Bismarck) для команды {team_num}: ").lower()
            if ship_name in ships_data:
                # Создаём копию шаблона корабля, чтобы избежать изменения оригинальных данных
                ship = copy.deepcopy(ships_data[ship_name])
                # Нумерация команды
                ship["team"] = team_num
                # Запрашиваем координаты и азимут у пользователя
                ship["x"], ship["y"] = get_coordinates()
                ship["azimuth"] = get_azimuth()
                fleet[ship_name] = ship
                break
            else:
                # для исключений
                print(f"{ship_name} - такого корабля нет! Повторите ввод.")

fleet_team1 = {name: dict_to_ship(data) for name, data in fleet_team1.items()}
fleet_team2 = {name: dict_to_ship(data) for name, data in fleet_team2.items()}

battle(fleet_team1, fleet_team2)
