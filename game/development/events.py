import random
import ruLocal as ru


EVENTS = [
    (ru.DROUGHT, {"grain": -3}),
    (ru.UNEXPECTED_PROFIT, {"money": +5}),
    (ru.EPIDEMIC, {"people": -3, "smuta": +2}),
    (ru.BOUNTIFUL_HARVEST, {"grain": +5}),
    (ru.PEASANT_UPRISING, {"grain": -2, "smuta": +3}),
    (ru.GENEROUS_MERCHANT, {"money": +3, "land": +1}),
    (ru.TRADE_BOOM, {"money": +2, "grain": +1}),
    (ru.BORDER_CONFLICT, {"people": -2, "smuta": +2}),
    (ru.CRAFT_DEVELOPMENT, {"money": +2}),
    (ru.POLITICAL_CRISIS, {"smuta": +3}),
]
def random_event():
    title, effects = random.choice(EVENTS)
    return title, effects

def apply_event(player, effects):
    parts = []
    for resource, delta in effects.items():
        player.change(resource, delta)
        sign = "+" if delta >= 0 else ""
        parts.append(f"{resource} {sign}{delta}")
    return ", ".join(parts)

