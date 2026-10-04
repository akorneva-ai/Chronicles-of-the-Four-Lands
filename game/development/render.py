import pygame
import config
from config import (WIDTH, HEIGHT, BACKGROUND, PANEL, PANEL_LIGHT,
                    WHITE, GRAY, GOLD, RED,
                    KINGDOM_PANEL, PLAYER_PANEL_X, PLAYER_PANEL_Y0,
                    PLAYER_PANEL_W, PLAYER_PANEL_H, PLAYER_PANEL_STEP,
                    LOG_X, LOG_Y, LOG_LINE_H, LOG_MAX)

from actions import ACTIONS
from ui import draw_text, draw_panel, draw_button, wrap_text



def draw_title(screen, game):
    draw_text(screen, "ХРОНИКИ ЧЕТЫРЁХ ЗЕМЕЛЬ",
              config.title_font, GOLD, 320, 25)
    draw_text(screen, f"Ход: {game.turn_number}",
              config.small_font, GRAY, 520, 75)


def draw_kingdom_panel(screen, player):
    draw_panel(screen, KINGDOM_PANEL)
    draw_text(screen, "МОЁ КОРОЛЕВСТВО", config.header_font,
              WHITE, 65, 135)
    draw_text(screen, player.name, config.text_font,
              player.color, 65, 170)

    rows = [
        ("Зерно",  player.grain),
        ("Деньги", player.money),
        ("Земля",  player.land),
        ("Народ",  player.people),
        ("Смута",  player.smuta),
    ]
    y = 215
    for label, value in rows:
        draw_text(screen, label, config.text_font, WHITE, 65, y)
        color = RED if (label == "Смута" and value >= 5) else GOLD
        draw_text(screen, str(value), config.text_font, color, 250, y)
        y += 40

    draw_text(screen, "Престиж", config.header_font, WHITE, 65, 425)
    draw_text(screen, str(player.prestige()),
              config.header_font, GOLD, 230, 425)


def draw_players_panel(screen, game):
    for i, p in enumerate(game.players):
        rect = pygame.Rect(
            PLAYER_PANEL_X,
            PLAYER_PANEL_Y0 + i * PLAYER_PANEL_STEP,
            PLAYER_PANEL_W,
            PLAYER_PANEL_H,
        )
        border = GOLD if p is game.current else PANEL_LIGHT
        draw_panel(screen, rect, bg=PANEL, border=border)

        draw_text(screen, p.name, config.text_font,
                  p.color, rect.x + 15, rect.y + 10)

        info = (f"Еда: {p.grain}  Д: {p.money}  Земля: {p.land}  "
                f"Н: {p.people}  С: {p.smuta}")
        draw_text(screen, info, config.small_font,
                  WHITE, rect.x + 15, rect.y + 40)

        draw_text(screen, f"Престиж: {p.prestige()}",
                  config.small_font, GOLD, rect.x + 15, rect.y + 68)

        if p.dead:
            draw_text(screen, "ПОГИБЛО", config.header_font,
                      RED, rect.x + 150, rect.y + 20)


def draw_logs(screen, game):
    draw_text(screen, "События:", config.small_font, GRAY, LOG_X, LOG_Y - 30)
    y = LOG_Y
    for line in game.logs[-LOG_MAX:]:
        draw_text(screen, line, config.small_font, WHITE, LOG_X, y)
        y += LOG_LINE_H


def draw_action_buttons(screen, game):
    if game.phase != "action" or game.game_over:
        return
    for action_id, info in ACTIONS.items():
        draw_button(screen, info["rect"], info["label"], config.text_font)


def draw_target_hint(screen):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))
    draw_text(screen, "Выбери цель (клик справа, Esc — отмена)",
              config.header_font, GOLD, 250, 300)


def draw_modal(screen, game):
    if not game.modal_visible:
        return

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    box = pygame.Rect(250, 250, 700, 200)
    draw_panel(screen, box, bg=PANEL_LIGHT, border=GOLD)

    draw_text(screen, "СОБЫТИЕ", config.header_font, GOLD,
              box.x + 25, box.y + 20)

    lines = wrap_text(game.modal_text, config.text_font, box.width - 50)
    y = box.y + 70
    for line in lines:
        draw_text(screen, line, config.text_font, WHITE, box.x + 25, y)
        y += 30
        draw_text(screen, "Клик — дальше", config.small_font, GRAY,
              box.x + 25, box.y + 165)


def draw_end_screen(screen, game):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    text = f"Победитель: {game.winner.name}" if game.winner else "Ничья! Все погибли"
    draw_text(screen, text, config.title_font, GOLD, 340, 320)

def draw_all(screen, game):
    screen.fill(BACKGROUND)

    draw_title(screen, game)
    draw_kingdom_panel(screen, game.current())
    draw_players_panel(screen, game)
    draw_logs(screen, game)
    draw_action_buttons(screen, game)

    if game.selecting_target:
        draw_target_hint(screen)

    draw_modal(screen, game)

    if game.game_over:
        draw_end_screen(screen, game)

def draw_action_buttons(screen, game):
    from actions import ACTIONS
    from ui import draw_button
    import config
    for action_id, info in ACTIONS.items():
        draw_button(screen, info["rect"], info["label"], config.small_font)