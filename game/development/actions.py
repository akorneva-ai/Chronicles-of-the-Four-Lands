import pygame
from config import BLUE
import ruLocal as ru

ACTIONS = {
    "A1": {"label": "Торговля",   "target": True,
           "rect": pygame.Rect(40,  590, 180, 55)},
    "A2": {"label": "Подкуп",     "target": True,
           "rect": pygame.Rect(240, 590, 180, 55)},
    "A3": {"label": "Союз",       "target": True,
           "rect": pygame.Rect(440, 590, 180, 55)},
    "A4": {"label": "Набег",      "target": True,
           "rect": pygame.Rect(640, 590, 180, 55)},
    "A5": {"label": "Пропаганда", "target": True,
           "rect": pygame.Rect(840, 590, 180, 55)},
    "A6": {"label": "Реформа",    "target": False,
           "rect": pygame.Rect(40,  655, 180, 40)},
}

def apply_action(action_id, actor, target):

    text = f"{actor.name}: "

    if action_id == "A1":
        actor.change("money", -3)
        actor.change("grain", +4)
        if target:
            target.change("grain", +4)
        text += "Торговля."
    elif action_id == "A2":
        actor.change("money", -5)
        actor.change("land",  +1)
        if target:
            target.change("smuta", -2)
        text += "Подкуп."
    elif action_id == "A3":
        actor.change("grain", -2)
        actor.change("smuta", -1)
        if target:
            target.change("smuta", -1)
        text += "Союз."
    elif action_id == "A4":
        actor.change("people", -2)
        actor.change("grain",  +3)
        actor.change("smuta",  +1)
        if target:
            target.change("grain", -3)
        text += "Набег."
    elif action_id == "A5":
        actor.change("money", -3)
        actor.change("smuta", -1)
        if target:
            target.change("smuta", +1)
        text += "Пропаганда."
    elif action_id == "A6":
        actor.change("smuta",  -1)
        actor.change("people", +1)
        text += "Реформа."

    return text