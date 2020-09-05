import Fortuna as rng
from Combat.data import DataModel
from Combat.weapons import Weapon


class Pirate:
    db = DataModel()

    def __init__(self, name, player):
        self.name = name
        self.player = str(player)
        self.weapon = Weapon()
        self.health = rng.middle_gauss(26) + 25
        self.db.push(self.to_dict())

    def __str__(self):
        return '\n  '.join(f'{k}: {v}' for k, v in self.to_dict().items())

    def to_dict(self):
        return {
            'Name': self.name,
            'Health': self.health,
            'Weapon': self.weapon.name,
            'Player': self.player,
        }
