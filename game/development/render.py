from pathlib import Path
import pygame
import config
from config import (
    WIDTH,
    HEIGHT,
    BACKGROUND,
    PANEL,
    PANEL_LIGHT,
    WHITE,
    GRAY,
    GOLD,
    GREEN,
    RED,
    WIN_PRESTIGE,
    KINGDOM_PANEL,
    PLAYER_PANEL_X,
    PLAYER_PANEL_Y0,
    PLAYER_PANEL_W,
    PLAYER_PANEL_H,
    PLAYER_PANEL_STEP,
    LOG_X,
    LOG_Y,
    LOG_LINE_H,
    LOG_MAX,
)

from actions import ACTIONS
from ui import draw_text, draw_panel, draw_button, wrap_text

_ICONS = None


def _get_icons():
    global _ICONS
    if _ICONS is not None:
        return _ICONS
    _ICONS = {}
    root_dir = Path(__file__).resolve().parents[2]
    icons_dir = root_dir / "assets" / "icons"
    for key in ("grain", "money", "land", "people", "smuta"):
        icon_path = icons_dir / f"{key}.png"
        if icon_path.exists():
            try:
                img = pygame.image.load(str(icon_path))
                if pygame.display.get_surface() is not None:
                    img = img.convert_alpha()
                _ICONS[key] = pygame.transform.smoothscale(img, (28, 28))
            except Exception:
                pass
    return _ICONS


def draw_title(screen, game):
    draw_text(screen, "ХРОНИКИ ЧЕТЫРЁХ ЗЕМЕЛЬ", config.title_font, GOLD, 320, 22)
    current_player = game.current()
    draw_text(
        screen,
        f"Раунд: {game.turn_number}  |  Ходит: {current_player.name}",
        config.small_font,
         current_player.color,
        430,
        72,
    )


def draw_kingdom_panel(screen, player):
    draw_panel(screen, KINGDOM_PANEL)
    draw_text(screen, "МОЁ КОРОЛЕВСТВО", config.header_font, WHITE, 55, 130)
    draw_text(screen, player.name, config.text_font, player.color, 55, 168)

    icons = _get_icons()
    rows = [
        ("grain", "Зерно", player.grain),
        ("money", "Деньги", player.money),
        ("land", "Земля", player.land),
        ("people", "Народ", player.people),
        ("smuta", "Смута", player.smuta),
    ]
    y = 215
    for key, label, value in rows:
        icon = icons.get(key)
        if icon:
            screen.blit(icon, (50, y - 4))
            label_x = 88
        else:
            label_x = 65
        draw_text(screen, label, config.text_font, WHITE, label_x, y)
        if key == "smuta":
            color = RED if value >= 7 else (GOLD if value >= 4 else GREEN)
        else:
            color = GOLD
        draw_text(screen, str(value), config.text_font, color, 260, y)
        y += 42

    pygame.draw.line(screen, GOLD, (50, 440), (305, 440), 2)
    draw_text(screen, "ПРЕСТИЖ", config.header_font, WHITE, 55, 465)
    draw_text(
        screen,
        f"{int(player.prestige)} / {WIN_PRESTIGE}",
        config.header_font,
        GOLD,
        200,
        465,
    )


def draw_players_panel(screen, game):
    current_player = game.current()
    for i, p in enumerate(game.players):
        rect = pygame.Rect(
            PLAYER_PANEL_X,
            PLAYER_PANEL_Y0 + i * PLAYER_PANEL_STEP,
            PLAYER_PANEL_W,
            PLAYER_PANEL_H,
        )
        if p.dead:
            bg_color = (28, 30, 38)       # Тёмно-серый приглушённый фон
            border = (90, 55, 55)         # Тускло-бордовая рамка
            name_color = GRAY             # Серое название
            info_color = (115, 120, 130)  # Серые ресурсы
            prestige_color = (130, 120, 95)
        else:
            bg_color = PANEL
            border = GOLD if p is current_player else PANEL_LIGHT
            name_color = p.color
            info_color = WHITE
            prestige_color = GOLD

        draw_panel(screen, rect, bg=bg_color, border=border)

        draw_text(screen, p.name, config.text_font, name_color, rect.x + 15, rect.y + 10)

        info = (
            f"Зерно:{p.grain} Д:{p.money} Зем:{p.land} "
            f"Нар:{p.people} См:{p.smuta}"
        )
        draw_text(screen, info, config.small_font, info_color, rect.x + 15, rect.y + 42)

        draw_text(
            screen,
            f"Престиж: {int(p.prestige)} / {WIN_PRESTIGE}",
            config.small_font,
            prestige_color,
            rect.x + 15,
            rect.y + 70,
        )

        if p.dead:
            # Аккуратная плашка «ПОГИБЛО» в правом нижнем углу без наложения на текст
            badge_rect = pygame.Rect(rect.right - 108, rect.y + 65, 96, 26)
            pygame.draw.rect(screen, (75, 35, 35), badge_rect, border_radius=6)
            pygame.draw.rect(screen, RED, badge_rect, width=1, border_radius=6)
            lbl = config.small_font.render("ПОГИБЛО", True, RED)
            screen.blit(
                lbl,
                (
                    badge_rect.x + (badge_rect.width - lbl.get_width()) // 2,
                    badge_rect.y + (badge_rect.height - lbl.get_height()) // 2,
                ),
            )


def draw_logs(screen, game):
    center_panel = pygame.Rect(350, 110, 510, 440)
    draw_panel(screen, center_panel, bg=PANEL, border=GOLD)
    draw_text(
        screen,
        "ХРОНИКА СОБЫТИЙ И ДЕЙСТВИЙ",
        config.header_font,
        GOLD,
        LOG_X,
        125,
    )

    max_width = center_panel.width - 40
    max_lines = (center_panel.bottom - 15 - LOG_Y) // LOG_LINE_H
    all_lines = []
    for entry in game.logs:
        all_lines.extend(wrap_text(entry, config.small_font, max_width))

    y = LOG_Y
    for line in all_lines[-max_lines:]:
        draw_text(screen, line, config.small_font, WHITE, LOG_X, y)
        y += LOG_LINE_H

def draw_action_buttons(screen, game):
    if game.game_over:
        return
    mouse_pos = pygame.mouse.get_pos()
    for action_id, info in ACTIONS.items():
        enabled = (
            game.phase == "action"
            and not game.modal_visible
            and game.can_act(action_id)
        )
        hovered = enabled and info["rect"].collidepoint(mouse_pos)
        draw_button(
            screen,
            info["rect"],
            info["label"],
            config.small_font,
            enabled=enabled,
            hovered=hovered,
            sublabel=info.get("cost_label"),
            small_font=config.small_font,
        )


def draw_target_hint(screen):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))
    draw_text(
        screen,
        "Выберите королевство-цель справа (клик мыши, Esc — отмена)",
        config.header_font,
        GOLD,
        180,
        310,
    )


def draw_modal(screen, game):
    if not game.modal_visible:
        return

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 165))
    screen.blit(overlay, (0, 0))

    box = pygame.Rect(250, 230, 700, 220)
    draw_panel(screen, box, bg=PANEL_LIGHT, border=GOLD)

    title = getattr(game, "modal_title", "") or "СОБЫТИЕ"
    draw_text(
        screen,
        f"СОБЫТИЕ ХОДА: {title.upper()}",
        config.header_font,
        GOLD,
        box.x + 25,
        box.y + 22,
    )

    lines = wrap_text(game.modal_text, config.text_font, box.width - 50)
    y = box.y + 80
    for line in lines:
        draw_text(screen, line, config.text_font, WHITE, box.x + 25, y)
        y += 32

    draw_text(
        screen,
        "Нажмите любую клавишу или кнопку мыши, чтобы перейти к действию...",
        config.small_font,
        GRAY,
        box.x + 25,
        box.y + 175,
    )


def draw_end_screen(screen, game):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 190))
    screen.blit(overlay, (0, 0))

    box = pygame.Rect(250, 230, 700, 220)
    draw_panel(screen, box, bg=PANEL_LIGHT, border=GOLD)

    text = (
        f"Победитель: {game.winner.name}!"
        if game.winner
        else "Ничья! Все королевства пали"
    )
    draw_text(screen, "ИГРА ОКОНЧЕНА", config.header_font, WHITE, box.x + 250, box.y + 35)
    draw_text(screen, text, config.title_font, GOLD, box.x + 60, box.y + 95)
    draw_text(
        screen,
        "Нажмите R для новой партии или закройте окно",
        config.small_font,
        GRAY,
        box.x + 165,
        box.y + 170,
    )


def draw_all(screen, game):
    if config.title_font is None:
        config.init_fonts()
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
