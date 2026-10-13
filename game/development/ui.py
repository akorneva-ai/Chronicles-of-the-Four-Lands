import pygame
from config import PANEL, GOLD, BLUE, BLUE_HOVER, DARK_GRAY, WHITE, GRAY


def draw_text(screen, message, font, color, x, y):
    surface = font.render(str(message), True, color)
    screen.blit(surface, (x, y))


def draw_panel(screen, rect, bg=PANEL, border=GOLD):
    pygame.draw.rect(screen, bg, rect, border_radius=12)
    pygame.draw.rect(screen, border, rect, width=2, border_radius=12)


def draw_button(
    screen,
    rect,
    label,
    font,
    enabled=True,
    hovered=False,
    sublabel=None,
    small_font=None,
):
    if not enabled:
        bg_color = DARK_GRAY
        border_color = GRAY
        text_color = GRAY
    elif hovered:
        bg_color = BLUE_HOVER
        border_color = GOLD
        text_color = WHITE
    else:
        bg_color = BLUE
        border_color = GOLD
        text_color = WHITE

    pygame.draw.rect(screen, bg_color, rect, border_radius=8)
    pygame.draw.rect(screen, border_color, rect, width=2, border_radius=8)

    surface = font.render(label, True, text_color)
    tx = rect.x + (rect.width - surface.get_width()) // 2
    if sublabel and small_font:
        ty = rect.y + 8
        screen.blit(surface, (tx, ty))
        sub_surf = small_font.render(sublabel, True, GOLD if enabled else GRAY)
        stx = rect.x + (rect.width - sub_surf.get_width()) // 2
        screen.blit(sub_surf, (stx, rect.y + 34))
    else:
        ty = rect.y + (rect.height - surface.get_height()) // 2
        screen.blit(surface, (tx, ty))


def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines
