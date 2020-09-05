import Fortuna as rng


class Weapon:
    weapons = rng.TruffleShuffle([
        'Cutlass', 'Hook', 'Steam Powered Flint Lock', 'Knife', 'Cannon',
        'Musket', 'Black-powder Blunderbuss', 'Dagger', 'Scimitar',
        'Boarding Axe',
    ])

    def __init__(self):
        self.name = self.weapons()

    def __str__(self):
        return self.name


if __name__ == '__main__':
    w = Weapon()
    print(w)
