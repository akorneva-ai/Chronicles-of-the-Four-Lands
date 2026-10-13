from config import (START_GRAIN, START_MONEY, START_LAND,
                    START_PEOPLE, START_SMUTA,
                    WIN_PRESTIGE, LOSE_SMUTA)
import ruLocal as ru


class Player:

    def __init__(self, name, color):
        self.name   = name
        self.color  = color
        self.grain  = START_GRAIN
        self.money  = START_MONEY
        self.land   = START_LAND
        self.people = START_PEOPLE
        self.smuta  = START_SMUTA
        self.dead   = False

    def prestige(self):
        return self.land * 2 + self.money // 5 + self.people // 5 - self.smuta

    def change(self, resource, delta):
        value = getattr(self, resource) + delta
        setattr(self, resource, max(0, value))

    def update_dead(self):
        if self.smuta >= LOSE_SMUTA or self.people <= 0:
            self.dead = True

    def has_won(self):
        return self.prestige() >= WIN_PRESTIGE


def create_players():
    return [
        Player(ru.NORTH, (255, 100, 100)),
        Player(ru.EAST, (100, 100, 255)),
        Player(ru.SOUTH, (100, 255, 100)),
        Player(ru.WEST, (255, 255, 100)),
    ]