import pygame

# =========================
# НАСТРОЙКИ
# =========================

WIDTH = 1200
HEIGHT = 700
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Хроники Четырёх Земель")

clock = pygame.time.Clock()


# =========================
# ЦВЕТА
# =========================

BACKGROUND = (25, 27, 35)
PANEL = (39, 42, 53)
PANEL_LIGHT = (50, 54, 68)

WHITE = (240, 240, 240)
GRAY = (170, 175, 185)

GOLD = (220, 180, 80)
GREEN = (80, 170, 100)
RED = (190, 70, 70)
BLUE = (70, 120, 190)


# =========================
# ШРИФТЫ
# =========================

title_font = pygame.font.Font(None, 48)
header_font = pygame.font.Font(None, 34)
text_font = pygame.font.Font(None, 28)
small_font = pygame.font.Font(None, 24)


# =========================
# ДАННЫЕ ИГРОКА
# =========================

grain = 10
money = 10
land = 5
people = 10
smuta = 0

prestige = land * 2 + money // 5 + people // 5 - smuta


# =========================
# ФУНКЦИИ
# =========================

def draw_text(text, font, color, x, y):
    """Рисует текст на экране."""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_panel(rect, color=PANEL, border_color=GOLD):
    """Рисует панель с рамкой."""
    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(
        screen,
        border_color,
        rect,
        width=2,
        border_radius=12
    )


def draw_button(rect, text, color=BLUE):
    """Рисует кнопку."""
    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        GOLD,
        rect,
        width=2,
        border_radius=8
    )

    text_surface = text_font.render(text, True, WHITE)

    text_x = rect.x + (rect.width - text_surface.get_width()) // 2
    text_y = rect.y + (rect.height - text_surface.get_height()) // 2

    screen.blit(text_surface, (text_x, text_y))


# =========================
# КНОПКИ
# =========================

trade_button = pygame.Rect(40, 590, 180, 55)
bribe_button = pygame.Rect(240, 590, 180, 55)
alliance_button = pygame.Rect(440, 590, 180, 55)
raid_button = pygame.Rect(640, 590, 180, 55)
reform_button = pygame.Rect(840, 590, 180, 55)


# =========================
# ГЛАВНЫЙ ЦИКЛ
# =========================

running = True

while running:

    # -------------------------
    # ОБРАБОТКА СОБЫТИЙ
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:

            if trade_button.collidepoint(event.pos):
                print("Выбрана торговля")

            elif bribe_button.collidepoint(event.pos):
                print("Выбран подкуп")

            elif alliance_button.collidepoint(event.pos):
                print("Выбран союз")

            elif raid_button.collidepoint(event.pos):
                print("Выбран набег")

            elif reform_button.collidepoint(event.pos):
                print("Выбрана реформа")


    # -------------------------
    # ФОН
    # -------------------------

    screen.fill(BACKGROUND)


    # =========================
    # ЗАГОЛОВОК
    # =========================

    draw_text(
        "ХРОНИКИ ЧЕТЫРЁХ ЗЕМЕЛЬ",
        title_font,
        GOLD,
        320,
        25
    )

    draw_text(
        "Ход игрока: 1",
        small_font,
        GRAY,
        520,
        75
    )


    # =========================
    # ПАНЕЛЬ КОРОЛЕВСТВА
    # =========================

    kingdom_panel = pygame.Rect(
        30,
        110,
        300,
        440
    )

    draw_panel(kingdom_panel)

    draw_text(
        "МОЁ КОРОЛЕВСТВО",
        header_font,
        WHITE,
        65,
        135
    )


    # -------------------------
    # РЕСУРСЫ
    # -------------------------

    draw_text("Зерно", text_font, WHITE, 65, 205)
    draw_text(str(grain), text_font, GOLD, 250, 205)

    draw_text("Деньги", text_font, WHITE, 65, 255)
    draw_text(str(money), text_font, GOLD, 250, 255)

    draw_text("Земля", text_font, WHITE, 65, 305)
    draw_text(str(land), text_font, GOLD, 250, 305)

    draw_text("Народ", text_font, WHITE, 65, 355)
    draw_text(str(people), text_font, GOLD, 250, 355)

    draw_text("Смута", text_font, WHITE, 65, 405)
    draw_text(str(smuta), text_font, RED, 250, 405)


    # -------------------------
    # ПРЕСТИЖ
    # -------------------------

    pygame.draw.line(
        screen,
        GOLD,
        (60, 450),
        (300, 450),
        2
    )

    draw_text(
        "ПРЕСТИЖ",
        header_font,
        WHITE,
        65,
        470
    )

    draw_text(
        f"{prestige} / 30",
        header_font,
        GOLD,
        190,
        470
    )


    # =========================
    # ИГРОВОЕ ПОЛЕ
    # =========================

    map_panel = pygame.Rect(
        350,
        110,
        500,
        440
    )

    draw_panel(
        map_panel,
        color=(35, 55, 45),
        border_color=GOLD
    )

    draw_text(
        "КАРТА КОРОЛЕСТВ",
        header_font,
        WHITE,
        490,
        135
    )


    # -------------------------
    # Условная карта
    # -------------------------

    # Земля игрока 1
    pygame.draw.rect(
        screen,
        (80, 120, 80),
        (390, 200, 180, 120),
        border_radius=10
    )

    # Земля игрока 2
    pygame.draw.rect(
        screen,
        (100, 80, 80),
        (620, 200, 180, 120),
        border_radius=10
    )

    # Земля игрока 3
    pygame.draw.rect(
        screen,
        (80, 90, 130),
        (390, 350, 180, 120),
        border_radius=10
    )

    # Земля игрока 4
    pygame.draw.rect(
        screen,
        (130, 110, 70),
        (620, 350, 180, 120),
        border_radius=10
    )


    draw_text(
        "КОРОЛЕВСТВО 1",
        small_font,
        WHITE,
        420,
        245
    )

    draw_text(
        "КОРОЛЕВСТВО 2",
        small_font,
        WHITE,
        650,
        245
    )

    draw_text(
        "КОРОЛЕВСТВО 3",
        small_font,
        WHITE,
        420,
        395
    )

    draw_text(
        "КОРОЛЕВСТВО 4",
        small_font,
        WHITE,
        650,
        395
    )


    # =========================
    # ПАНЕЛЬ СОБЫТИЯ
    # =========================

    event_panel = pygame.Rect(
        870,
        110,
        300,
        440
    )

    draw_panel(event_panel)

    draw_text(
        "СОБЫТИЕ",
        header_font,
        WHITE,
        970,
        140
    )

    draw_text(
        "ЗАСУХА",
        header_font,
        RED,
        950,
        210
    )

    draw_text(
        "-3 зерна",
        text_font,
        WHITE,
        970,
        260
    )

    draw_text(
        "Засуха обрушилась",
        small_font,
        GRAY,
        915,
        330
    )

    draw_text(
        "на ваше королевство.",
        small_font,
        GRAY,
        915,
        360
    )

    draw_text(
        "Теперь выберите действие.",
        small_font,
        GRAY,
        900,
        410
    )


    # =========================
    # КНОПКИ
    # =========================

    draw_button(
        trade_button,
        "ТОРГОВЛЯ",
        GREEN
    )

    draw_button(
        bribe_button,
        "ПОДКУП",
        BLUE
    )

    draw_button(
        alliance_button,
        "СОЮЗ",
        BLUE
    )

    draw_button(
        raid_button,
        "НАБЕГ",
        RED
    )

    draw_button(
        reform_button,
        "РЕФОРМА",
        GREEN
    )


    # =========================
    # ОБНОВЛЕНИЕ ЭКРАНА
    # =========================

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
