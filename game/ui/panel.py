import pygame
from game.config import PANEL, GOLD

def draw_text(screen, text, font, color, x, y):
    """Рисует текст на экране."""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_panel(screen, rect, color=PANEL, border_color=GOLD):
    """Рисует панель с рамкой."""
    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, border_color, rect, width=2, border_radius=12)
