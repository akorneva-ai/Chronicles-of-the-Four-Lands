import random
import ruLocal as ru

# Список из 10 событий согласно docs/game_design.md (5 положительных, 5 отрицательных)
EVENTS = [
    (ru.DROUGHT, {"grain": -3}, False),
    (ru.UNEXPECTED_PROFIT, {"money": +5}, True),
    (ru.EPIDEMIC, {"people": -3, "smuta": +2}, False),
    (ru.BOUNTIFUL_HARVEST, {"grain": +5}, True),
    (ru.PEASANT_UPRISING, {"grain": -2, "smuta": +3}, False),
    (ru.GENEROUS_MERCHANT, {"money": +3, "land": +1}, True),
    (ru.TRADE_BOOM, {"money": +2, "grain": +1}, True),
    (ru.BORDER_CONFLICT, {"people": -2, "smuta": +2}, False),
    (ru.CRAFT_DEVELOPMENT, {"money": +2}, True),
    (ru.POLITICAL_CRISIS, {"smuta": +3}, False),
]


def random_event():
    title, effects, _is_positive = random.choice(EVENTS)
    return title, effects


def roll_event():
    """Возвращает True для положительного события и False для отрицательного (вероятность 50/50)."""
    _title, _effects, is_positive = random.choice(EVENTS)
    return is_positive


def apply_event(player, effects):
    parts = []
    for resource, delta in effects.items():
        player.change(resource, delta)
        sign = "+" if delta >= 0 else ""
        res_name = ru.RESOURCE_NAMES.get(resource, resource)
        parts.append(f"{res_name} {sign}{delta}")
    return ", ".join(parts)
