import sys
from pathlib import Path
import pygame

# Обеспечиваем корректные импорты независимо от того, откуда запущен скрипт
DEV_DIR = Path(__file__).resolve().parent
if str(DEV_DIR) not in sys.path:
    sys.path.insert(0, str(DEV_DIR))

from config import (
    WIDTH,
    HEIGHT,
    FPS,
    PLAYER_PANEL_X,
    PLAYER_PANEL_Y0,
    PLAYER_PANEL_W,
    PLAYER_PANEL_H,
    PLAYER_PANEL_STEP,
    init_fonts,
)
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
        rect = pygame.Rect(
            PLAYER_PANEL_X,
            PLAYER_PANEL_Y0 + i * PLAYER_PANEL_STEP,
            PLAYER_PANEL_W,
            PLAYER_PANEL_H,
        )
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
    if game.phase != "action" or game.game_over or game.modal_visible:
        return
    for action_id, info in ACTIONS.items():
        if info["rect"].collidepoint(pos):
            if not game.can_act(action_id):
                game.log("Недостаточно ресурсов (или подкуп на перезарядке)!")
                return
            if info["target"]:
                game.pending_action = action_id
                game.selecting_target = True
                game.phase = "target"
            else:
                game.commit_action(action_id, None)
            return


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(ru.CHRONICLES_FOUR_LANDS)
    clock = pygame.time.Clock()
    init_fonts()

    game = Game()
    running = True

    while running:
        if not game.game_over and not game.modal_visible:
            if game.phase == "event":
                game.do_event_phase()
            elif game.phase == "next":
                game.advance_turn()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if (
                game.game_over
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_r
            ):
                game = Game()
                continue
            if handle_modal_input(game, event):
                continue
            if game.selecting_target:
                handle_target_selection(game, event)
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_action_click(game, event.pos)

        draw_all(screen, game)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
