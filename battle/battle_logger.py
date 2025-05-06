from battle.battle_logo_art import game_logo


def logo():
    print(game_logo)

def log_round_start(round_number):
    print(f"\n⚔️ Раунд {round_number}")


def log_distance(attacker_name, target_name, distance):
    # Применяем title() для корректного вывода имени с заглавной буквы
    attacker_name = attacker_name.title()  # Преобразуем в формат с заглавной буквы
    target_name = target_name.title()  # Преобразуем в формат с заглавной буквы
    print(f"📏 Расстояние между {attacker_name} и {target_name}: {distance:.2f}")


def log_attack(attacker_name, target_name, damage, remaining_hp):
    # Применяем title() для корректного вывода имени с заглавной буквы
    attacker_name = attacker_name.title()
    target_name = target_name.title()
    print(f"💥 {attacker_name} атакует {target_name} и наносит {damage} урона. Осталось HP: {max(0, remaining_hp)}")


def log_ship_sunk(ship_name):
    print(f"☠️ {ship_name} потоплен!")


def log_no_attacks():
    print("🤝 Ничья! Бой завершён: ни один корабль не смог атаковать.")


def log_battle_result(team1_alive, team2_alive):
    print("\n🏁 Бой окончен!")
    if team1_alive and not team2_alive:
        print("🎉 Победила команда 1!")
    elif team2_alive and not team1_alive:
        print("🎉 Победила команда 2!")
    else:
        print("🤝 Ничья! Все корабли потоплены.")
