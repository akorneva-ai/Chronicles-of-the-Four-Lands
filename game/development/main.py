import pygame

from config import WIDTH, HEIGHT, FPS, init_fonts
from game import Game
from render import draw_all
from actions import ACTIONS
import ruLocal as ru

def handle_modal_input(game, event):
    if not game.modal_visible:
        return False
    if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
        game.modal_visible = False
        if not game.game_over:
            game.phase = "action"
    return True

def find_target(game, pos):
    for i, p in enumerate(game.players):
        rect = pygame.Rect(880, 130 + i * 120, 290, 100)
        if rect.collidepoint(pos) and p is not game.current() and not p.dead:
            return p
    return None

def handle_target_selection(game, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        game.selecting_target = False
        game.pending_action = None
        game.phase = "action"
        return

    if event.type == pygame.MOUSEBUTTONDOWN:
        target = find_target(game, event.pos)
        if target:
            game.commit_action(game.pending_action, target)

def handle_action_click(game, pos):
    if game.phase != "action" or game.game_over:
        return
    for action_id, info in ACTIONS.items():
        if info["rect"].collidepoint(pos):
            if info["target"]:
                game.pending_action = action_id
                game.selecting_target = True
                game.phase = "target"
            else:
                game.commit_action(action_id, None)
            return

def handle_target_selection(game, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        game.selecting_target = False
        game.pending_action = None
        game.phase = "action"
        return
    if event.type == pygame.MOUSEBUTTONDOWN:
        target = find_target(game, event.pos)
        if target:
            game.commit_action(game.pending_action, target)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(ru.CHRONICLES_FOUR_LANDS)
    clock = pygame.time.Clock()
    init_fonts()

    game = Game()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if handle_modal_input(game, event):
                continue
            if game.selecting_target:
                handle_target_selection(game, event)
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_action_click(game, event.pos)
        if not game.game_over:
            if game.phase == "event":
                game.do_event_phase()
            elif game.phase == "next":
                game.advance_turn()

        draw_all(screen, game)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()