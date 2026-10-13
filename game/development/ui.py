import pygame
from config import PANEL, GOLD, BLUE, WHITE

def draw_text(screen, message, font, color, x, y):
    surface = font.render(message, True, color)
    screen.blit(surface, (x, y))

def draw_panel(screen, rect, bg=PANEL, border=GOLD):
    pygame.draw.rect(screen, bg, rect, border_radius=12)
    pygame.draw.rect(screen, border, rect, width=2, border_radius=12)

def draw_button(screen, rect, label, font):
    pygame.draw.rect(screen, BLUE, rect, border_radius=8)
    pygame.draw.rect(screen, GOLD, rect, width=2, border_radius=8)

    surface = font.render(label, True, WHITE)
    tx = rect.x + (rect.width - surface.get_width()) // 2
    ty = rect.y + (rect.height - surface.get_height()) // 2
    screen.blit(surface, (tx, ty))

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines