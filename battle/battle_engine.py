from model.position import Position
from model.attack_context import AttackContext
from battle.battle_logger import (
    log_round_start,
    log_distance,
    log_attack,
    log_ship_sunk,
    log_no_attacks,
    log_battle_result, logo
)
import time


def battle(team1, team2):
    round_number = 1
    logo()

    while True:
        log_round_start(round_number)
        attacked_this_round = False
        attacked_ships = set()

        # Атака команды 1
        for attacker_name, attacker in team1.items():
            if attacker_name in attacked_ships or attacker.health_points <= 0:
                continue
            for target_name, target in team2.items():
                if target.health_points <= 0:
                    continue

                distance = attacker.position.distance_to(target.position)
                log_distance(attacker_name, target_name, distance)

                if distance <= attacker.attack_distance:
                    attack_context = AttackContext(attacker, target)
                    damage = attack_context.calculate_damage()
                    target.health_points -= damage

                    log_attack(attacker_name, target_name, damage, target.health_points)

                    if target.health_points <= 0:
                        log_ship_sunk(target_name)

                    attacked_ships.add(attacker_name)
                    attacked_this_round = True
                    break

        # Атака команды 2
        for attacker_name, attacker in team2.items():
            if attacker_name in attacked_ships or attacker.health_points <= 0:
                continue
            for target_name, target in team1.items():
                if target.health_points <= 0:
                    continue

                distance = attacker.position.distance_to(target.position)
                log_distance(attacker_name, target_name, distance)

                if distance <= attacker.attack_distance:
                    attack_context = AttackContext(attacker, target)
                    damage = attack_context.calculate_damage()
                    target.health_points -= damage

                    log_attack(attacker_name, target_name, damage, target.health_points)

                    if target.health_points <= 0:
                        log_ship_sunk(target_name)

                    attacked_ships.add(attacker_name)
                    attacked_this_round = True
                    break

        if not attacked_this_round:
            log_no_attacks()
            break

        # Движение
        for fleet in [team1, team2]:
            for ship in fleet.values():
                if ship.health_points <= 0:
                    continue
                ship.position.move(ship.speed)

        # Победа/ничья
        team1_alive = any(ship.health_points > 0 for ship in team1.values())
        team2_alive = any(ship.health_points > 0 for ship in team2.values())

        if not team1_alive or not team2_alive:
            log_battle_result(team1_alive, team2_alive)
            break

        round_number += 1
        time.sleep(1)
