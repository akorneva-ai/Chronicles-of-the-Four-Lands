from players import create_players
from events import random_event, apply_event
from actions import apply_action
from config import WIN_PRESTIGE, LOSE_SMUTA

class Game:
    def __init__(self):
        self.players = create_players()
        self.current_index = 0
        self.turn = 1
        self.turn_number = 1
        self.game_over = False
        self.winner = None
        self.logs = []
        self.phase = "action"
        self.pending_action = None
        self.selecting_target = False
        self.modal_visible = False
        self.modal_text = ""

    def current(self):
        return self.players[self.current_index]

    def log(self, text):
        self.logs.append(text)

    def check_over(self):
        for p in self.players:
            if not p.dead:
                if p.smuta >= LOSE_SMUTA or p.people <= 0:
                    p.dead = True
                    self.log(p.name + ": Погибло")

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
            if p.prestige() >= WIN_PRESTIGE:
                self.game_over = True
                self.winner = p
                return

    def event(self):
        title, effects = random_event()
        text = apply_event(self.current(), effects)
        self.log(f"{title}: {text}")
        self.check_over()
        return text

    def act(self, action_id, target):
        text = apply_action(action_id, self.current(), target)
        self.log(text)
        self.check_over()

        if not self.game_over:
            self.next_turn()

    def next_turn(self):
        for _ in range(len(self.players)):
            self.current_index = (self.current_index + 1) % len(self.players)
            if not self.current().dead:
                break
        self.turn += 1

    def commit_action(self, action_id, target):
        self.act(action_id, target)
        self.pending_action = None
        self.selecting_target = False
        self.phase = "action"

    def do_event_phase(self):
        self.event()
        self.phase = "action"

    def advance_turn(self):
        self.next_turn()
        self.phase = "event"
        self.turn_number += 1