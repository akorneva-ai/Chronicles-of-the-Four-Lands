from players import create_players
from events import random_event, apply_event
from actions import apply_action, can_perform_action
from config import WIN_PRESTIGE, LOSE_SMUTA, LOG_MAX


class Game:
    def __init__(self):
        self.players = create_players()
        self.current_index = 0
        self.turn = 1
        self.turn_number = 1
        self.game_over = False
        self.winner = None
        self.logs = []
        # Каждый ход начинается с фазы случайного события ("event") согласно Game Design (п. 7)
        self.phase = "event"
        self.pending_action = None
        self.selecting_target = False
        self.modal_visible = False
        self.modal_title = ""
        self.modal_text = ""

    def current(self):
        return self.players[self.current_index]

    def log(self, text):
        self.logs.append(text)
        if len(self.logs) > LOG_MAX:
            self.logs = self.logs[-LOG_MAX:]

    def check_over(self):
        for p in self.players:
            if not p.dead:
                if p.smuta >= LOSE_SMUTA or p.people <= 0:
                    p.dead = True
                    self.log(f"{p.name}: Погибло!")

        alive = [p for p in self.players if not p.dead]

        if len(alive) == 1:
            self.game_over = True
            self.winner = alive[0]
            return
        elif len(alive) == 0:
            self.game_over = True
            self.winner = None
            return

        for p in alive:
            if int(p.prestige) >= WIN_PRESTIGE:
                self.game_over = True
                self.winner = p
                return

    def event(self):
        actor = self.current()
        title, effects = random_event()
        text = apply_event(actor, effects)
        log_entry = f"[Ход {self.turn_number}] {actor.name} — {title} ({text})"
        self.log(log_entry)
        self.modal_title = title
        self.modal_text = f"{actor.name}: «{title}» ({text})"
        self.modal_visible = True
        self.check_over()
        return text

    def can_act(self, action_id):
        return can_perform_action(action_id, self.current(), self.turn_number)

    def act(self, action_id, target):
        if not self.can_act(action_id):
            self.log("Недостаточно ресурсов или действие перезаряжается!")
            return False
        text = apply_action(action_id, self.current(), target, self.turn_number)
        self.log(text)
        self.check_over()

        if not self.game_over:
            self.next_turn()
        return True

    def next_turn(self):
        prev_index = self.current_index
        for _ in range(len(self.players)):
            self.current_index = (self.current_index + 1) % len(self.players)
            if not self.current().dead:
                break
        self.turn += 1
        if self.current_index <= prev_index:
            self.turn_number += 1

    def commit_action(self, action_id, target):
        success = self.act(action_id, target)
        self.pending_action = None
        self.selecting_target = False
        if success and not self.game_over:
            # Следующий игрок начинает свой ход со случайного события
            self.phase = "event"
        else:
            self.phase = "action"

    def do_event_phase(self):
        self.event()
        # Если текущий игрок погиб от самого события, сразу передаём ход следующему живому игроку
        if not self.game_over and self.current().dead:
            self.next_turn()
            self.phase = "event"
        else:
            self.phase = "action"

    def advance_turn(self):
        self.next_turn()
        self.phase = "event"
