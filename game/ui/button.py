import pygame
from game.config import WHITE, GOLD, BLUE

pygame.font.init()
text_font = pygame.font.Font(None, 28)

def draw_button(screen, rect, text, color=BLUE):
    """Рисует кнопку с рамкой и текстом."""
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, GOLD, rect, width=2, border_radius=8)

    text_surface = text_font.render(text, True, WHITE)
    text_x = rect.x + (rect.width - text_surface.get_width()) // 2
    text_y = rect.y + (rect.height - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))
