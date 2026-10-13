import pygame

ACTIONS = {
    "A1": {
        "label": "Торговля",
        "cost_label": "-3 Д",
        "cost": {"money": 3},
        "target": True,
        "rect": pygame.Rect(30, 590, 180, 60),
    },
    "A2": {
        "label": "Подкуп",
        "cost_label": "-5 Д (раз в 3х)",
        "cost": {"money": 5},
        "target": True,
        "rect": pygame.Rect(222, 590, 180, 60),
    },
    "A3": {
        "label": "Союз",
        "cost_label": "-2 Зерна",
        "cost": {"grain": 2},
        "target": True,
        "rect": pygame.Rect(414, 590, 180, 60),
    },
    "A4": {
        "label": "Набег",
        "cost_label": "-2 Народа",
        "cost": {"people": 3},  # Чтобы после -2 народа оставался хотя бы 1 житель
        "target": True,
        "rect": pygame.Rect(606, 590, 180, 60),
    },
    "A5": {
        "label": "Пропаганда",
        "cost_label": "-3 Д",
        "cost": {"money": 3},
        "target": True,
        "rect": pygame.Rect(798, 590, 180, 60),
    },
    "A6": {
        "label": "Реформа",
        "cost_label": "Бесплатно",
        "cost": {},
        "target": False,
        "rect": pygame.Rect(990, 590, 180, 60),
    },
}


def can_perform_action(action_id, actor, turn_number=1):
    info = ACTIONS.get(action_id)
    if not info:
        return False
    for res, required in info.get("cost", {}).items():
        if getattr(actor, res, 0) < required:
            return False
    if action_id == "A2" and (turn_number - getattr(actor, "last_bribe_turn", -10)) < 3:
        return False
    return True


def apply_action(action_id, actor, target, turn_number=1):
    text = f"{actor.name}: "

    if action_id == "A1":
        actor.change("money", -3)
        actor.change("grain", +4)
        if target:
            target.change("grain", +4)
            text += f"Торговля с «{target.name}» (+4 зерна обоим)"
        else:
            text += "Торговля."
    elif action_id == "A2":
        actor.change("money", -5)
        actor.change("land", +1)
        actor.last_bribe_turn = turn_number
        if target:
            target.change("smuta", -2)
            text += f"Подкуп «{target.name}» (+1 земля, цели -2 смуты)"
        else:
            text += "Подкуп."
    elif action_id == "A3":
        actor.change("grain", -2)
        actor.change("smuta", -1)
        if target:
            target.change("smuta", -1)
            text += f"Союз с «{target.name}» (-1 смуты обоим)"
        else:
            text += "Союз."
    elif action_id == "A4":
        actor.change("people", -2)
        actor.change("grain", +3)
        actor.change("smuta", +1)
        if target:
            target.change("grain", -3)
            text += f"Набег на «{target.name}» (+3 зерна, +1 смута)"
        else:
            text += "Набег."
    elif action_id == "A5":
        actor.change("money", -3)
        actor.change("smuta", -1)
        if target:
            target.change("smuta", +1)
            text += f"Пропаганда против «{target.name}» (-1 смута, цели +1 смута)"
        else:
            text += "Пропаганда."
    elif action_id == "A6":
        actor.change("smuta", -1)
        actor.change("people", +1)
        text += "Реформа (-1 смута, +1 народ)"

    return text
