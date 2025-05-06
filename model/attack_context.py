from model.ship import Ship


class AttackContext:
    def __init__(self, attacker: "Ship", target: "Ship"):
        self.attacker = attacker
        self.target = target

    def calculate_damage(self) -> int:

        base_damage = self.attacker.base_damage
        distance = self.attacker.position.distance_to(self.target.position)

        # Cпец. условия для Bismarck и Hood
        if self.attacker.name == "Bismarck" and self.target.name == "Hood" and 15 <= distance <= 18:
            base_damage *= 2  # Bismarck наносит двойной урон по Hood

        base_damage = self.apply_class_modifiers(base_damage, distance)

        # Модификаторы нации
        base_damage = self.apply_nation_modifiers(base_damage, distance)

        return max(0, round(base_damage))


    def apply_class_modifiers(self, damage: float, distance: float) -> float:
        if self.attacker.ship_class == "Cruiser" and distance <= 5:
            damage *= 4  # Увеличение на близкой дистанции
        elif self.attacker.ship_class == "Battleship" and distance > 10:
            damage -= (distance - 10) * 100  # Потеря бронепробития
        return damage

    def apply_nation_modifiers(self, damage: float, distance: float) -> float:
        nation = self.target.nation.strip()

        if nation == "uk" and distance > 8:
            damage *= 0.5  # уменьшение урона на 50%
        elif nation == "german":
            damage *= 0.8  # уменьшение урона на 20%

        return damage



