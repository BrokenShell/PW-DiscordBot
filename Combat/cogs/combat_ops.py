"""
Steam Punk Pirates

Swords and Steam powered pistols.
"""
from Fortuna import dice


def turn(defense: dict):
    roll_offence, roll_defense = dice(1, 20), dice(1, 20)

    if roll_offence > roll_defense:
        damage = dice(1, 10)
        defense['Health'] = max(defense['Health'] - damage, 0)
    return defense


def combat_round(player_1, player_2):
    player_2 = turn(player_2)
    player_1 = turn(player_1)
    return player_1, player_2


def combat(player: dict, target: dict):
    init_roll_a, init_roll_b = dice(1, 20), dice(1, 20)
    while init_roll_a == init_roll_b:
        init_roll_a, init_roll_b = dice(1, 20), dice(1, 20)

    while player['Health'] > 0 and target['Health'] > 0:
        if init_roll_a > init_roll_b:
            player, target = combat_round(player, target)
        else:
            target, player = combat_round(target, player)

    if player['Health'] > 0:
        return player['Name']
    elif target['Health'] > 0:
        return target['Name']
    else:
        return 'Tie'


if __name__ == '__main__':
    jim = {'Name': 'Jim', 'Health': 10}
    joe = {'Name': 'Joe', 'Health': 10}
    print(combat(jim, joe))
