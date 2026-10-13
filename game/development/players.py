from config import (
    START_GRAIN,
    START_MONEY,
    START_LAND,
    START_PEOPLE,
    START_SMUTA,
    WIN_PRESTIGE,
    LOSE_SMUTA,
)
import ruLocal as ru


class CallableInt(int):
    """Число, которое можно и сравнивать как свойство (p.prestige), и вызывать как метод (p.prestige())."""

    def __call__(self):
        return int(self)


class Player:
    def __init__(self, name, color=(255, 255, 255)):
        self.name = name
        self.color = color
        self.grain = START_GRAIN
        self.money = START_MONEY
        self.land = START_LAND
        self.people = START_PEOPLE
        self.smuta = START_SMUTA
        self._dead = False
        self.last_bribe_turn = -10

    @property
    def prestige(self):
        val = (self.land * 2) + (self.money // 5) + (self.people // 5) - self.smuta
        return CallableInt(val)

    @property
    def is_dead(self):
        if self._dead or self.smuta >= LOSE_SMUTA or self.people <= 0:
            self._dead = True
        return self._dead

    @is_dead.setter
    def is_dead(self, value):
        self._dead = bool(value)

    @property
    def dead(self):
        return self.is_dead

    @dead.setter
    def dead(self, value):
        self._dead = bool(value)

    def change(self, resource, delta):
        value = getattr(self, resource) + delta
        setattr(self, resource, max(0, value))
        self.update_dead()

    def update_dead(self):
        if self.smuta >= LOSE_SMUTA or self.people <= 0:
            self._dead = True

    def has_won(self):
        return not self.is_dead and int(self.prestige) >= WIN_PRESTIGE


def create_players():
    return [
        Player(ru.NORTH, (255, 100, 100)),
        Player(ru.EAST, (100, 140, 255)),
        Player(ru.SOUTH, (100, 220, 120)),
        Player(ru.WEST, (240, 210, 90)),
    ]
