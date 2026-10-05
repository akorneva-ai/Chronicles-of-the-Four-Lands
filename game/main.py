import pygame
import sys
from game.config import *
from game.ui.button import draw_button
from game.ui.panel import draw_panel, draw_text

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Хроники Четырёх Земель")
    clock = pygame.time.Clock()

    title_font = pygame.font.Font(None, 48)
    header_font = pygame.font.Font(None, 34)
    text_font = pygame.font.Font(None, 28)
    small_font = pygame.font.Font(None, 24)

    # Игровые ресурсы
    grain, money, land, people, smuta = 10, 10, 5, 10, 0
    prestige = land * 2 + money // 5 + people // 5 - smuta

    # Интерактивные зоны
    trade_button = pygame.Rect(40, 590, 180, 55)
    bribe_button = pygame.Rect(240, 590, 180, 55)
    alliance_button = pygame.Rect(440, 590, 180, 55)
    raid_button = pygame.Rect(640, 590, 180, 55)
    reform_button = pygame.Rect(840, 590, 180, 55)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if trade_button.collidepoint(event.pos): print("Выбрана торговля")
                elif bribe_button.collidepoint(event.pos): print("Выбран подкуп")
                elif alliance_button.collidepoint(event.pos): print("Выбран союз")
                elif raid_button.collidepoint(event.pos): print("Выбран набег")
                elif reform_button.collidepoint(event.pos): print("Выбрана реформа")

        screen.fill(BACKGROUND)

        # Заголовки
        draw_text(screen, "ХРОНИКИ ЧЕТЫРЁХ ЗЕМЕЛЬ", title_font, GOLD, 320, 25)
        draw_text(screen, "Ход игрока: 1", small_font, GRAY, 520, 75)

        # Панель состояния
        kingdom_panel = pygame.Rect(30, 110, 300, 440)
        draw_panel(screen, kingdom_panel)
        draw_text(screen, "МОЁ КОРОЛЕВСТВО", header_font, WHITE, 65, 135)

        draw_text(screen, "Зерно", text_font, WHITE, 65, 205)
        draw_text(screen, str(grain), text_font, GOLD, 250, 205)
        draw_text(screen, "Деньги", text_font, WHITE, 65, 255)
        draw_text(screen, str(money), text_font, GOLD, 250, 255)
        draw_text(screen, "Земля", text_font, WHITE, 65, 305)
        draw_text(screen, str(land), text_font, GOLD, 250, 305)
        draw_text(screen, "Народ", text_font, WHITE, 65, 355)
        draw_text(screen, str(people), text_font, GOLD, 250, 355)
        draw_text(screen, "Смута", text_font, WHITE, 65, 405)
        draw_text(screen, str(smuta), text_font, RED, 250, 405)

        pygame.draw.line(screen, GOLD, (60, 450), (300, 450), 2)
        draw_text(screen, "ПРЕСТИЖ", header_font, WHITE, 65, 470)
        draw_text(screen, f"{prestige} / 30", header_font, GOLD, 190, 470)

        # Карта
        map_panel = pygame.Rect(350, 110, 500, 440)
        draw_panel(screen, map_panel, color=(35, 55, 45))
        draw_text(screen, "КАРТА КОРОЛЕВСТВ", header_font, WHITE, 490, 135)

        pygame.draw.rect(screen, (80, 120, 80), (390, 200, 180, 120), border_radius=10)
        pygame.draw.rect(screen, (100, 80, 80), (620, 200, 180, 120), border_radius=10)
        pygame.draw.rect(screen, (80, 90, 130), (390, 350, 180, 120), border_radius=10)
        pygame.draw.rect(screen, (130, 110, 70), (620, 350, 180, 120), border_radius=10)

        draw_text(screen, "КОРОЛЕВСТВО 1", small_font, WHITE, 420, 245)
        draw_text(screen, "КОРОЛЕВСТВО 2", small_font, WHITE, 650, 245)
        draw_text(screen, "КОРОЛЕВСТВО 3", small_font, WHITE, 420, 395)
        draw_text(screen, "КОРОЛЕВСТВО 4", small_font, WHITE, 650, 395)

        # Панель события
        event_panel = pygame.Rect(870, 110, 300, 440)
        draw_panel(screen, event_panel)
        draw_text(screen, "СОБЫТИЕ", header_font, WHITE, 970, 140)
        draw_text(screen, "ЗАСУХА", header_font, RED, 950, 210)
        draw_text(screen, "-3 зерна", text_font, WHITE, 970, 260)
        draw_text(screen, "Засуха обрушилась", small_font, GRAY, 915, 330)
        draw_text(screen, "на ваше королевство.", small_font, GRAY, 915, 360)
        draw_text(screen, "Теперь выберите действие.", small_font, GRAY, 900, 410)

        # Отрисовка интерактивных элементов
        draw_button(screen, trade_button, "ТОРГОВЛЯ", GREEN)
        draw_button(screen, bribe_button, "ПОДКУП", BLUE)
        draw_button(screen, alliance_button, "СОЮЗ", BLUE)
        draw_button(screen, raid_button, "НАБЕГ", RED)
        draw_button(screen, reform_button, "РЕФОРМА", GREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
