from models.player import Player
from logic.game_state import GameState

def test_initial_resources():
    p = Player("Test", (255,0,0))
    assert p.grain == 10
    assert p.money == 10
    assert p.land == 5
    assert p.people == 10
    assert p.smuta == 0

def test_prestige_formula():
    p = Player("Test", (255,0,0))
    p.land, p.money, p.people, p.smuta = 5, 10, 10, 0
    assert p.prestige == (p.land * 2) + (p.money // 5) + (p.people // 5) - p.smuta

def test_death_by_smuta():
    p = Player("Test", (255,0,0))
    p.smuta = 10
    assert p.is_dead == True

def test_death_by_zero_people():
    p = Player("Test", (255,0,0))
    p.people = 0
    assert p.is_dead == True

def test_event_distribution():
    from logic.events_pool import roll_event
    positives = sum(1 for _ in range(10000) if roll_event())
    assert 4700 < positives < 5300

def test_victory_by_prestige():
    p = Player("Test", (255,0,0))
    p.land, p.money, p.people, p.smuta = 15, 0, 0, 0
    assert p.prestige >= 30