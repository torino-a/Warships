from model.position import Position


class Ship:
    def __init__(self, name: str, nation: str, ship_class: str, position: Position, base_damage: int, attack_distance: int,
                 health_points: int, speed: float):
        self.name = name
        self.ship_class = ship_class
        self.nation = nation
        self.position = position
        self.base_damage = base_damage
        self.attack_distance = attack_distance
        self.health_points = health_points
        self.speed = speed

    @staticmethod
    def from_dict(data: dict) -> "Ship":
        """Этот метод создаёт экземпляр класса Ship из словаря данных."""
        from model.position import Position
        position = Position(data["x"], data["y"], data["azimuth"])
        return Ship(
            name=data["name"],
            ship_class=data["ship_class"],
            nation=data["nation"],
            base_damage=data["base_damage"],
            speed=data["speed"],
            attack_distance=data["attack_distance"],
            health_points=data["health_points"],
            position=position
        )



